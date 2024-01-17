import pygame, random

import Player, AiPlayer

""" 
Spieler / Ai während des Spiels - für jedes Spiel ein neues Paddel

Das Paddel wird einem Spieler / AiSpieler zugeordnet - übernimmt von diesem den Skin und weiter Eigenschaften


"""

class Paddel(pygame.sprite.Sprite):
    
    def __init__(self, player,x_pos,y_pos,speed, screen_height):
        # verpflichtender Aufruf des Übergeordneten Gruppen Konstruktors
        pygame.sprite.Sprite.__init__(self)
        
        #legt fest, welchem Player das Paddel zugeordnet ist
        self.player = player

        # Generiert das Paddle, mit dem Aussehen und der Pixel-Größe des gewählten PNGs
        self.image = player.skin
        # Bildet das Rechteck (Pixel des Bildes gleich Maße des Rechtecks)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
        
        # weitere Spiel-relevante Variablen wie die Geschwindigkeit, mit der sich das Paddle bewegt
        
        # (Nur Vollgas oder kein Gas - keine Beschleunigung - Speed gibt die Max V vom Paddle an)
        self.speed = player.player_speed
        
        # Gibt die aktuelle Bewegung des Paddels an / (Wird dann per TastenEingabe temporär verändert)
        self.movement = 0
        
        # Standart Info, wie der Bildschrim aussieht
        self.screen_height = screen_height

    # Das Paddle kann sich nur innerhalb des Bildschirms bewegen, 
    # daher muss seine Bewegung eingeschränlt werden
    def screen_beschränkung(self, screen_height):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

    # Passt die Position des Paddles, abhängig von seiner Bewegung, an
    def update(self, ball_group):
        # Positions Update, wennn es sich um ein Spieler Paddel handelt:
        if isinstance(self.player, Player.Player):
            
            self.rect.y += self.movement
            self.screen_beschränkung(self.screen_height)

        # Updaten, wie wenn es sich um eine Ai handelt:
            # anpassen nach Ai Typus (Stärke)    
        elif isinstance(self.player, AiPlayer.AIPlayer):
            
            if self.rect.top < ball_group.sprite.rect.y:
                self.rect.y += self.speed
            if self.rect.bottom > ball_group.sprite.rect.y:
                self.rect.y -= self.speed
                self.screen_beschränkung(self.screen_height)            