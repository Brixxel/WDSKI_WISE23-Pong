import pygame

 # Inhalte eines Spieler Objekts. D.h.: Score; Items; Frabe etc


class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.score = 0
        self.skin = pygame.image.load('skins/Paddle.png')             # Standard-Textur für jedes Paddle

        self.player_speed = 15
        
        self.highscore = 0


    def update_score(self, by: int):
        self.score += by
        return self.score
   