import pygame, random
import Paddel, Ball 

"""
AiPlayer ist eine Klasse die, die Atribute und Methoden enthält, die ein AI-Player für Pong benötigt:

    1.) da der Paddel Skin aus dem Spieler entnommen wird, hat jeder Ai Spieler eine Liste an möglichen skins, aus der ein einen zufällig auswählt
    2.) der AI-Spieler passt sein Verhalten je nach Schwierigkeitsgrad an und gibt eine andere Verhaltens Methode an das ihm zugewiesene Paddle zurück 

"""

class AIPlayer():

    def __init__(self):

        paddle_img = [pygame.image.load("skins/Paddle_blue.png").convert_alpha(), pygame.image.load("skins/Paddle_green.png").convert_alpha(), 
            pygame.image.load("skins/Paddle_white.png").convert_alpha(), pygame.image.load("skins/Paddle_yellow.png").convert_alpha(), 
            pygame.image.load("skins/Paddle.png").convert_alpha()]
        
        # Die relevanten Atribute für einen AI-Player
        self.skin = paddle_img[random.randint(0,4)]  
        self.score = 0
        self.player_speed = 7
        
        # Die Standart Schwierigkeit, wird später über GameState geändert
        self.difficulty = 0
    
    # Liefert eine Funktion, abhängig vom Schwierigkeitsgrad der KI
    def operating(self):
        if self.difficulty == 0:
            # Funktion die für die Bewegung des Paddels zurückgegeben wird:
            # Das Paddel wird mit dieser Funktion einfach von unten nach oben und umgekehrt fahren
            def action(ball_group, paddel: Paddel):
                print(paddel.moving_up)
                # prüft ob das Paddle sich in positive Y-Richtung bewegt:
                if paddel.moving_up:
                    paddel.rect.y += random.uniform(0.5, 1) * paddel.speed
                    # Wenn das Paddle ganz unten angekommen ist, ändert es seine Richtung
                    if paddel.rect.y > paddel.screen_height - paddel.rect.height - 60:
                        paddel.moving_up = False
                else:
                    # Das Paddel bewegt sich also in negative Y-Richtung:
                    paddel.rect.y -= random.uniform(0.5, 1) * paddel.speed
                    # Wenn das Paddle ganz oben angekommen ist, ändert es seine Richtung
                    if paddel.rect.y < 60:
                        paddel.moving_up = True
                # Überprüft stetig, ob das Paddel noch innerhalb des Screens ist.
                # Theoretisch redundant, zur Sicherheit jedoch hier implimentiert.
                paddel.screen_beschränkung(paddel.screen_height)
            return action 

        if self.difficulty == 1:
            # Funktion die für die Bewegung des Paddels zurückgegeben wird:
            # Das Paddel orientiert sich an dem ersten Ball der Ball-Gruppe
            def action(ball_group, paddel: Paddel):
                observed_ball = ball_group.sprites()[0]
                if paddel.rect.top < observed_ball.rect.y:
                    paddel.rect.y += paddel.speed
                if paddel.rect.bottom > observed_ball.rect.y:
                    paddel.rect.y -= paddel.speed
                    paddel.screen_beschränkung(paddel.screen_height) 
            return action
          
        if self.difficulty == 2:
            # Funktion die für die Bewegung des Paddels zurückgegeben wird:
            # Das Paddel versucht stehts den Ball in seiner Mitte zu haben, der dem Paddel am nähsten ist
            def action(ball_group, paddel: Paddel):
                nearest_Ball_y = 0
                nearest_Ball_x = 10000000000
                # itteriert durch alle Bälle um zu prüfen, welcher Ball am nähsten am Paddle ist
                for ball in ball_group.sprites():
                    if ball.rect.x < nearest_Ball_x:
                        nearest_Ball_x = ball.rect.x            # passt dann dessen Koordinate als die nähste x-Koordinate an
                        nearest_Ball_y = ball.rect.y            # und übernimmt auch dessen Y-Ausrichtung
                # Aufgrund des oben ermittelten Y-Wert des nähsten Balls, wird die Bewegung / Positions Anpassung des Paddles bestimmt:    
                if paddel.rect.top + 20 < nearest_Ball_y:
                    paddel.rect.y += paddel.speed
                if paddel.rect.bottom - 20 > nearest_Ball_y:
                    paddel.rect.y -= paddel.speed
                    paddel.screen_beschränkung(paddel.screen_height)     
            return action