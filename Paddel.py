import pygame
from pygame.sprite import _Group

import Player

""" 
Spieler / Ai während des Spiels - für jedes Spiel ein neues Paddel

"""

class Paddel(pygame.sprite.Sprite):
    
    def __init__(self,path,x_pos,y_pos,speed):
        # verpflichtender Aufruf des Übergeordneten Gruppen Konstruktors
        pygame.sprite.Sprite.__init__(path,x_pos,y_pos)
        
        # Generiert das Paddle, mit dem Aussehen und der Pixel-Größe des gewählten PNGs
        self.image = pygame.image.load(path)
        # Bildet das Rechteck (Pixel des Bildes gleich Maße des Rechtecks)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
        
        # weitere Spiel-relevante Variablen wie die Geschwindigkeit, mit der sich das Paddle bewegt
        # (Nur Vollgas oder kein Gas - keine Beschleunigung - Speed gibt die Max V vom Paddle an)
        self.speed = speed
        # Im Urzustand bewegt sich das Paddle nicht
        self.movement = 0

    # Das Paddle kann sich nur innerhalb des Bildschirms bewegen, 
    # daher muss seine Bewegung eingeschränlt werden
    def screen_beschränkung(self, screen_height):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height


    # Passt die Position des Paddles, abhängig von seiner Bewegung, an
    def update(self, ball_group, screen_height):
        self.rect.y += self.movement
        self.screen_beschränkung(screen_height)