from constants import SHAPES, GRID_SIZE, DARK_PURPLE, BEIGE
import pygame
from tetronimo import Tetronimo
import random


class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0

    def new_piece(self):
        shape = random.choice(SHAPES)
        return Tetronimo(self.width // 2 ,0, shape)
    
    def valid_move(self, piece, x, y, rotation):
        # Check if piece can move to the position
        for i, row in enumerate(piece.shape[(piece.rotation + rotation) %len(piece.shape)]):
            for j, cell in enumerate(row):
                if cell == 'O':
                    new_y = piece.y + i + y
                    new_x = piece.x + j + x
                    # Spielfeldgrenzen prüfen!
                    if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
                        return False
                    if self.grid[new_y][new_x] != 0:
                        return False
        
        return True
    
    def clear_rows(self):
        # Clears full rows and return number of cleared rows
        cleared_rows = 0
        for i in range(self.height - 1, -1, -1 ):
            if all(cell != 0 for cell in self.grid[i]):
                cleared_rows+=1
                del self.grid[i]
                self.grid.insert(0, [0 for _ in range(self.width)])
        return cleared_rows

    def place_piece(self, piece):
        # Place a piece and calculate score
        for i, row in enumerate(piece.shape[piece.rotation %len(piece.shape)]):
            for j, cell in enumerate(row):
                if cell == 'O':
                    self.grid[piece.y + i][piece.x + j] = piece.color
        cleared_rows = self.clear_rows()
        self.score += cleared_rows * 100
        self.current_piece = self.new_piece()
        if not self.valid_move(self.current_piece, 0, 0, 0 ):
            self.game_over=True
        return cleared_rows
    
    def update_piece(self):
        # Move piece down by one
        if not self.game_over:
            if self.valid_move(self.current_piece, 0, 1, 0):
                self.current_piece.y += 1
            else:
                self.place_piece(self.current_piece)

    def draw(self, screen):
        # Draw grid and current piece
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

        if self.current_piece:
            for i, row in enumerate(self.current_piece.shape[(self.current_piece.rotation) %len(self.current_piece.shape)]):
                for j, cell in enumerate(row):
                    if cell == 'O':
                        pygame.draw.rect(screen, self.current_piece.color, ((self.current_piece.x + j) * GRID_SIZE, (self.current_piece.y + i) * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

    def draw_score(self, screen, score, x, y):
        # Draw score on screen
        font = pygame.font.Font(None,35)
        text = font.render(f'Your score is {score}', True, DARK_PURPLE)

        screen.blit(text, (x, y))

    def draw_game_over(self, screen, x, y):
        font = pygame.font.Font(None, 50)
        text = font.render("Game Over :(", True, DARK_PURPLE)
        screen.blit(text, (x, y))

    def draw_rematch(self, screen, x, y):
        font = pygame.font.Font(None, 40)
        text = font.render("Press any key to continue", True, DARK_PURPLE)
        screen.blit(text, (x, y))



    




    




