import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True 

    clock = pygame.time.Clock()
    fps = 60
    dt = 0
    updatabele = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Player.containers = (updatabele, drawable)
    Asteroid.containers = (updatabele, drawable, asteroids)
    AsteroidField.containers = (updatabele)
    Shot.containers = (updatabele, drawable, shot)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    while running: 
        dt = (clock.tick(fps)) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        for update in updatabele:
            update.update(dt)   
        for draw in drawable:
            draw.draw(screen)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                running = False
        for s in shot:
            for asteroid in asteroids:
                if s.collides_with(asteroid):
                    asteroid.split()
                    s.kill()
        pygame.display.flip()






if __name__ == "__main__":
    main()