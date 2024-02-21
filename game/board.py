import pygame
from settings import win, WIDTH, HEIGHT

class Board: 
    def __init__(self) -> None:
        self.board: list = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.x_enum: int = 1
        self.o_enum: int = 2

        self.turn: int = self.x_enum
        self.winner = None
        self.winner_printed: bool = False

        self.x_sprite = pygame.image.load("sprites/x.png")
        self.o_sprite = pygame.image.load("sprites/o.png")
    
    def draw(self) -> None: 
        row_height: int = (WIDTH/3).__floor__()
        col_width: int = (WIDTH/3).__floor__()

        pygame.draw.line(win, (255, 0, 255), (col_width, 0), (col_width, HEIGHT))
        pygame.draw.line(win, (255, 0, 255), (col_width * 2, 0), (col_width * 2, HEIGHT))

        pygame.draw.line(win, (255, 0, 255), (0, row_height), (WIDTH, row_height))
        pygame.draw.line(win, (255, 0, 255), (0, row_height * 2), (WIDTH, row_height * 2))

        for r in range(3):
            for c in range(3): 
                piece = self.board[r][c]

                if piece == self.x_enum: 
                    win.blit(self.x_sprite, (c * col_width, r * row_height))
                elif piece == self.o_enum: 
                    win.blit(self.o_sprite, (c * col_width, r * row_height))


    def xy_to_rc(self, mouse_x: int, mouse_y: int) -> tuple: 
        row: int = 0
        col: int = 0

        r1 = (HEIGHT/3).__floor__()
        r2 = (2 * HEIGHT/3).__floor__()

        c1 = (WIDTH/3).__floor__()
        c2 = (2 * WIDTH/3).__floor__()

        if mouse_y < r1: 
            row = 0
        elif mouse_y < r2: 
            row = 1
        else:
            row = 2
        
        if mouse_x < c1: 
            col = 0
        elif mouse_x < c2: 
            col = 1
        else:
            col = 2
        
        return (row, col)

    def make_move(self, mouse_x: int, mouse_y: int) -> None: 
        if not self.winner:
            r, c = self.xy_to_rc(mouse_x, mouse_y)

            if not self.board[r][c]: 
                self.board[r][c] = self.turn
            
                if self.turn == self.x_enum:
                    self.turn = self.o_enum
                else:
                    self.turn = self.x_enum

    def check_for_winner(self) -> None:
        for r in range(3):
            if self.board[r][0] == self.board[r][1] == self.board[r][2] and self.board[r][0]:
                self.winner = self.board[r][0] 
        for c in range(3): 
            if self.board[0][c] == self.board[1][c] == self.board[2][c] and self.board[0][c]: 
                self.winner = self.board[0][c]
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[1][1]:
            self.winner = self.board[1][1]
        
        if not self.winner_printed:
            if self.winner == self.o_enum: 
                print("O won!")
                self.winner_printed = True
            elif self.winner == self.x_enum:
                print("X won!")
                self.winner_printed = True