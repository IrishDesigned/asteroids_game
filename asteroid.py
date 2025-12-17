import pygame
from circleshape import CircleShape
from constants import *

# Base class for asteroids
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen ):
        color = WHITE
        width = LINE_WIDTH
        center = [self.position.x, self.position.y]
        pygame.draw.circle(screen, color, center, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt 