import pygame, sys, time, random
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('comicsans', 45) # font used later in the code. (font, size), change font or 
                                               #size and it will change the size or font of the death screen text.
width = 900 # ensure this is divisible by snake_width
height = 500 # ensure this is divisible by snake_height
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake by Xander") # set the title to snake by xander

snake_width, snake_height = 50, 50 # these are basically each grid cell's width and height

white = (255,255,255) # the colour used by the death screen text
green = (0,255,0) # the colour used by the snake head
snakegreen = (100,255,100) # the colour used by every snake section apart from the head
red = (255,0,0) # the colour used by apples
black = (0,0,0) # the background colour

def reset():
    global locations, applelocations, pos, length, appleamount, direction, snakeDead # terrible code ik but i cant be bothered to change it so ygwyg probably some bad performance
    locations = [] # the locations of the snake sections, locations[0] being the end, locations[-1] being the start
    applelocations = []
    pos = [0,0] # the position of the snake head
    length = 1 # length of snakes
    appleamount = 1 # amount of apples to be on the board at once, make it less than width//snake_width*height//snake_height
    direction = 90 # 90 is right, 180 is down, -90 is left, 0 is up
    snakeDead = False

reset()

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
            #if event.key == pygame.K_SPACE: #debug
            #    length += 1
            if (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER) and snakeDead: # if pressing main or keypad enter key, 
                reset()                                                                          # reset back to normal
            if event.key == pygame.K_x:
                running = False
                sys.exit()
    if not snakeDead:
        if appleamount != len(applelocations): # spawn a new apple if there are not enough to meet the amount on line 24
            newlocation = pygame.Rect(
                    (random.choice(
                        range(0, width, snake_width) # choose out of a list between 0 and the screen width, in increments of snake_width (grid width)
                    ), 
                    random.choice(
                        range(0, height, snake_height) # choose out of a list between 0 and the screen height, in increments of snake_height (grid height)
                    )), 
                    (snake_width, 
                    snake_height))
            if newlocation not in applelocations and newlocation not in locations: # if the apple spawns, it will not spawn on another apple and will not spawn on the snake
                applelocations.append(newlocation)                               #!# note: this will make it crash when there are not enough spaces for the apple to spawn in,
        x = pos[0] # pos is defined on line 22                                     # I need to fix this, but probably never will
        y = pos[1] # and line 67
        pos = [
            x+snake_width if direction == 90 else x-snake_width if direction == -90 else x, # increase or decrease x if direction is right or left, respectively, or don't if it isn't
            y+snake_height if direction == 180 else y-snake_width if direction == 0 else y  # increase or decrease y if direction is down or up, respectively, or don't if it isn't
        ]
        locations.append(pygame.Rect((pos[0], pos[1]), (snake_width,snake_height))) # add the snake head to the list
        if len(locations) > length:
            del locations[0] # delete the end of the snake if the length of the snake if the snake is already the correct length
        snakehead = locations[-1]
        if snakehead in applelocations: # if the snake head is touching an apple
            del applelocations[applelocations.index(snakehead)] # delete the apple the snake is touching
            length += 1
        if snakehead in locations[0:-1]: # if the snake head is touching another snake section
            snakeDead = True # kill the snake
        if pos[0] < 0 or pos[0] > width or pos[1] < 0 or pos[1] > height: # if the snake head is past the border of the screen
            snakeDead = True # kill the snake
        screen.fill(black)
        for location in range(len(locations)-1): # for every snake section that is not the head
            pygame.draw.rect(screen, snakegreen, locations[location]) # draw the section in green
        pygame.draw.rect(screen, green, snakehead) # now do that for the head with a slightly different green colour
        for apple in applelocations: # for every apple
            pygame.draw.rect(screen, red, apple) # draw the apple in red
    if snakeDead:
        screen.fill(black)
        text1 = my_font.render("You're dead!", False, (white))
        text2 = my_font.render("Press enter to play again.", False, (white))
        text3 = my_font.render("Press X to close.", False, (white))
        screen.blit(text1, ((width//2)-(text1.get_width()//2), (height//2)-(text1.get_height()//2)-(text1.get_height()))) # display the first text 1 height above the center
        screen.blit(text2, ((width//2)-(text2.get_width()//2), (height//2)-(text2.get_height()//2)))                      # display the second text in the center
        screen.blit(text3, ((width//2)-(text3.get_width()//2), (height//2)-(text3.get_height()//2)+(text3.get_height()))) # display the third text 1 height below the center
    pygame.display.flip() # draw
    time.sleep(0.5)

pygame.quit()
