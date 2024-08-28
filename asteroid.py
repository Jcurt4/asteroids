import pygame
from circleshape import CircleShape
import random  
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            random_angle = random.uniform(20, 50)
            child_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            child_asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
            child_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            child_asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2 
            self.kill()


