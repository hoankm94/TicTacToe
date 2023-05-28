import pygame


width = 900
height = 900

line_width = 5

screen = pygame.display.set_mode((width, height))

def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 300), (width, x * 300), line_width)
        pygame.draw.line(screen, grid, (x * 300, 0), (x * 300, width), line_width)