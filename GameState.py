import pygame, random
import Player, Paddel, AiPlayer, Ball, Obstacel


class GameState_Manager:
    
    def __init__(self, screen):
    
        # !!! evtl ja nach KI anpassen
        self.player_ai = AiPlayer.AIPlayer()
        
        # nicht initialisierte Paddels -- werden bei jedem neuen Spiel dieser GamestateKlasse überschrieben
        self.paddle_player_1 = 0
        self.paddle_player_2 = 0
        #self.ball = 0
        #self.ball02 = 0
        
        self.ball_group = pygame.sprite.Group()
        self.paddle_group = pygame.sprite.Group()
        
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        self.game_timer = 0

        # Design Standarts
        self.standart_font = pygame.font.Font('freesansbold.ttf', 32)
        self.accent_color = (27,35,43)
        
        
        # !!!!! Abänderung auf Intensitäts Kriterium (0 - kein Modus Feature - 1,2,3,4 ... in jeweils erhöter Ausführung)
        
        # Optionale Spiel-Modi-Ergänzungen:
        self.game_modus_feature_increasingSpeed  = False         # Spielmodus, bei dem nach Spiel-Zeit, die Reflexion verstärkt wird
        self.game_modus_feature_increasingSpeed_intensity = 1
        self.game_modus_feature_increasingReflektion = False       # Spielmodus, der nach gewisser Anzahl an Reflektionen die Geschwindikeit erhöt
        self.game_modus_feature_Obstacel_count = 5                  # Spielmodus, bei dem zusätzliche Hindernisse das Spiel erschwerden oder vereinfachen
        self.game_modus_feature_Obstacel_difficulty = 0

        self.game_modus_balls_count = 12                             # Spielmodus, der die Anzahl der Bälle veränderlich macht
        
        # Spiel Mosu Atribute
        self.game_modus_obstacel_group = pygame.sprite.Group()
        
    def run_game(self):
		# Drawing the game objects
        self.paddle_group.draw(self.screen)
        self.ball_group.draw(self.screen)
        
        
        
        # Auführen besonderer Spiel-Modi
        if self.game_modus_feature_increasingSpeed:
            self.feature_increasing_Speed()
        if self.game_modus_feature_increasingReflektion:
            self.feature_increasing_Reflection()
        if self.game_modus_feature_Obstacel_difficulty != 0:
            self.game_modus_obstacel_group.draw(self.screen)
            self.feature_Obstacels()
            self.game_modus_obstacel_group.update(self.game_modus_obstacel_group)
            pass

		# Updating the game objects
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()
        
        # Timer / run-Durchlauf um eins erhöhen
        self.game_timer += 1
    
    # Wenn ein Punkt erziehlt wurde: (Sowohl Überprüfung wie auch Score Erhöhung)
    def reset_ball(self):
        for ball in self.ball_group.sprites():
            
            if ball.rect.right >= self.screen_width:
                self.paddle_player_2.player.score += 1
                ball.reset_ball()
            if ball.rect.left <= 0:
                self.paddle_player_1.player.score += 1
                ball.reset_ball()
            
    # Um den aktuellen Spiel-Score von Spieler und Gegner darzustellen:
    def draw_score(self):
        player_1_score = self.standart_font.render(str(self.paddle_player_1.player.score),True,self.accent_color)
        opponent_score = self.standart_font.render(str(self.paddle_player_2.player.score),True,self.accent_color)

        player_score_rect = player_1_score.get_rect(midleft = (self.screen_width / 2 + 40,self.screen_height/2))
        opponent_score_rect = opponent_score.get_rect(midright = (self.screen_width / 2 - 40,self.screen_height/2))

        self.screen.blit(player_1_score,player_score_rect)
        self.screen.blit(opponent_score,opponent_score_rect)
        
    
