import pygame, sys, time, random; pygame.init(); width, height, screen, snake_width, snake_height, white, green, snakegreen, red, black, locations, applelocations, pos, length, appleamount, direction, running = 900, 500, pygame.display.set_mode((900, 500)), 50, 50, (255,255,255), (0,255,0), (100,255,100), (255,0,0), (0,0,0), [], [], [0,0], 1, 1, 90, True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); running = False; sys.exit()
        if event.type == pygame.KEYDOWN: direction = (90 if event.key == pygame.K_RIGHT else -90 if event.key == pygame.K_LEFT else 180 if event.key == pygame.K_DOWN else 0 if event.key == pygame.K_UP else direction)      
    if appleamount != len(applelocations): newlocation = pygame.Rect((random.choice(range(0, width, snake_width)), random.choice(range(0, height, snake_height))), (snake_width, snake_height)); applelocations = applelocations + [newlocation] if newlocation not in applelocations and newlocation not in locations else applelocations
    x, y, = pos[0], pos[1]; pos = [x+snake_width if direction == 90 else x-snake_width if direction == -90 else x, y+snake_height if direction == 180 else y-snake_width if direction == 0 else y]; locations.append(pygame.Rect((pos[0], pos[1]), (snake_width,snake_height))); pygame.display.flip(); time.sleep(0.5); screen.fill(black); pygame.draw.rect(screen, green, locations[-1])
    if len(locations) > length: del locations[0]
    if locations[-1] in applelocations: del applelocations[applelocations.index(locations[-1])]; length += 1
    for location in range(len(locations)-1): pygame.draw.rect(screen, snakegreen, locations[location])
    for apple in applelocations: pygame.draw.rect(screen, red, apple)