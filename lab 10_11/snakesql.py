import pygame
import sqlite3
import sys
import random
import psycopg2

# Initialize DB

db = psycopg2.connect(dbname='suppliers', user='postgres', password='postgres', host='localhost')
current = db.cursor()
def init_db():
    conn = sqlite3.connect("snake_game.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_score (
            user_id INTEGER,
            level INTEGER,
            score INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect("snake_game.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    if user is None:
        c.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        user_id = c.lastrowid
    else:
        user_id = user[0]
    c.execute("SELECT level, score FROM user_score WHERE user_id = ?", (user_id,))
    progress = c.fetchone()
    conn.close()
    return user_id, (progress if progress else (1, 0))

def save_score(user_id, level, score):
    conn = sqlite3.connect("snake_game.db")
    c = conn.cursor()
    c.execute("REPLACE INTO user_score (user_id, level, score) VALUES (?, ?, ?)", (user_id, level, score))
    conn.commit()
    conn.close()

# Game Variables
BLOCK_SIZE = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

def draw_snake(snake, screen):
    for block in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*block, BLOCK_SIZE, BLOCK_SIZE))

def draw_food(food, screen):
    pygame.draw.rect(screen, (255, 0, 0), (*food, BLOCK_SIZE, BLOCK_SIZE))

def generate_food(snake):
    while True:
        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if (x, y) not in snake:
            return (x, y)

def get_walls(level):
    walls = []
    if level >= 2:
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            walls.append((x, 0))
            walls.append((x, SCREEN_HEIGHT - BLOCK_SIZE))
    if level >= 3:
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            walls.append((0, y))
            walls.append((SCREEN_WIDTH - BLOCK_SIZE, y))
    return walls

def draw_walls(walls, screen):
    for wall in walls:
        pygame.draw.rect(screen, (100, 100, 100), (*wall, BLOCK_SIZE, BLOCK_SIZE))

def main(username):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game with Levels and Save")
    clock = pygame.time.Clock()

    user_id, (level, saved_score) = get_user(username)
    speed = 10 + (level - 1) * 3

    font = pygame.font.SysFont(None, 30)

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (BLOCK_SIZE, 0)
    food = generate_food(snake)
    score = saved_score
    walls = get_walls(level)

    paused = False
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_snake(snake, screen)
        draw_food(food, screen)
        draw_walls(walls, screen)

        score_text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(user_id, level, score)
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_score(user_id, level, score)
                elif not paused:
                    if event.key == pygame.K_UP and direction[1] == 0:
                        direction = (0, -BLOCK_SIZE)
                    elif event.key == pygame.K_DOWN and direction[1] == 0:
                        direction = (0, BLOCK_SIZE)
                    elif event.key == pygame.K_LEFT and direction[0] == 0:
                        direction = (-BLOCK_SIZE, 0)
                    elif event.key == pygame.K_RIGHT and direction[0] == 0:
                        direction = (BLOCK_SIZE, 0)

        if paused:
            clock.tick(3)
            continue

        # Move Snake
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)

        # Check for food
        if head == food:
            score += 10
            food = generate_food(snake)
            if score >= 50 * level:
                level += 1
                speed += 3
                walls = get_walls(level)
        else:
            snake.pop()

        # Check for collisions
        if (head in snake[1:] or
            head[0] < 0 or head[0] >= SCREEN_WIDTH or
            head[1] < 0 or head[1] >= SCREEN_HEIGHT or
            head in walls):
            save_score(user_id, level, score)
            running = False

        clock.tick(speed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    init_db()
    username = input("Enter your username: ")
    main(username)
