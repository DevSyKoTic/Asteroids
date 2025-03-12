import pygame
from circleshape import CircleShape
SHOT_RADIUS = 5
class Shot(CircleShape):

    def __init__(self, position, velocity):
        x, y = position
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, SHOT_RADIUS)