import sys, os
import pygame
import random
from pygame.locals import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)

# Game Variables
moveSpeed = 5


GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")

# Main Game Starts here
pygame.init()

#Initialize frame manager
clock = pygame.time.Clock()

#Set Frame Rate
clock.tick(60)

#Set caption bar
pygame.display.set_caption("Crazy Driver")

# Load images
IMG_ROAD = pygame.image.load(os.path.join(IMAGE_FOLDER, "Road.png"))
IMG_PLAYER = pygame.image.load(os.path.join(IMAGE_FOLDER, "Player.png"))
IMG_ENEMY = pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy.png"))

# Initialize Game screen
screen = pygame.display.set_mode(IMG_ROAD.get_size())

# Create game objects
# Calculate Initial player position
h = IMG_ROAD.get_width() // 2
v = IMG_ROAD.get_height() - (IMG_PLAYER.get_height() // 2)

# Create player sprite
player = pygame.sprite.Sprite()
player.image = IMG_PLAYER
player.surf = pygame.Surface(IMG_PLAYER.get_size())
player.rect = player.surf.get_rect(center = (h,v))

#Enemy
# Calculate intial enemy position
hl = IMG_ENEMY.get_width()//2
hr = IMG_ROAD.get_width() - (IMG_ENEMY.get_width() // 2)
h = random.randrange(hl, hr)
v = 0

# Create enemy sprite
enemy = pygame.sprite.Sprite()
enemy.image = IMG_ENEMY
enemy.surf = pygame.Surface(IMG_ENEMY.get_size())
enemy.rect = enemy.surf.get_rect(center = (h,v))

while True:
    # Place background
    screen.blit(IMG_ROAD, (0,0))

    #Place player on screen
    screen.blit(player.image, player.rect)

    #Place enemy on screen
    screen.blit(enemy.image, enemy.rect)
    enemy.rect.move_ip(0, moveSpeed)

    # Check for events
    for event in pygame.event.get():
        # Did the player quit?
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()