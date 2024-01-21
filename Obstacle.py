import pygame
import random
import os

"""
    Hindernisse haben einen zufälligen Skin und zufällige Größe.
    Hindernisse reflektieren den Ball wie eine Wand und ermöglichen so eine neue Spiel-Situation.
    Hindernisse können sich bewegen, teleportieren oder statisch ihre Postition beibehalten.
        Wenn sie sich bewegen, verhalten sie sich wie ein Ball, und prallen an Wänden und einander ab.
        Beim genereien der Hindernisse wird darauf geachtet, dass sie nicht im Spwanberreich des Balls generiert werden.
"""

class Obstacle(pygame.sprite.Sprite):
    
    def __init__(self, screen, scale, difficulty):
        pygame.sprite.Sprite.__init__(self)
        
        self.screen = screen
        
        self.difficulty = difficulty
        self.ready_for_change = False
        self.image = pygame.image.load(self.change_img(directory="obstacle_skins")) #Hindernisse bekommen zufälliges Image aus dem Ordner obtacle_skins
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        
        self.position = self.generate_valid_position()
        self.speed_x = self.generate_valid_speed()
        self.speed_y = self.generate_valid_speed()
        
        self.rect = self.image.get_rect(center = self.position)
        
        self.obstacle_group = pygame.sprite.Group()
    
    def update(self, game_modus_obstacle_group):
        
        
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Performance. evtl verlegen
        
        
        self.obstacle_group = game_modus_obstacle_group
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
    
    #Hindernisse sollen aus einem Ordner ein zufälliges .jpg bekommen
    def change_img(self,directory="."):
        
        #wählt nur die Images mit dem Ende jpg
        self.imgExtension = ["jpg"] 
        self.allImages = list()

        
        for img in os.listdir(directory): 
            ext = img.split(".")[len(img.split(".")) - 1]
            if (ext in self.imgExtension):
                self.allImages.append(os.path.join(directory, img))
        self.choice = random.randint(0, len(self.allImages) - 1)
        self.chosenImage = self.allImages[self.choice] 
        return self.chosenImage
    
    
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
    def move_position(self, ):
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
            
        if pygame.sprite.spritecollide(self,self.obstacle_group,False):
            collision_obstacle = pygame.sprite.spritecollide(self,self.obstacle_group,False)[0].rect
            
            if abs(self.rect.right - collision_obstacle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.rect.left - collision_obstacle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
            if abs(self.rect.top - collision_obstacle.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_obstacle.bottom
                self.speed_y *= -1
            if abs(self.rect.bottom - collision_obstacle.top) < 10 and self.speed_y > 0:
                self.rect.bottom = collision_obstacle.top
                self.speed_y *= -1