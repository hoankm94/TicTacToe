import pygame
import board

pygame.init()

pygame.display.set_caption("Tic Tac Toe by Tuticoi")

run = True
while run:
    board.draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()