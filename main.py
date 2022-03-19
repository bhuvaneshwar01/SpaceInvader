import pygame

# Initialised pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))  # 800 -> height 600->width

# Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background colors
    screen.fill((150,0,0))
    pygame.display.update()