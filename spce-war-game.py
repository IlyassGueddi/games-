import pygame
import random

# Pygame setup stuff
pygame.init()
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("My Game")
icon = pygame.image.load('mario.png')
pygame.display.set_icon(icon)

#background
back = pygame.image.load('background.png')

# player
playerImg = pygame.image.load('attack.png')
# Where the player will start at the beginning of the game
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(X, Y):
    screen.blit(playerImg, (X, Y))

# enemy
enemyImg = pygame.image.load('enemy1.png')
# Where the enemy will start at the beginning of the game
enemyX = random.randint(0, 745)
enemyY = random.randint(50, 350)
enemyX_change = 0.3
enemyY_change = 0.3


def enemy(X, Y):
    screen.blit(enemyImg, (X, Y))



# GAME LOOP
running = True
while running:

    #the color of the background
    screen.fill((10, 10, 30)) 
    # background
    screen.blit(back, (0,0))

    # making the game turn of if we press X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        # Making the player controled by the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                playerX_change = -1
            if event.key == pygame.K_RIGHT :
                playerX_change = 1
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    

    # player
    playerY += playerY_change
    playerX += playerX_change
    enemyX += enemyX_change
    enemyY += enemyY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 745 :
        playerX = 745


    # enemy
    if enemyX <= 0:
        enemyX_change = 0.3
    elif enemyX >= 745 :
        enemyX_change = -0.3

    if enemyY <= 0:
        enemyY_change = 0.1
    elif enemyY >= 380:
        enemyY_change = -0.1


    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()