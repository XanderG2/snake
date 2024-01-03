import pygame, sys
pygame.init()

width = 900
height = 500
screen = pygame.display.set_mode((width, height))

white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

locations = []
length = 1
direction = 90

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 90
            if event.key == pygame.K_LEFT:
                direction = -90
            if event.key == pygame.K_DOWN:
                direction = 180
            if event.key == pygame.K_UP:
                direction = 0
            print(direction)
    screen.fill(black)
    pygame.display.flip()

pygame.quit()
