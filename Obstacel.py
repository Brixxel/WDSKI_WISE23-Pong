import pygame

"""
Obstacels versdchiedener Typen sollen unterscheideliche Reflektions Eigenschaften haben
    
"""

class Obstacel(pygame.sprite.Sprite):
    
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
         
        self.image = pygame.image.load('grafics/Hinderniss_1.png')
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
        
    
    def change_position(self):
        pass
    
    
    