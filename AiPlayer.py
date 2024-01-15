import pygame, random
from Paddel import Paddel 

"""
AiPlayer ist eine Spezielisierung des "normalen" Paddles - da dieses von einer Ai gespielt wird

 !!!!! evtl keine Spezialisierung des Paddles, sonder der Player Klasse --> Paddel AI Klasse?
"""

class AIPlayer(Paddel):
    
    def __init__(self):
        self.skin = pygame.image.load('skins/Paddle.png')
