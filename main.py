import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
# Initiate the pygame module




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
    clock = pygame.time.Clock()
    dt = 0


    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
    
        dt = clock.tick(60) / 1000
        player.update(dt)
    # End of game cycle
# End of main


if __name__ == "__main__":
    main()
