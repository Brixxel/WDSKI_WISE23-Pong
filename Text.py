import pygame

class Text(pygame.sprite.Sprite):

    def __init__(self,text, x, y):
        
        pygame.init()
        self.text = text
        self.antialias = True
        self.colour = (157,0,255)    
        self.background = None
        self.font = pygame.font.Font('freesansbold.ttf',30)
        self.img = self.font.render(self.text, self.antialias, self.colour,self.background)
        self.pos = (x,y)   
    def blitnew (self,surface):
        surface.blit(self.img, self.pos)
    def remove(self):
        self.text = " "    
