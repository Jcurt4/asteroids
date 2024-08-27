import pygame 
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True 

    clock = pygame.time.Clock()
    fps = 60
    dt = 0

    while running: 
        dt = (clock.tick(fps)) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()






if __name__ == "__main__":
    main()