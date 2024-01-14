import pygame, sys, random
# More imports...
import Player

# #########################################
# Version 1.0 Beta
# @Felix Regler, @Tom Weber, @Gina G
# 13.02.2024
# #########################################

def ball_animation():
	global ball_speed_x, ball_speed_y, player_score, opponent_score
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y


    # Ball trifft auf Decke
	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1
  
    # Ball trifft auf Wand:
    # Player Score
	if ball.left <= 0: 
		ball_start()
		player_score += 1

	# Opponent Score
	if ball.right >= screen_width:
		ball_start()
		opponent_score += 1	    


    # Ball wird von Spieler "gespielt"
	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1



def player_animation():
	player.y += player_speed

	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height
  
def opponent_ai():
	if opponent.top < ball.y:
		opponent.y += opponent_speed
	if opponent.bottom > ball.y:
		opponent.y -= opponent_speed

	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height
  
def ball_start():
	global ball_speed_x, ball_speed_y

	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))
  

# ################ #
# Initialisieren des Spiels - Grundzustands
# ################ #

# General setup
pygame.init()
clock = pygame.time.Clock()

# setting the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')


#Game Rectangel
ball = pygame.Rect((screen_width/2) - 15, (screen_height/2) - 15, 30,30)

player = player_1.create_Player_obj(screen_width, screen_height)

opponent = pygame.Rect(10, screen_height/ 2 - 70, 10, 140)


# Farben
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)


# ################################################ #
# Hier läuft das ganze Spiel
# ################################################ #

while True:
    
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_UP:   
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7
    
    # Game logic
    
    ball_animation()
    player_animation()
    opponent_ai()
    
    
    
    # Visuals
    # Hier werden alle Darstellungen erst geprintet
    
    
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
    
    player_text = basic_font.render(f'{player_score}',False,light_grey)
    screen.blit(player_text,(660,470))

    opponent_text = basic_font.render(f'{opponent_score}',False,light_grey)
    screen.blit(opponent_text,(600,470))
    
    
    #Updating the window
    pygame.display.flip()
    clock.tick(60)

