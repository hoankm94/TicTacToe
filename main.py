import pygame
import board

pygame.init()

pygame.display.set_caption("Tic Tac Toe by Tuticoi")

clicked = False
run = True
player = 1



while run:
    board.draw_grid()
    board.draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if board.markers[cell_x // 300][cell_y // 300] == 0:
                board.markers[cell_x // 300][cell_y // 300] = player
                player *= -1
    pygame.display.update()

pygame.quit()