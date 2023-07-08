import random
import pygame
import math
from random import uniform
from starfield_simulation.constants import (
    Z_DISTANCE,
    WIDTH,
    HEIGHT,
    COLORS,
    CENTER
)

class Star:
    """
    class for creating stars
    """
    def __init__(self, screen):
        self.screen = screen
        self.position_3d = self.get_3d_position()
        self.screen_pos = vec2(0, 0)
        self.velocity = uniform(0.05, 0.25)
        self.color = random.choice(COLORS)
        self.size = 10

    def update(self):
        self.position_3d.z -= self.velocity
        self.position_3d = self.get_3d_position() if self.position_3d.z < 1 else self.position_3d
        self.screen_pos = vec2(self.position_3d.x, self.position_3d.y) / self.position_3d.z + center
        self.size = (Z_DISTANCE - self.position_3d.z) / (0.2 * self.position_3d.z)

        # rotate xy
        self.position_3d.xy = self.position_3d.xy.rotate(0.2)

        # update position on mouse movement
        mouse_pos = CENTER - vec2(pygame.mouse.get_pos())
        self.screen_pos += mouse_pos

    def get_3d_position(self):
        scale_pos = 35
        angle = random.uniform(0, 2 * math.pi)
        radius = random.randrange(HEIGHT // scale_pos, WIDTH) * scale_pos
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        return vec3(x, y, Z_DISTANCE)

    def show(self):
        s = self.size
        if (-s < self.screen_pos.x < WIDTH + s) and (-s < self.screen_pos.y < HEIGHT + s):
            pygame.draw.circle(self.screen, self.color,
                               (int(self.screen_pos.x),
                                int(self.screen_pos.y)),
                               self.size)


# defining vectors
vec2, vec3 = pygame.math.Vector2, pygame.math.Vector3

# Initialize Pygame
pygame.init()

# Set the width and height of the canvas
RES = WIDTH,HEIGHT
center = vec2(WIDTH//2, HEIGHT//2)
app_screen = pygame.display.set_mode(RES)

# Creating a list to store the stars
stars = [Star(app_screen) for _ in range(300)]

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and render the stars
    for star in stars:
        star.update()
        star.show()
    clock.tick(60)
    pygame.display.update()
    app_screen.fill([0, 0, 0])

# Quit Pygame
pygame.quit()
