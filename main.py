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
PlayerX = 370
PlayerY = 480
PlayerX_change = 0

def player(x,y):
    screen.blit(PlayerLogo,(x,y))

# Game loop
running = True
while running:
    # Background colors
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # The keydown event is triggered first when user presses a key. The keyup event is triggered last when user releases a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0

    PlayerX += PlayerX_change
    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    player(PlayerX,PlayerY)
    pygame.display.update()