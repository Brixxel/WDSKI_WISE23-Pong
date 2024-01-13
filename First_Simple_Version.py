import pygame, sys
# More imports...

# #########################################
# Version 1.0 Beta
# @Felix Regler, @Tom Weber, @Gina G
# 13.02.2024
# #########################################

# General setup
pygame.init()
clock = pygame.time.Clock()

# setting the main window
screen_width = 1280
screen_heigth = 960
screen = pygame.display.set_mode((screen_width,screen_heigth))
pygame.display.set_caption('Pong')




while True:
    #Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    #Updating the window
    pygame.display.flip()
    clock.tick(60)

