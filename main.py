import pygame, sys, time
pygame.init()

width = 900
height = 500
screen = pygame.display.set_mode((width, height))

snake_width, snake_height = 50, 50

white = (255,255,255)
green = (0,255,0)
snakegreen = (100,255,100)
red = (255,0,0)
black = (0,0,0)

locations = []
pos = [0,0]
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
            if event.key == pygame.K_SPACE:
                length += 1
    x = pos[0]
    y = pos[1]
    pos = [
        x+snake_width if direction == 90 else x-snake_width if direction == -90 else x, 
        y+snake_height if direction == 180 else y-snake_width if direction == 0 else y
    ]
    locations.append(pygame.Rect((pos[0], pos[1]), (snake_width,snake_height)))
    if len(locations) > length:
        del locations[0]
    screen.fill(black)
    for location in range(len(locations)-1):
        pygame.draw.rect(screen, snakegreen, locations[location])
    pygame.draw.rect(screen, green, locations[-1])
    pygame.display.flip()
    time.sleep(0.5)

pygame.quit()
