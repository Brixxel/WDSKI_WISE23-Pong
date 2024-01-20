import pygame, random
import Paddel, Ball 

"""
AiPlayer ist eine Spezielisierung des "normalen" Paddles - da dieses von einer Ai gespielt wird

 !!!!! evtl keine Spezialisierung des Paddles, sonder der Player Klasse --> Paddel AI Klasse?
"""

class AIPlayer():

    def __init__(self):

        paddle_img = [pygame.image.load("skins/Paddle_blue.png").convert_alpha(), pygame.image.load("skins/Paddle_green.png").convert_alpha(), 
            pygame.image.load("skins/Paddle_white.png").convert_alpha(), pygame.image.load("skins/Paddle_yellow.png").convert_alpha(), 
            pygame.image.load("skins/Paddle.png").convert_alpha()]
        
        self.skin = paddle_img[random.randint(0,4)]  
        self.score = 0
        self.player_speed = 7
        
        self.difficulty = 0
    
    # Liefert eine Funktion, abhängig vom Schwierigkeitsgrad der KI
    def operating(self):
        if self.difficulty == 0:
            # Funktion die für die Bewegung des Paddels zurückgegeben wird:
            def action(ball_group, paddel: Paddel):
                print("es wird leicht")
            return action 

        if self.difficulty == 1:
            # Funktion die für die Bewegung des Paddels zurückgegeben wird:

            def action(ball_group, paddel: Paddel):
                print("es wird mittel")
                observed_ball = ball_group.sprites()[0]
                if paddel.rect.top < observed_ball.rect.y:
                    paddel.rect.y += paddel.speed
                if paddel.rect.bottom > observed_ball.rect.y:
                    paddel.rect.y -= paddel.speed
                    paddel.screen_beschränkung(paddel.screen_height) 
            return action  
        if self.difficulty == 2:
            # Funktion die für die Bewegung des Paddels zurückgegeben wird:

            def action(ball_group, paddel: Paddel):
                print("es wird hard")
                nearest_Ball_y = 0
                nearest_Ball_x = 10000000000
                for ball in ball_group.sprites():
                    if ball.rect.x < nearest_Ball_x:
                        nearest_Ball_y = ball.rect.y
                if paddel.rect.top - 5 < nearest_Ball_y:
                    paddel.rect.y += paddel.speed
                if paddel.rect.bottom + 5 > nearest_Ball_y:
                    paddel.rect.y -= paddel.speed
                    paddel.screen_beschränkung(paddel.screen_height) 
                
            return action
        
