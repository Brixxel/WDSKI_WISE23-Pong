import pygame, random, Explosion

"""
Ball ist eine Klasse die, die Atribute und Methoden enthält, die ein Ball für Pong benötigt:

    1.) Die Update-Methode, die jedes relevante Atribut einer Ball Entität pro Spiel-Tick aktualisier. (Darunter Position, Kollison mit Wand und Hinderniss)
    2.) ...

"""

class Ball(pygame.sprite.Sprite):
    def __init__(self,path,x_pos,y_pos,paddles,screen_height, screen_width, screen):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
             
        # Richtungs Vektor, wird in Methode bestimmt, hier wird weiter Komponenten-weise betrachtet:
        self.speed_x = self.generate_valid_speed()[0]
        self.speed_y = self.generate_valid_speed()[1]
        
        # Zustands-Atribute des Balls
        self.paddles = paddles
        self.active = False
        self.score_time = 0
        self.obstacels = pygame.sprite.Group()
        
        # Variablen, die der Ball über den Screen / das Spielfeld braucht
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen = screen
        
        self.reflections_since_new_round = 0
        
    # Relevanteste Methode, die den Ball pro Spiel-Tick, updatet    
    def update(self):
        # Wenn der Ball im Spiel ist (Sich bewegt und nicht gerade wartet):
        if self.active:
            # verändert er seine Position, abhängig von seiner Bewegungsrichtung
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            # Und überprüft auf Kollisionen und damit einhergehende Reflektionen
            self.collisions()
            self.collision_obstacel()
            
        else:
             self.restart_counter()
            
    def collisions(self):
        # Der Ball trifft auf Decke oder Boden:
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            pygame.mixer.Sound("sounds/hit_sound.mp3").play()
            self.speed_y *= -1 # Richtung der vertikalen Geschwindigkeitskomponente umkehren
        # Der Ball trifft auf ein Paddle:
        if pygame.sprite.spritecollide(self,self.paddles,False):
            # Reflexions Counter erhöhen, da Ball von Paddle getroffen wurde
            self.reflections_since_new_round += 1
            pygame.mixer.Sound("sounds/hit_sound.mp3").play()
            collision_paddle = pygame.sprite.spritecollide(self,self.paddles,False)[0].rect
             # Abhängig davon, wo der Ball das Paddle getroffen hat, die Richtung der horizontalen Geschwindigkeitskomponente ändern
            if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
            # Abhängig davon, wo der Ball das Paddle getroffen hat, die Richtung der vertikalen Geschwindigkeitskomponente ändern
            if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_paddle.bottom
                self.speed_y *= -1
            if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
                self.rect.bottom = collision_paddle.top
                self.speed_y *= -1

    def reset_ball(self):

        self.speed_x = self.generate_valid_speed()[0]
        self.speed_y = self.generate_valid_speed()[1]
        self.score_time = pygame.time.get_ticks()
        self.rect.center = (self.screen_width/2,self.screen_height/2)
        #pygame.mixer.Sound.play(score_sound)
        print(self.speed_x)
        print(f"Speed Y: {self.speed_y}")
        
    def restart_counter(self):
        current_time = pygame.time.get_ticks()
        countdown_number = 3
        
        if current_time - self.score_time <= 700:
            countdown_number = 3
        if 700 < current_time - self.score_time <= 1400:
            countdown_number = 2
            self.explosions_animation.active = False
        if 1400 < current_time - self.score_time <= 2100:
            countdown_number = 1
        if current_time - self.score_time >= 2100:
            pygame.mixer.Sound("sounds/start_sound.mp3").play()
            self.active = True
            self.reflections_since_new_round = 0
            
            
        time_counter = pygame.font.Font('freesansbold.ttf', 32).render(str(countdown_number),True,(27,35,43))
        time_counter_rect = time_counter.get_rect(center = (self.screen_width/2,self.screen_height/2 + 50))
        pygame.draw.rect(self.screen,('#2F373F'),time_counter_rect)
        self.screen.blit(time_counter,time_counter_rect)
    
# --------------------------------------------------------------------------------------------------------- #
# Methoden für die Spiel-Modi
    
    # "härtere Reflektion"
    def increasing_reflection(self):
        if self.reflections_since_new_round % 2 == 0 and pygame.sprite.spritecollide(self,self.paddles,False):
            self.speed_x = self.speed_x * 1.5
            self.speed_y = self.speed_y * 1.5
            print(f"Paddle erhöhete Speed auf: {self.speed_x}")
           
    # Reflektion an Hindernissen        
    def collision_obstacel(self):
        if self.obstacels:
            if pygame.sprite.spritecollide(self,self.obstacels,False):
                # Reflexions Counter erhöhen, da Ball von Paddle getroffen wurde
                self.reflections_since_new_round += 1
                # Sound, für das Reflektieren
                pygame.mixer.Sound("sounds/hit_sound.mp3").play()
                # Richtungsänderung des Balls, abhängig auf welcher Seitde er auf ein Hinderniss getroffen ist
                collision_paddle = pygame.sprite.spritecollide(self,self.obstacels,False)[0].rect
                if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
                    self.speed_x *= -1
                if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
                    self.speed_x *= -1
                if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
                    self.rect.top = collision_paddle.bottom
                    self.speed_y *= -1
                if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
                    self.rect.bottom = collision_paddle.top
                    self.speed_y *= -1
                    
    # Methode, die einen Valieden Richtuingsvektors eines Balls zurückgibt
    def generate_valid_speed(self):
        # Ursprungs-Geschwindigkeis-Vektor
        speed = (0 , 0)
        # Der Ball sollte sich möglichst nicht senk- bzw. wagerecht bewegen, dass wird durch den Vergleich der quadratischen Komponenten garantiert
        while speed[0]**2 < 6 or speed[1]**2 < 6:
            speed_x =  random.uniform(-5,5)
            speed_y =  random.uniform(-5,5)
            speed = (speed_x, speed_y)
        # das korrekte Speed-Tupel wird übergeben
        return speed