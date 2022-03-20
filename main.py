# Import libraries
import math
import random

import pygame
from pygame import mixer

# Initialised pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))  # 800 -> width 600 -> height

# Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

# Player (PlayerX and Player are the position)
PlayerLogo = pygame.image.load("arcade-game.png")
PlayerX = 370
PlayerY = 480
PlayerX_change = 0

# Background Image
BackGroundImg = pygame.image.load("bg.jpg")

# Background music
mixer.music.load("background.wav")
mixer.music.play(-1)

# Enemy
EnemyLogo = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
number_of_enemies = 6

for i in range(number_of_enemies):
    EnemyLogo.append(pygame.image.load("ghost.png"))
    EnemyX.append(random.randint(0,736))
    EnemyY.append(random.randint(50,150))
    EnemyX_change.append(0.3)
    EnemyY_change.append(40)

# Bullet
BulletLogo = pygame.image.load("bullet.png")
BulletX = 0
BulletY = 480
BulletX_change = 0
BulletY_change = 1
Bullet_state = "ready"

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(PlayerLogo, (x, y))

def enemy(EnemyX, EnemyY,i):
    screen.blit(EnemyLogo[i], (EnemyX, EnemyY))

def fire_bullet(x,y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletLogo,(x+16,y+10))

def isCollison(EnemyX,EnemyY,BulletX,BulletY):
    distance = math.sqrt(math.pow((EnemyX-BulletX),2) + math.pow((EnemyY-BulletY),2))
    if distance <= 27:
        return True
    else:
        return False

def show_score(x,y):
    s = font.render("Score : " + str(score),True,(0,0,0),(255,255,255))
    screen.blit(s,(x,y))

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
            if event.key == pygame.K_SPACE:
                if Bullet_state == "ready":
                    Bullet_sound = mixer.Sound("laser.wav")
                    Bullet_sound.play()
                    BulletX = PlayerX
                    fire_bullet(BulletX,BulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0

    # Player movement
    PlayerX += PlayerX_change
    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    if BulletY <= 0:
        BulletY = 480
        Bullet_state = "ready"

    # Bullet Movement
    if Bullet_state == "fire":
        BulletY -= BulletY_change
        fire_bullet(BulletX,BulletY)

    # Enemy movement
    for i in range(number_of_enemies):

        # Game Over
        if EnemyY[i] > 440:
            for j in range(number_of_enemies):
                EnemyY[j] = 2000
            game_over_text()
            break

        EnemyX[i] += EnemyX_change[i]
        if EnemyX[i] <= 0:
            EnemyX_change[i] = 0.3
            EnemyY[i] += EnemyY_change[i]

        elif EnemyX[i] >= 736:
            EnemyX_change[i] = -0.3
            EnemyY[i] += EnemyY_change[i]

        # Collision
        collision = isCollison(EnemyX[i], EnemyY[i], BulletX, BulletY)
        if collision:
            Explosion_sound = mixer.Sound("explosion.wav")
            Explosion_sound.play()
            BulletY = 480
            Bullet_state = "ready"
            score += 1
            EnemyX[i] = random.randint(0, 735)
            EnemyY[i] = random.randint(50, 150)
        enemy(EnemyX[i], EnemyY[i],i)
    player(PlayerX,PlayerY)
    show_score(textX,textY)
    pygame.display.update()