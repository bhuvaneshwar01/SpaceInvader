import pygame

# Initialised pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))  # 800 -> width 600 -> height

# Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Player (PlayerX and Player are the position)
PlayerLogo = pygame.image.load("arcade-game.png")
PlayerX = 375
PlayerY = 430

def player():
    screen.blit(PlayerLogo,(PlayerX,PlayerY))

# Game loop
running = True
while running:
    # Background colors
    screen.fill((150, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
