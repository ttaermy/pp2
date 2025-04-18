import pygame
import random

pygame.init()

try:
    food_sound = pygame.mixer.Sound('catch.mp3')
    direction_sound = pygame.mixer.Sound('gotcoin.wav')  # Changed to use gotcoin.wav
    direction_sound.set_volume(0.3)
except:
    print("Could not load sound files")
    direction_sound = None
    food_sound = None

# экран
WIDTH, HEIGHT = 800, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# размеры и цвета
BLOCK = 20
BLACK = (0, 0, 0)
GRAY = (240, 240, 240)
WHITE = (255, 255, 255)
SNAKE = (0, 200, 180)
BG_GRID = (50, 50, 50, 180)
MARGIN = 1
GRID_ROWS = 30
GRID_COLS = 30
BG_PADDING = 10
RED = (255, 0, 0)

try:
    head_img = pygame.image.load('snake_head.jpg').convert_alpha()
    head_img = pygame.transform.scale(head_img, (BLOCK, BLOCK))  # Resize to match block size
    use_head_image = True
except:
    print("Could not load snake_head.png, using rectangle instead")
    use_head_image = False

# координаты сетки
grid_width = GRID_COLS * BLOCK + (GRID_COLS + 1) * MARGIN
grid_height = GRID_ROWS * BLOCK + (GRID_ROWS + 1) * MARGIN
start_x = (WIDTH - grid_width) // 2
start_y = (HEIGHT - grid_height) // 2

# задний фон
def create_background(screen, width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(screen, colors[(row + col) % 2],pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width

done = False

# шрифт
font = pygame.font.SysFont("arial", 24)

# класс блока змейки
class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# класс еды с весом и временем исчезновения
class FoodItem:
    def __init__(self, x, y, weight, ttl):
        self.x = x
        self.y = y
        self.weight = weight
        self.ttl = ttl

    def is_expired(self):
        return self.ttl <= 0

    def tick(self):
        self.ttl -= 1

# начальная змейка
snake_block = [SnakeBlock(13, 13)]
dx, dy = 1, 0  # движение вправо

# таймер и скорость
clock = pygame.time.Clock()
speed = 15
move_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_event, 150)

# счёт и уровень
score = 0
level = 1

# отрисовка блока
def draw_block(color, row, column, is_head=False, direction=(0,0)):
    x = start_x + column * BLOCK + MARGIN * (column + 1)
    y = start_y + row * BLOCK + MARGIN * (row + 1)
    
    if is_head and use_head_image:
        # Двигаем голову в нужную сторону
        angle = 0
        if direction == (0, -1):  # up
            angle = 90
        elif direction == (0, 1):  # down
            angle = 270
        elif direction == (-1, 0):  # left
            angle = 180
        # когда право, не нужно
        
        rotated_head = pygame.transform.rotate(head_img, angle)
        screen.blit(rotated_head, (x, y))
    else:
        pygame.draw.rect(screen, color, [x, y, BLOCK, BLOCK])

# генерация еды не на змейке
def generate_food():
    while True:
        x = random.randint(0, GRID_ROWS - 1)
        y = random.randint(0, GRID_COLS - 1)
        occupied = any(block.x == x and block.y == y for block in snake_block)
        if not occupied:
            weight = random.choice([1, 2, 3])
            ttl = random.randint(300, 500)  # 5–8 сек
            return FoodItem(x, y, weight, ttl)

# еда
food = generate_food()

# запуск
running = True
while running:
    clock.tick(speed)

    # управление 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            old_dx, old_dy = dx, dy  # Store old direction
            
            if event.key == pygame.K_a and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_d and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_w and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_s and dx == 0:
                dx, dy = 1, 0
            
            # Звук если поменяли направление
            if (dx, dy) != (old_dx, old_dy) and direction_sound:
                direction_sound.play()

        elif event.type == move_event:
            head = snake_block[-1]
            new_x = head.x + dx
            new_y = head.y + dy


            # проверка выхода за границу 
            if not (0 <= new_x < GRID_ROWS and 0 <= new_y < GRID_COLS):
                print("Game Over: out of bounds!", "Your Score is", score)
                running = False
                break

            # столкновение с телом
            if any(block.x == new_x and block.y == new_y for block in snake_block):
                print("Game Over: hit itself!", "Your Score is", score)
                running = False
                break

            new_head = SnakeBlock(new_x, new_y)
            snake_block.append(new_head)

            # сьел еду
            if new_x == food.x and new_y == food.y:
                food_sound.play()
                score += food.weight
                food = generate_food()

                # уровень 
                if score % 3 == 0:
                    level += 1
                    speed += 2
            else:
                snake_block.pop(0)

            # уменьшаем таймер еды
            food.tick()
            if food.is_expired():
                food = generate_food()

    screen.fill(BLACK)

    # сетка
    for row in range(GRID_ROWS):
        for column in range(GRID_COLS):
            # Красные края
            if row == 0 or row == GRID_ROWS-1 or column == 0 or column == GRID_COLS-1:
                draw_block(RED, row, column)
            else:
                color = GRAY if (row + column) % 2 == 0 else WHITE
                draw_block(color, row, column)

    # еда с цветом в зависимости от веса
    if food.weight == 1:
        FOOD_COLOR = (200, 50, 50)
    elif food.weight == 2:
        FOOD_COLOR = (255, 165, 0)
    else:
        FOOD_COLOR = (255, 215, 0)
    draw_block(FOOD_COLOR, food.x, food.y)

    # змейка 
    for i, block in enumerate(snake_block):
        if i == len(snake_block) - 1:  #Голова
            draw_block(SNAKE, block.x, block.y, is_head=True, direction=(dx, dy))
        else:
            draw_block(SNAKE, block.x, block.y)
    

    # счёт и уровень
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (2, 2))

    # таймер еды 
    seconds_left = max(1, food.ttl // 40)
    timer_text = font.render(f"Food disappears in: {seconds_left}s", True, WHITE)
    screen.blit(timer_text, (WIDTH - 250, 2))

    pygame.display.flip()

pygame.quit()