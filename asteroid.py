import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

# Base class for asteroids
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = WHITE
        width = LINE_WIDTH
        center = [self.position.x, self.position.y]
        pygame.draw.circle(screen, color, center, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        # 1. this asteroid is always destroyed
        self.kill()

        # 2. if it's already small, don't spawn anything
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # 3. log the split event
        log_event("asteroid_split")

        # 4. pick a random angle between 20 and 50 degrees
        split_angle = random.uniform(20, 50)

        # 5. create two new velocity vectors, rotated left and right
        vel_a = self.velocity.rotate(split_angle)
        vel_b = self.velocity.rotate(-split_angle)

        # 6. compute the new (smaller) radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # 7. create two new asteroids at the same position
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)

        # 8. make them move faster in their new directions
        asteroid_a.velocity = vel_a * 1.2
        asteroid_b.velocity = vel_b * 1.2