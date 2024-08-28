import pygame 
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True 

    clock = pygame.time.Clock()
    fps = 60
    dt = 0
    updatabele = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatabele, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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
        pygame.display.flip()






if __name__ == "__main__":
    main()