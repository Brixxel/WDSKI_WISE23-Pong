import pygame

 # Inhalte eines Spieler Objekts. D.h.: Score; Items; Frabe etc


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.score = 0
        self.skin = Paddle.png
     
   