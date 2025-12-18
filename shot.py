import pygame
from circleshape import CircleShape
from constants import *

# Base class for player fired shots
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen ):
        color = WHITE
        width = LINE_WIDTH
        center = [self.position.x, self.position.y]
        pygame.draw.circle(screen, color, center, SHOT_RADIUS, width)

    def update(self, dt):
        self.position += self.velocity * dt 
        #print(f"Shot position: {self.position.x}, {self.position.y}")