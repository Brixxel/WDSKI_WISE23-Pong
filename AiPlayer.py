import pygame, random
from pygame.sprite import _Group

import Player, Paddel

# AiPlayer ist eine Spezielisierung des "normalen" Paddles - da dieses von einer Ai gespielt wird

class AIPlayer(Paddel):
    def __init__(self,path,x_pos,y_pos,speed, screen_height):
        
        # verpflichtender Aufruf des Übergeordneten Gruppen Konstruktors
        pygame.sprite.Sprite.__init__(path,x_pos,y_pos)
        
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