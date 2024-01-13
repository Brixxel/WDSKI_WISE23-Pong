import pygame, sys
# More imports...

# #########################################
# Version 1.0 Beta
# @Felix Regler, @Tom Weber, @Gina G
# 13.02.2024
# #########################################

def ball_animation():
	global ball_speed_x, ball_speed_y
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_heigth:
		ball_speed_y *= -1
	if ball.left <= 0 or ball.right >= screen_width:
		ball_speed_x *= -1

	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1


# General setup
pygame.init()
clock = pygame.time.Clock()

# setting the main window
screen_width = 1280
screen_heigth = 960
screen = pygame.display.set_mode((screen_width,screen_heigth))
pygame.display.set_caption('Pong')


#Game Rectangel
ball = pygame.Rect((screen_width/2) - 15, (screen_heigth/2) - 15, 30,30)
player = pygame.Rect((screen_width - 20), (screen_heigth/2 -70), 10, 140)
opponent = pygame.Rect(10, screen_heigth/ 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7
ball_speed_y = 7


while True:
    
    #Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Game logic
    ball_animation()
    
    
    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_heigth))
    
    
    
    #Updating the window
    pygame.display.flip()
    clock.tick(60)

