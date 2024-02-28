import pygame
from settings import win, WIDTH, HEIGHT, FONT_SIZE

big_font = pygame.font.SysFont("arial", FONT_SIZE)
small_font = pygame.font.SysFont("arial", 50)

class ResetButton: 
        def __init__(self) -> None:
            self.res = (205, 60)
            self.pos = ((WIDTH-self.res[0])/2, (HEIGHT-self.res[1])/2)

        def draw(self): 
            button = pygame.Rect(self.pos[0], self.pos[1], self.res[0], self.res[1])
            text = small_font.render("Play again!", False, (0, 0, 0))
            pygame.draw.rect(win, (200, 200, 200), button)
            win.blit(text, self.pos)
        
        def is_clicked(self) -> bool: 
            mouse_pos = pygame.mouse.get_pos()
            return True if ((self.pos[0] <= mouse_pos[0] <= self.pos[0] + self.res[0]) and (self.pos[1] <= mouse_pos[1] <= self.pos[1] + self.res[1])) else False

class Board: 
    def __init__(self) -> None:
        self.board: list = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.sound = pygame.mixer.Sound("./assets/sounds/pop (1).mp3")

        self.reset_button = ResetButton()

        self.x_enum: int = 1
        self.o_enum: int = 2

        self.turn: int = self.x_enum
        self.winner = 0
        self.winner_printed: bool = False

        self.x_sprite = pygame.image.load("./assets/sprites/x.png")
        self.o_sprite = pygame.image.load("./assets/sprites/o.png")

        self.is_draw = 0
    
    def reset(self): 
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.turn = self.x_enum if self.turn == self.x_enum else self.o_enum
        self.winner = 0
        self.winner_printed: bool = False

        self.sound.play()

    def draw(self) -> None: 
        row_height: int = (WIDTH/3).__floor__()
        col_width: int = (WIDTH/3).__floor__()

        pygame.draw.line(win, (255, 0, 255), (col_width, 0), (col_width, HEIGHT))
        pygame.draw.line(win, (255, 0, 255), (col_width * 2, 0), (col_width * 2, HEIGHT))

        pygame.draw.line(win, (255, 0, 255), (0, row_height), (WIDTH, row_height))
        pygame.draw.line(win, (255, 0, 255), (0, row_height * 2), (WIDTH, row_height * 2))

        self.is_draw = 0
        for r in range(3):
            for c in range(3): 
                piece = self.board[r][c]
                if not piece == 0: 
                    self.is_draw += 1
                if piece == self.x_enum: 
                    win.blit(self.x_sprite, (c * col_width, r * row_height))
                elif piece == self.o_enum: 
                    win.blit(self.o_sprite, (c * col_width, r * row_height))
        
        text = ""
        if self.winner:
            if self.winner == self.o_enum: 
                text = "O won!"
            else: 
                text = "X won!"
            text_surface = big_font.render(text, False, (255, 0, 255))
            pygame.draw.rect(win, (255, 255, 255), pygame.Rect(0, HEIGHT-FONT_SIZE, 300, FONT_SIZE))
            win.blit(text_surface, (0, HEIGHT-FONT_SIZE))
            self.reset_button.draw()
            
        elif self.is_draw == 9:
            text = "Draw!" 
            text_surface = big_font.render(text, False, (255, 0, 255))
            pygame.draw.rect(win, (255, 255, 255), pygame.Rect(0, HEIGHT-FONT_SIZE, 300, FONT_SIZE))
            win.blit(text_surface, (0, HEIGHT-FONT_SIZE))
            self.reset_button.draw()

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

                self.sound.play()

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
                    if (board.winner or board.is_draw == 9) and board.reset_button.is_clicked(): 
                        board.reset()

        win.fill((0, 0, 0))

        board.draw()
        board.check_for_winner()

        pygame.display.flip()
    
    pygame.quit()

main()