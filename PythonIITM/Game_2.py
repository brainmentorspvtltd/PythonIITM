import pygame
import random
from pygame.locals import *

pygame.init()

width = 800
height = 500

red = (255,0,0)

screen = pygame.display.set_mode((width, height))

bg_Image = pygame.image.load("assets/images/background.png")

aim_Image = pygame.image.load("assets/images/aim_pointer.png")

gunShot = pygame.mixer.Sound('assets/sounds/shot_sound.wav')

bgSound = pygame.mixer.Sound('assets/sounds/background.wav')
bgSound.play(-1)

gunImage = pygame.image.load("assets/images/gun_1.png")

zombie_1 = pygame.image.load('assets/images/zombie_1.gif')
zombie_2 = pygame.image.load('assets/images/zombie_2.png')
zombie_3 = pygame.image.load('assets/images/zombie_3.png')

zombie_list = [zombie_1, zombie_2, zombie_3]

def timer(seconds):
    font = pygame.font.SysFont(None, 40)
    text = font.render('Time Left : '+str(seconds), True, red)
    screen.blit(text, (width - 200,0))

def score(counter):
    font = pygame.font.SysFont(None, 40)
    text = font.render('Score : '+str(counter), True, red)
    screen.blit(text, (0,0))

def gameOver():
    font = pygame.font.SysFont(None, 80)
    text = font.render('Game Over', True, red)
    while True:
        screen.blit(text, (width/2 - 140,height/2 - 40))
        pygame.display.update()

def game():

    zombie_x = random.randint(0, width - 150)
    zombie_y = random.randint(0, height - 200)
    zombieImage = random.choice(zombie_list)
    counter = 0

    seconds = 10
    pygame.time.set_timer(USEREVENT + 1, 1000)

    while True:

        posX, posY = pygame.mouse.get_pos()

        zombie_rect = pygame.Rect(zombie_x, zombie_y, zombieImage.get_width(), zombieImage.get_height())
        aim_rect = pygame.Rect(posX, posY, aim_Image.get_width(), aim_Image.get_height())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == USEREVENT + 1:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                gunShot.play()
                if zombie_rect.colliderect(aim_rect):
                    print("Collision")
                    counter += 1
                    zombieImage = random.choice(zombie_list)
                    zombie_x = random.randint(0, width - 150)
                    zombie_y = random.randint(0, height - 200)

        if seconds == -1:
            seconds = 0
            gameOver()
        
        #print(posX, posY)

        screen.blit(bg_Image, (0,0))
        screen.blit(zombieImage, (zombie_x, zombie_y))
        screen.blit(aim_Image, (posX - 50, posY - 50))
        screen.blit(gunImage, (posX, height - 300))

        score(counter)
        timer(seconds)
        
        pygame.display.update()


game()
