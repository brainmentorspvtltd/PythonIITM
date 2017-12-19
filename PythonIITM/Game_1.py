import pygame

# Initialize Pygame
pygame.init()

red = (255,0,0)
white = (255,255,255)

screen = pygame.display.set_mode((800,500))

x = 0
y = 0

move_x = 0

while True:
##    event = pygame.event.get()
##    print(event)

    for event in pygame.event.get():
##        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 1

    screen.fill(red)

    pygame.draw.rect(screen, white, [x,y, 50,50])

    x += move_x

    pygame.display.update()
