import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT, FONT_SIZE
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def show_score(x, y):

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

def main():
    # print to the terminal basic information.

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # intitialize a pygame with a screen of desired screen width and height. Set the caption to be the title of the game.

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids by Jon")
    # initialize a time clock. Set delta to zero.

    clock = pygame.time.Clock()
    dt = 0
    # initialize a score variable set to zero.

    score = Score()

    font = pygame.font.SysFont(FONT, FONT_SIZE)
    # Create groups of different categories based on functionality

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Create containers for all the categories a certain sprite falls in.

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    # Create the player and asteroid field.

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()
    # MAIN GAME CODE

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        for sprite in drawable:
            sprite.draw(screen)
        

        screen.blit(score_text, (15, 10))

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
