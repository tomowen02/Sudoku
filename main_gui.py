from sudoku_board import Sudoku_Board
import pygame
import sys

# Initialise components
pygame.init()
pygame.font.init()
board = Sudoku_Board()


# Canvas dimensions
WIDTH = 594
HEIGHT = 594

# Colors
C_RED = (255, 0, 0)
C_BG = (20, 189, 172)
C_GRID = (13, 161, 146)
C_DIGIT = (84, 84, 84)
C_ACCENT = (14, 138, 125)

# Fonts
font = pygame.font.SysFont("Arial", 40)


# Variables
selected_x = 0
selected_y = 3
if WIDTH < HEIGHT:
    diff = WIDTH // 9
else:
    diff = HEIGHT // 9

# Set up canvas
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
canvas.fill(C_BG)


def get_cords(pos):
    global selected_x
    selected_x = pos[0] // diff
    global selected_y
    selected_y = pos[1]//diff

def draw_grid():
    # Draw grid lines
    for i in range(1, 9):
        if i % 3 == 0:
            thinkness = 3
        else:
            thinkness = 1
        # Horizontal
        pygame.draw.line(canvas, C_GRID, (0, i * diff), (diff * 9, i*diff), thinkness)
        # Vertical
        pygame.draw.line(canvas, C_GRID, (i * diff, 0), (i * diff, diff * 9), thinkness)
    
    # Draw numbers
    grid = board.get_board()
    x_font_offset = 22
    y_font_offset = 10
    for x in range(9):
        for y in range(9):
            digit_text = font.render(str(grid[y][x]), 1, C_DIGIT)
            canvas.blit(digit_text, (x * diff + x_font_offset, diff * 8 - y * diff + y_font_offset))

# Highlight selected box
def draw_box():
    for i in range(2):
        # Horizontal
        pygame.draw.line(canvas, C_ACCENT, (selected_x * diff - 1, diff*(selected_y + i)), (selected_x * diff + diff + 1, diff*(selected_y + i)), 3)
        # Vertical
        pygame.draw.line(canvas, C_ACCENT, (diff*(selected_x + i), selected_y * diff - 1), (diff*(selected_x + i), selected_y * diff + diff + 1), 3)


draw_grid()
draw_box()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()