import pygame
import sys

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Create the Connect 4 board
def create_board():
    board = [[0] * COLUMN_COUNT for _ in range(ROW_COUNT)]
    return board

# Draw the Connect 4 board
def draw_board(board):
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), border_radius=10)

# Main display loop
def display_loop():
    board = create_board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        draw_board(board)
        pygame.display.update()

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4 Display")

# Run the display loop
display_loop()
