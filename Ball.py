import pygame, random

class Ball(pygame.sprite.Sprite):
    def __init__(self,path,x_pos,y_pos,speed_x,speed_y,paddles,screen_height, screen_width, screen):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
             
        self.speed_x = speed_x * random.choice((-1,1))
        self.speed_y = speed_y * random.choice((-1,1))
        
        self.paddles = paddles
        self.active = False
        self.score_time = 0
        
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen = screen
        
        self.reflections_since_new_round = 1
        
        
    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()
        else:
             self.restart_counter()
            
    def collisions(self):
        # Der Ball trifft auf Decke oder Boden:
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            #pygame.mixer.Sound.play(plob_sound)
            self.speed_y *= -1
        # Der Ball trifft auf ein Paddle:
        if pygame.sprite.spritecollide(self,self.paddles,False):
            # Reflexions Counter erhöhen, da Ball von Paddle getroffen wurde
            self.reflections_since_new_round += 1
            #pygame.mixer.Sound.play(plob_sound)
            collision_paddle = pygame.sprite.spritecollide(self,self.paddles,False)[0].rect
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
        
    
    def reset_ball(self):
        self.active = False
        self.speed_x *= random.choice((-1,1))
        self.speed_y *= random.choice((-1,1))
        self.score_time = pygame.time.get_ticks()
        self.rect.center = (self.screen_width/2,self.screen_height/2)
        #pygame.mixer.Sound.play(score_sound)
        
    def restart_counter(self):
        current_time = pygame.time.get_ticks()
        countdown_number = 3
        
        if current_time - self.score_time <= 700:
            countdown_number = 3
        if 700 < current_time - self.score_time <= 1400:
            countdown_number = 2
        if 1400 < current_time - self.score_time <= 2100:
            countdown_number = 1
        if current_time - self.score_time >= 2100:
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
        if self.reflections_since_new_round % 2 == 0:
            self.speed_x = self.speed_x * 1.5
            self.speed_y = self.speed_y * 1.5
        print(self.speed_x)