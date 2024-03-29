import pygame
import random
from constants import *

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Christmas Trees")


# Function to draw a single Christmas tree
def draw_tree(x, y):
    pygame.draw.polygon(screen, GREEN, [(x, y), (x - 50, y + 100), (x + 50, y + 100)])
    pygame.draw.polygon(screen, GREEN, [(x, y + 50), (x - 75, y + 150), (x + 75, y + 150)])
    pygame.draw.polygon(screen, GREEN, [(x, y + 100), (x - 100, y + 200), (x + 100, y + 200)])
    pygame.draw.rect(screen, BROWN, (x - 12, y + 200, 24, 40))


# Function to draw a star on top of the tree
def draw_star(x, y):
    pygame.draw.polygon(screen, YELLOW,
                        [(x, y - 30), (x + 5, y - 10), (x + 20, y - 7), (x + 7, y), (x + 12, y + 15), (x, y + 7),
                         (x - 12, y + 15), (x - 7, y), (x - 20, y - 7), (x - 5, y - 10)])


# Function to generate twinkling stars
def generate_stars(num_stars):
    stars = []
    for _ in range(num_stars):
        x = random.randint(0, WIDTH)
        y = random.randint(0, STARS_MAX_HEIGHT)
        brightness = random.randint(100, 255)
        stars.append([x, y, brightness])
    return stars


# Function to draw twinkling stars
def draw_stars(stars):
    for star in stars:
        x, y, brightness = star
        pygame.draw.circle(screen, (brightness, brightness, brightness), (x, y), 2)


# Function to draw fixed trees with stars
def draw_fixed_trees_with_stars():
    tree_positions = [(150, 350), (275, 375), (400, 400), (525, 375), (650, 350)]
    for position in tree_positions:
        draw_tree(position[0], position[1])
        draw_star(position[0], position[1])


# Function to write "Merry Christmas" on the screen
def write_christmas_wish():
    font = pygame.font.Font(None, 72)
    text = font.render("Merry Christmas", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, 150))
    screen.blit(text, text_rect)


# Main loop
def main():
    running = True
    clock = pygame.time.Clock()
    twinkling_stars = generate_stars(100)

    while running:

        # if even is quit, break loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with black color
        screen.fill((0, 0, 0))

        # Draw twinkling stars
        draw_stars(twinkling_stars)

        # Draw the fixed trees with stars
        draw_fixed_trees_with_stars()

        # write merry christmas
        write_christmas_wish()

        # Update the display
        pygame.display.flip()

        # Add twinkling effect by randomly adjusting star brightness
        for star in twinkling_stars:
            star[2] = random.randint(100, 255)

        # Control frame rate
        clock.tick(30)

    pygame.quit()  # Quit Pygame properly


if __name__ == "__main__":
    main()
