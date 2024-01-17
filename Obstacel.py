import pygame
import random

"""
Obstacels versdchiedener Typen sollen unterscheideliche Reflektions Eigenschaften haben
    
"""

class Obstacel(pygame.sprite.Sprite):
    
    def __init__(self, screen, scale, difficulty):
        pygame.sprite.Sprite.__init__(self)
        
        self.screen = screen
        
        self.difficulty = difficulty
        self.ready_for_change = False
         
        self.image = pygame.image.load('grafics/Hinderniss_1.png')
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        
        self.position = self.generate_valid_position()
        self.speed_x = self.generate_valid_speed()
        self.speed_y = self.generate_valid_speed()
        
        self.rect = self.image.get_rect(center = self.position)
    
    def update(self):
        #Entscheidet je nach Schweirigkeit, wie sich dasHinderniss verändern soll
        if self.difficulty <= 1:
            #Die Hindernisse existieren entweder nicht oder sie verändern ihre Position nicht
            pass
        elif self.difficulty < 5:
            # Die Hindernisse teleportieren sich
            self.change_position()
        else:
            # Die Hindernisse bewegen sich
            self.move_position()
            self.collisions()
            
    # Die Hindernisse sollen in bestimmten Abständen ihre position wechseln        
    def check_for_time(self, current_game_timer, obstical_group_index):
        # je größer die Schwierigkeit umso öfter wird die Position gewechselt
        diff_modifier = 1000 - self.difficulty * 200
        if (current_game_timer + (obstical_group_index)*40 ) % diff_modifier == 0:
            self.ready_for_change = True
    
    def change_img():
        pass
    
    # Funktion, welche valide Werte für die Position des Hindernisses generieren
    def generate_valid_position(self):
        rand_x_pos = random.randint(int(self.screen.get_width() / 10 ), int(self.screen.get_width() - self.screen.get_width() / 10))
        rand_y_pos = random.randint(0, self.screen.get_height())
        rand_pos = (rand_x_pos, rand_y_pos)
        critical_x = False
        critical_y = False       
        
        # Prüfen ob zufällig generierte X-Position innerhalb des Spawn bereich des Balls liegt
        if rand_x_pos > self.screen.get_width() / 2 - (self.screen.get_width() / 10 + self.image.get_width() / 2) and rand_x_pos < self.screen.get_width() /  2 + (self.screen.get_width() / 10 + self.image.get_width() / 2):
            critical_x = True

        # Prüfen ob zufällig generierte Y-Position innerhalb des Spawn bereich des Balls liegt  
        if rand_y_pos > self.screen.get_height() / 2 - (self.screen.get_height() / 10 + self.image.get_height() / 2) and rand_y_pos < self.screen.get_height() / 2 + (self.screen.get_height() / 10 + self.image.get_height() / 2):
            critical_y = True
  
        # Nur wenn beide Koordinaten des Hindernisses innerhalb der Koordinaten des Spwans liegen, müssen rekursiv neue valide Koordinaten gefunden werden
        if critical_x and critical_y:
            rand_pos = self.generate_valid_position()
            
        return rand_pos
    
    def generate_valid_speed(self):
        if self.difficulty < 5:
            return 0
        else:
            difficulty_modifier = (self.difficulty - 4) * 1.5
            return random.uniform(- 1 *difficulty_modifier, difficulty_modifier)
      
    # Teleportationsähnliche Änderung der Postion
    def change_position(self):
        # Blöcke sollten ihre Position erst nach einer geiwssen Zeit ändern
        if self.ready_for_change:
            self.position = self.generate_valid_position()
            self.rect = self.image.get_rect(center = self.position)
            self.ready_for_change = False    
        
    # Die Blöcke können sich bewegen (wie ein Ball)
    def move_position(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.collisions()
        
    def collisions(self):
        # Das Hinderniss trifft auf Decke oder Boden:
        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
            self.speed_y *= -1
        # Das Hinderniss trifft auf eine der Wände:
        if self.rect.left <= 0 or self.rect.right >= self.screen.get_width():
            self.speed_x *= -1