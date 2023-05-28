import pygame


width = 900
height = 900
line_width = 5
marker_width = 8

# Define colors
green = (0, 255, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode((width, height))

def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 300), (width, x * 300), line_width)
        pygame.draw.line(screen, grid, (x * 300, 0), (x * 300, width), line_width)

markers = []
for x in range(3):
    row = [0] * 3
    markers.append(row)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 300 + 50, y_pos * 300 + 50), (x_pos * 300 + 250, y_pos * 300 + 250), marker_width)
                pygame.draw.line(screen, green, (x_pos * 300 + 50, y_pos * 300 + 250), (x_pos * 300 + 250, y_pos * 300 + 50), marker_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 300 + 150, y_pos * 300 + 150), 100, marker_width)
            y_pos += 1
        x_pos += 1