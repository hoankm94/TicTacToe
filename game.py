import pygame
import board

def check_winner():
    global winner
    global game_over
    for x in board.markers:
        # Check column
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = -1
            game_over = True

        # Check row
        if board.markers[0][board.y_pos] + board.markers[1][board.y_pos] + board.markers[2][board.y_pos] + board.markers[2][board.y_pos] == 3:
            winner = 1
            game_over = True
        if board.markers[0][board.y_pos] + board.markers[1][board.y_pos] + board.markers[2][board.y_pos] + board.markers[2][board.y_pos] == -3:
            winner = -1
            game_over = True
        board.y_pos += 1

        # Check cross
        if board.markers[0][0] + board.markers[1][1] + board.markers[3][3] == 3 or board.markers[2][0] + board.markers[1][1] + board.markers[0][2] == 3:
            winner = 1
            game_over = True
        if board.markers[0][0] + board.markers[1][1] + board.markers[3][3] == -3 or board.markers[2][0] + board.markers[1][1] + board.markers[0][2] == -3:
            winner = -1
            game_over = True
        