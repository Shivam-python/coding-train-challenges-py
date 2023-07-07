import pygame
from random import randint, uniform


class Star:
    def __init__(self):
        self.x = uniform(-width, width)
        self.y = uniform(-height, height)
        self.z = uniform(0, width)
        self.pz = self.z

    def update(self):
        self.z -= speed
        if self.z < 1:
            self.z = width
            self.x = uniform(-width, width)
            self.y = uniform(-height, height)
            self.pz = self.z

    def scale_point(self, value, old_min, old_max, new_min, new_max):
        old_range = (old_max - old_min)
        new_range = (new_max - new_min)
        new_value = (((value - old_min) * new_range) / old_range) + new_min
        return new_value

    def show(self):
        sx = self.scale_point(self.x / self.z, 0, 1, 0, width)
        sy = self.scale_point(self.y / self.z, 0, 1, 0, height)

        r = self.scale_point(self.z, 0, width, 10, 0)

        px = self.scale_point(self.x / self.pz, 0, 1, 0, width)
        py = self.scale_point(self.y / self.pz, 0, 1, 0, height)

        self.pz = self.z

        pygame.draw.line(screen, (255, 255, 255), (px, py), (sx, sy), int(r))


# Initialize Pygame
pygame.init()

# Set the width and height of the canvas
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set the initial speed of the stars
speed = 1

# Creating a list to store the stars
stars = [Star() for _ in range(300)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and render the stars
    for star in stars:
        star.update()
        star.show()

    pygame.display.update()
    screen.fill([0, 0, 0])

# Quit Pygame
pygame.quit()
