import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state

def game_loop():
    run_game_loop = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    while run_game_loop:
        log_state()
        screen.fill((0,0,0))
        pygame.display.flip()

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"""Screen width: {SCREEN_WIDTH}
    Screen height: {SCREEN_HEIGHT}""")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop()
    

if __name__ == "__main__":
    main()
