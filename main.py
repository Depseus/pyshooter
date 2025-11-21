import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
# Initiate the pygame module




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    asteroids_field = AsteroidField()
    player = Player(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
    clock = pygame.time.Clock()
    dt = 0

    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
 
    while(True):
        # Get logstate
        log_state()

        # Check to see if the user wishes to exit out of the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        # update everything within the group
        updatable.update(dt)  

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # fill out the background
        screen.fill("black")
        #iterate over everything that is 'drawable' in the system
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000



    # End of game cycle
# End of main


if __name__ == "__main__":
    main()
