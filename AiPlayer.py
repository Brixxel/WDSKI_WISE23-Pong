import pygame, random
import Paddel 

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