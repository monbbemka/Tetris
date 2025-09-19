from constants import WIDTH, HEIGHT, GRID_SIZE, BEIGE
import pygame
from tetris import Tetris

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tetris')
    # Create a clock object
    clock = pygame.time.Clock()
    # Create a Tetris object
    game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)

    fall_time = 0
    fall_speed = 400  

    while True: 
        screen.fill(BEIGE)
        for event in pygame.event.get():
            # Check for the QUIT event
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # Move piece left
                if event.key == pygame.K_LEFT:
                    if game.valid_move(game.current_piece, -1, 0, 0):
                        game.current_piece.x -= 1 
                # Move piece right
                if event.key == pygame.K_RIGHT:
                    if game.valid_move(game.current_piece, 1, 0, 0):
                        game.current_piece.x += 1
                # Move piece down
                if event.key == pygame.K_DOWN:
                    if game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1 
                # Rotate piece
                if event.key == pygame.K_UP:
                    if game.valid_move(game.current_piece, 0, 0, 1):
                        game.current_piece.rotation += 1 
                if event.key == pygame.K_SPACE:
                    while game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1 #Move the piece down until it hits the bottom
                    game.place_piece(game.current_piece) # Place the piece

        # Get the number of milliseconds since the last frame
        delta_time = clock.tick(60)
        # Add the delta time to the fall time
        fall_time += delta_time 
        if fall_time >= fall_speed:
            # Move the piece down
            game.update_piece()
            # Reset the fall time
            fall_time = 0

        # Draw the score on the screen
        game.draw_score(screen, game.score, 10, 10)

        # Draw the grid and the current piece
        game.draw(screen)

        if game.game_over:
            # Draw the "Game Over" message
            game.draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)
            
            game.draw_rematch(screen, WIDTH // 2 - 170, HEIGHT // 2 +20)
            # Check for the KEYDOWN event
            if event.type == pygame.KEYDOWN:
                # Create a new Tetris object
                game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
        # Update the display
        pygame.display.flip()
        

main()