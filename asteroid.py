from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width = 2)


    def update(self, dt):
        velocity = self.velocity
        self.position += velocity * dt
    
    def rotate(self, angle):
        self.rotation += angle
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        self.kill()
        rand_angle = random.uniform(20,50)
        smaller_ast_velocity1 = self.velocity.rotate(-rand_angle)
        smaller_ast_velocity2 = self.velocity.rotate(rand_angle)
       
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        ast1 = Asteroid(self.position[0], self.position[1], new_radius)
        ast2 = Asteroid(self.position[0], self.position[1], new_radius)

        ast1.velocity = smaller_ast_velocity1 * 1.2
        ast2.velocity = smaller_ast_velocity2 * 1.2


