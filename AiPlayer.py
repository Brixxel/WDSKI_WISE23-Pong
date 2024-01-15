import pygame, random
from Paddel import Paddel 

"""
AiPlayer ist eine Spezielisierung des "normalen" Paddles - da dieses von einer Ai gespielt wird

 !!!!! evtl keine Spezialisierung des Paddles, sonder der Player Klasse --> Paddel AI Klasse?
"""


class AIPlayer(Paddel):
    
    def __init__(self,path,x_pos,y_pos,speed, screen_height):
        
        # verpflichtender Aufruf des Übergeordneten Gruppen Konstruktors
        pygame.sprite.Sprite.__init__(self)
        
        # Generiert das Paddle wie ein "normales"
        # Hier SPÄTER zufällige "Farb"-Wahl ############# !!!!!!!
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))

        self.speed = speed
        self.screen_height = screen_height
        
        
    def update(self,ball_group):
        if self.rect.top < ball_group.sprite.rect.y:
            self.rect.y += self.speed
        if self.rect.bottom > ball_group.sprite.rect.y:
            self.rect.y -= self.speed
        self.screen_beschränkung(self.screen_height)