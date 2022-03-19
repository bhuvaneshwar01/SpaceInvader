# Import libraries
import pygame
import random

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

# Background Image
BackGroundImg = pygame.image.load("bg.jpg")

# Enemy
EnemyLogo = pygame.image.load("ghost.png")
EnemyX = random.randint(0,800)
EnemyY = random.randint(50,150)
EnemyX_change = 0.3
EnemyY_change = 40


def player(x, y):
    screen.blit(PlayerLogo, (x, y))


def enemy(x, y):
    screen.blit(EnemyLogo, (EnemyX, EnemyY))


# Game loop
running = True
while running:
    # Background colors
    screen.fill((0, 0, 0))

    # fill background image
    screen.blit(BackGroundImg,(0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        # The keydown event is triggered first when user presses a key. The keyup event is triggered last when user releases a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change = -1
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0

    PlayerX += PlayerX_change
    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    EnemyX += EnemyX_change
    if EnemyX <= 0:
        EnemyX_change = 0.3
        EnemyY += EnemyY_change

    elif EnemyX >= 736:
        EnemyX_change = -0.3
        EnemyY += EnemyY_change

    player(PlayerX,PlayerY)
    enemy(EnemyX, EnemyY)
    pygame.display.update()