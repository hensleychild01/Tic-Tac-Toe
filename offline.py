import pygame
from board import Board
from settings import win

def main():
    board = Board()

    run = True 
    while run: 
        for event in pygame.event.get():
            match event.type: 
                case pygame.QUIT:
                    run = False 
                    break
                case pygame.MOUSEBUTTONDOWN:
                    board.make_move(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        win.fill((0, 0, 0))

        board.draw()
        board.check_for_winner()

        pygame.display.flip()
    
    pygame.quit()