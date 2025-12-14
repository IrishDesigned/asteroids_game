import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state

def game_loop(screen, clock):
    run_game_loop = True
    dt = 0
    while run_game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = clock.tick(60)/1000
        # print(dt) # debug

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"""
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
""")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop(screen, clock)
    

if __name__ == "__main__":
    main()
