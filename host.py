from socket import AF_INET, SOCK_STREAM, socket

try:
    HOST: str = input("$ Host IP: ").strip()
    PORT: int = int(input("$ Server port (5050 if unsure): ").strip())
except TypeError: 
    print("$ Invalid type")
    exit()

try: 
    server: socket = socket(AF_INET, SOCK_STREAM)
    server.bind((HOST, PORT))
    print(f"$ Server hosted at {HOST}:{PORT}")
except: 
    print(f"$ Server unable to be hosted at {HOST}:{PORT}")

import pygame
from board import Board
from settings import win

def main():    
    board: Board = Board()

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

main()