# --------------------------------------------------------------------------------------- #
# Spiel-Modi Funktioen
# --------------------------------------------------------------------------------------- #
    
    # !!! Achtung: für Multi-Ball muss hier jeweils auf mehrere Bälle erweitert werden !!!
    
    # Spiel-Modus: je länger gespielt wird, umso schneller wird der Ball
    def feature_increasing_Speed(self):
        if self.game_modus_feature_increasingSpeed:
            if self.game_timer % 1000 == 0:
                for ball in self.ball_group.sprites():
                    ball.speed_x = ball.speed_x * 1.1
                    ball.speed_y = ball.speed_y * 1.1
                    # !!!!! Print Statement entfehrnen
                    print(f"Erhöhe Geschwindigkeit auf: {ball.speed_x}")
    
    # Spiel-Modus: je öfter der Ball Reflektiert wird, um so schneller bewegt er sich
    def feature_increasing_Reflection(self):
        if self.game_modus_feature_increasingReflektion:
            for ball in self.ball_group.sprites():
                ball.increasing_reflection()
       


# ......................... Obstacels ................................................... #

    def feature_Obstacels(self):
        # Die Blöcke ändern nach gewisser Zeit ihre Position -> Variable die dem Obstical sagt, dass es sich ändern soll
        count = 0
        for obstacel in self.game_modus_obstacel_group.sprites():
            # Bei einer Schwierigkeit des Hinderniusses von 1, bewegen sie sich nicht
            # Bei einer Schwierigkeit des Hinderniusses zwischen 2 und 4 teleportieren sie sich (mit zunehmnder Schwierigkeit häufiger)
            if obstacel.difficulty < 5 and obstacel.difficulty != 1:
                obstacel.check_for_time(self.game_timer, count)
                count += 1
            # Bei einer Schwierigkeit des Hinderniusses von größer, gleich 5, können diese sich bewegen wie ein Ball
            elif obstacel.difficulty >= 5:
                obstacel.move_position()
        
    
    # Initialisiert die Hindernisse standartisiert
    def feature_Obstacels_initialise(self):
        self.game_modus_obstacel_group.empty()
        # !!!! evtl unterschiedliche Arten von Hindernissen
        for x in range(self.game_modus_feature_Obstacel_count):
           
            rand_scale = random.uniform(1,3.5)
            obstacel_1 = Obstacel.Obstacel(self.screen, rand_scale, self.game_modus_feature_Obstacel_difficulty)
            self.game_modus_obstacel_group.add(obstacel_1)
        for ball in self.ball_group.sprites():
            ball.obstacels = self.game_modus_obstacel_group

 
# --------------------------------------------------------------------------------------- #
# Spiel - Initialisierungs / Generierungs Methoden
# --------------------------------------------------------------------------------------- # 
 
 
# New Game Methode, die den Speilstand des bisherigen Spiels löscht und mit den neuen Paddels beginnt
    def Start_PvAi_Game(self, player_1 : Player):
        
        self.paddle_player_1 = Paddel.Paddel(player_1, self.screen_width - 20, self.screen_height/2, 5, self.screen_height)
        # entspricht hier einem AI Paddle
        self.paddle_player_2 = Paddel.Paddel(self.player_ai,20,self.screen_width/2, 5, self.screen_height)
        
        self.general_setUp()
        
        return "PvAi"

    def Start_PvP_Game(self, player_1 : Player, player_2 : Player):
        
        self.paddle_player_1 = Paddel.Paddel(player_1, self.screen_width - 20, self.screen_height/2, 5, self.screen_height)
        self.paddle_player_2 = Paddel.Paddel(player_2,20,self.screen_width/2, 5, self.screen_height)

        self.general_setUp()
              
        return "PvP"

    def general_setUp(self):
        self.paddle_group.empty()
        self.paddle_group.add(self.paddle_player_1)
        self.paddle_group.add(self.paddle_player_2)
        
        self.ball_group.empty()
        for x in range(self.game_modus_balls_count):
            ball = Ball.Ball('Ball.png', self.screen_width/2, self.screen_height/2, 4, 4, self.paddle_group, self.screen_height, self.screen_width, self.screen)
            self.ball_group.add(ball)
        
        if self.game_modus_feature_Obstacel_difficulty != 0:
            self.feature_Obstacels_initialise()
        
        self.game_timer = 0