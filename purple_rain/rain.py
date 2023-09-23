import random
import pygame
from purple_rain.constants import (
    RAIN_COLOR,
    BACKGROUND,
    SCREEN_SIZE,
    NUM_DROPS
)

class Raindrop:
    def __init__(self, window):
        self.x = random.randint(5, 695)
        self.y = random.randint(-1500, 0)
        self.zaxis = random.randint(0, 30)
        self.width = random.randint(0, 3)
        self.color = RAIN_COLOR
        self.window = window
        self.length = map_rain(self.zaxis, 0, 20, 0, 30)
        self.yspeed = map_rain(self.zaxis, 0, 0.05, 0, 30)

    def fall(self):
        self.y += self.yspeed
        self.yspeed += (0.025 * self.zaxis) / 100
        if self.y >= 700:
            self.y = random.randint(-200, -100)
            self.yspeed = random.uniform(2.5, 0.5)

    def display(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.length))


def screen(window):
    window.fill(BACKGROUND)


def map_rain(x, x1, x2, y1, y2):
    return y1 + x * (y2 - y1) / (x2 - x1)


def main():
    pygame.init()

    # initializing window
    window = pygame.display.set_mode(SCREEN_SIZE)


    rainfall = []


    for i in range(0, NUM_DROPS):
        drop = Raindrop(window)
        rainfall.append(drop)

    break_loop = False
    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                break_loop = True
                break

        if break_loop:
            break

        for i in rainfall:
            i.display()

        pygame.display.flip()

        for i in rainfall:
            i.fall()

        pygame.display.flip()
        screen(window)


main()
