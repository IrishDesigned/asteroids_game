import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player

def game_loop(screen, clock, updatable, drawable):
    run_game_loop = True
    dt = 0
    while run_game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill((0,0,0))
        dt = clock.tick(60) / 1000
        # print("dt:", dt) # debug
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"""
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
""")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()   
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))

    # print("updatable size:", len(updatable)) # debug
    # print("drawable size:", len(drawable)) # debug
   
    game_loop(screen, clock, updatable, drawable)

if __name__ == "__main__":
    main()
