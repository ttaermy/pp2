import pygame
import math

# Initialize pygame
pygame.init()

# Screen setup
screen_width, screen_height = 900, 700
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))  # White background
pygame.display.set_caption('Advanced Paint')

# Drawing variables
draw_on = False
last_pos = (0, 0)
radius = 5  # Default brush size
color = (0, 0, 0)  # Default color (black)
mode = 'pen'  # Current drawing mode
start_pos = None  # For shape drawing

# Color definitions
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
COLORS = [RED, GREEN, BLUE, BLACK, YELLOW, PURPLE]

# Toolbar setup
toolbar_width = 60
tool_height = 60
font = pygame.font.SysFont('Arial', 14)

def draw_toolbar():
    """Draw the toolbar with color and tool options"""
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, toolbar_width, screen_height))
    
    # Draw color selection buttons
    for i, col in enumerate(COLORS):
        pygame.draw.rect(screen, col, (10, 10 + i * 40, 40, 30))
    
    # Draw tool selection buttons
    tools = ['pen', 'eraser', 'rect', 'square', 'circle', 
             'rtri', 'etri', 'rhomb']
    tool_names = ['Pen', 'Eraser', 'Rect', 'Square', 'Circle', 
                  'RTri', 'ETri', 'Rhom']
    
    for i, (tool, name) in enumerate(zip(tools, tool_names)):
        pygame.draw.rect(screen, (240, 240, 240), (10, 250 + i * 50, 40, 40))
        text = font.render(name[:4], True, BLACK)
        screen.blit(text, (15, 260 + i * 50))
    
    # Highlight current tool
    if mode in tools:
        index = tools.index(mode)
        pygame.draw.rect(screen, (100, 100, 255), (10, 250 + index * 50, 40, 40), 2)

def roundline(canvas, color, start, end, radius=1):
    """Draw a smooth line between two points"""
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(canvas, color, (x, y), radius)

def draw_equilateral_triangle(surface, color, start, end):
    """Draw equilateral triangle with base at start and height to end"""
    base_length = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    
    # Calculate the three points
    if end[0] > start[0]:  # Dragging right
        left = (start[0], start[1])
        right = (end[0], start[1])
    else:  # Dragging left
        left = (end[0], start[1])
        right = (start[0], start[1])
    
    top = (start[0] + (end[0] - start[0]) // 2, end[1])
    
    pygame.draw.polygon(surface, color, [left, right, top])

def draw_right_triangle(surface, color, start, end):
    """Draw right triangle with right angle at start point"""
    pygame.draw.polygon(surface, color, [
        start,
        (start[0], end[1]),
        end
    ])

def draw_rhombus(surface, color, start, end):
    """Draw rhombus centered around start point"""
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    
    points = [
        (start[0], start[1] - height),  # Top
        (start[0] + width, start[1]),   # Right
        (start[0], start[1] + height), # Bottom
        (start[0] - width, start[1])   # Left
    ]
    pygame.draw.polygon(surface, color, points)

# Initial toolbar drawing
draw_toolbar()

# Main game loop
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        # Handle mouse button down
        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            # Check if click is in toolbar
            if pos[0] < toolbar_width:
                # Check color selection
                for i, col in enumerate(COLORS):
                    if 10 <= pos[0] <= 50 and 10 + i * 40 <= pos[1] <= 40 + i * 40:
                        color = col
                
                # Check tool selection
                tools = ['pen', 'eraser', 'rect', 'square', 'circle', 
                         'rtri', 'etri', 'rhomb']
                for i, tool in enumerate(tools):
                    if 10 <= pos[0] <= 50 and 250 + i * 50 <= pos[1] <= 290 + i * 50:
                        mode = tool
                
                # Redraw toolbar to update highlights
                draw_toolbar()
            else:
                # Start drawing or shape creation
                draw_on = True
                start_pos = pos
                if mode == 'pen' or mode == 'eraser':
                    current_color = WHITE if mode == 'eraser' else color
                    pygame.draw.circle(screen, current_color, pos, radius)

        # Handle mouse button release
        if e.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if start_pos and pos[0] > toolbar_width:
                if mode == 'rect':
                    rect = pygame.Rect(
                        min(start_pos[0], pos[0]),
                        min(start_pos[1], pos[1]),
                        abs(pos[0] - start_pos[0]),
                        abs(pos[1] - start_pos[1])
                    )
                    pygame.draw.rect(screen, color, rect, radius)
                elif mode == 'square':
                    size = max(abs(pos[0] - start_pos[0]), abs(pos[1] - start_pos[1]))
                    rect = pygame.Rect(
                        start_pos[0] if pos[0] > start_pos[0] else start_pos[0] - size,
                        start_pos[1] if pos[1] > start_pos[1] else start_pos[1] - size,
                        size, size
                    )
                    pygame.draw.rect(screen, color, rect, radius)
                elif mode == 'circle':
                    radius_circle = int(((pos[0] - start_pos[0])**2 + (pos[1] - start_pos[1])**2)**0.5)
                    pygame.draw.circle(screen, color, start_pos, radius_circle, radius)
                elif mode == 'rtri':
                    draw_right_triangle(screen, color, start_pos, pos)
                elif mode == 'etri':
                    draw_equilateral_triangle(screen, color, start_pos, pos)
                elif mode == 'rhomb':
                    draw_rhombus(screen, color, start_pos, pos)
            
            draw_on = False
            start_pos = None

        # Handle mouse motion (drawing)
        if e.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if draw_on and pos[0] > toolbar_width:
                if mode == 'pen':
                    pygame.draw.circle(screen, color, pos, radius)
                    roundline(screen, color, pos, last_pos, radius)
                elif mode == 'eraser':
                    pygame.draw.circle(screen, WHITE, pos, radius)
                    roundline(screen, WHITE, pos, last_pos, radius)
            last_pos = pos

    pygame.display.flip()

pygame.quit()