import pygame, random
import Player, Paddel, AiPlayer, Ball, Obstacle, Explosion


class GameState:
    
    def __init__(self, screen, ai_player):
    
        # die KI
        self.player_ai: AiPlayer.AIPlayer = ai_player
        
        # nicht initialisierte Paddels -- werden bei jedem neuen Spiel dieser GamestateKlasse überschrieben
        self.paddle_player_1: Paddel.Paddel
        self.paddle_player_2: Paddel.Paddel
        
        self.ball_group = pygame.sprite.Group()
        self.paddle_group = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group()
        
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        self.game_timer = 0

        # Design Standarts
        self.standart_font = pygame.font.Font('freesansbold.ttf', 32)
        self.accent_color = (27,35,43)
        
        
        # Optionale Spiel-Modi-Ergänzungen:
        self.game_modus_feature_increasingSpeed  = False            # Spielmodus, bei dem nach Spiel-Zeit, die Reflexion verstärkt wird
        self.game_modus_feature_increasingSpeed_intensity = 1
        self.game_modus_feature_increasingReflektion = False        # Spielmodus, der nach gewisser Anzahl an Reflektionen die Geschwindikeit erhöt
        self.game_modus_feature_obstacle_count = 5                  # Spielmodus, bei dem zusätzliche Hindernisse das Spiel erschwerden oder vereinfachen
        self.game_modus_feature_obstacle_difficulty = 0             # Gibt an, ob es statische(1), sich teleporteierende(2,3,4) oder sich bewegende Hindernisse sind(5,6,7)   

        self.game_modus_balls_count = 1                             # Spielmodus, der die Anzahl der Bälle veränderlich macht
        
        # Spiel Modus Atribute
        self.game_modus_obstacle_group = pygame.sprite.Group()      # Speichert alle Hindernisse des aktuellen Spiels
        
    def run_game(self):
        
		# Drawen der Game-Objekte der Paddels und des Balls
        self.paddle_group.draw(self.screen)
        self.ball_group.draw(self.screen)
        

        # Auführen besonderer Spiel-Modi, sofern diese aktiviert sind
        if self.game_modus_feature_increasingSpeed:
            self.feature_increasing_Speed()
        if self.game_modus_feature_increasingReflektion:
            self.feature_increasing_Reflection()
        if self.game_modus_feature_obstacle_difficulty != 0:
            # 0 stünde für keine Hindernisse
            self.game_modus_obstacle_group.draw(self.screen)
            self.feature_obstacles()
            self.game_modus_obstacle_group.update(self.game_modus_obstacle_group)

        # Updating der game Objekte
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.explosion_group.update()
        self.reset_ball()
        self.draw_score()

        # Timer / run-Durchlauf um eins erhöhen
        self.game_timer += 1
    
    # Wenn ein Punkt erziehlt wurde: (Sowohl Überprüfung wie auch Score Erhöhung)
    def reset_ball(self):
        for ball in self.ball_group.sprites():
            
            if ball.rect.right >= self.screen_width:
                # Punktzahl des erfolgreichen Spielers / AI erhöhen
                self.paddle_player_2.player.score += 1
                
                #Explosions Animation erstellen
                explosion = Explosion.Explosion(ball.rect.right - 20, ball.rect.y)
                self.explosion_group.add(explosion)
                self.explosion_group.draw(self.screen)
                self.explosion_group.remove(explosion)
                # Explosions Sound, für das athmossphärische Erlebniss
                pygame.mixer.Sound("sounds/explosion_sound.wav").play()
                
                pygame.display.update()
                ball.reset_ball()
                
            if ball.rect.left <= 0:
                # Punktzahl des erfolgreichen Spielers / AI erhöhen
                self.paddle_player_1.player.score += 1
                
                #Explosions Animation erstellen
                self.explosion = Explosion.Explosion(ball.rect.left+20, ball.rect.y)
                self.explosion_group.add(self.explosion)
                self.explosion_group.draw(self.screen)
                self.explosion_group.remove(self.explosion)
                # Explosions Sound, für das athmossphärische Erlebniss
                pygame.mixer.Sound("sounds/explosion_sound.wav").play()
                
                pygame.display.update()
                ball.reset_ball()
            
    # Um den aktuellen Spiel-Score von Spieler und Gegner darzustellen:
    def draw_score(self):
        # Die Werte / der Punktstand wird im jewelig instanzierten Player-Paddel gespeichert
        player_1_score = self.standart_font.render(str(self.paddle_player_1.player.score),True,self.accent_color)
        opponent_score = self.standart_font.render(str(self.paddle_player_2.player.score),True,self.accent_color)
        # Die Werte / der Punktstand wird im jewelig instanzierten Player-Paddel gespeichert
        player_score_rect = player_1_score.get_rect(midleft = (self.screen_width / 2 + 40,self.screen_height/2))
        opponent_score_rect = opponent_score.get_rect(midright = (self.screen_width / 2 - 40,self.screen_height/2))

        self.screen.blit(player_1_score,player_score_rect)
        self.screen.blit(opponent_score,opponent_score_rect)
        
    
# --------------------------------------------------------------------------------------- #
# Spiel-Modi Funktioen
# --------------------------------------------------------------------------------------- #

    # Alle Methoden ittereien durch alle aktuellen Bälle    
    # Spiel-Modus: je länger gespielt wird, umso schneller wird der Ball
    def feature_increasing_Speed(self):
        if self.game_modus_feature_increasingSpeed:
            if self.game_timer % 1000 == 0:
                for ball in self.ball_group.sprites():
                    ball.speed_x = ball.speed_x * 1.1
                    ball.speed_y = ball.speed_y * 1.1
    
    # Spiel-Modus: je öfter der Ball Reflektiert wird, um so schneller bewegt er sich
    def feature_increasing_Reflection(self):
        if self.game_modus_feature_increasingReflektion:
            for ball in self.ball_group.sprites():
                ball.increasing_reflection()
    


# ......................... obstacles ................................................... #

    def feature_obstacles(self):
        # Die Blöcke ändern nach gewisser Zeit ihre Position -> Variable die dem Obstical sagt, dass es sich ändern soll
        count = 0
        for obstacle in self.game_modus_obstacle_group.sprites():
            # Bei einer Schwierigkeit des Hinderniusses von 1, bewegen sie sich nicht
            # Bei einer Schwierigkeit des Hinderniusses zwischen 2 und 4 teleportieren sie sich (mit zunehmnder Schwierigkeit häufiger)
            if obstacle.difficulty < 5 and obstacle.difficulty != 1:
                obstacle.check_for_time(self.game_timer, count)
                count += 1
            # Bei einer Schwierigkeit des Hinderniusses von größer, gleich 5, können diese sich bewegen wie ein Ball
            elif obstacle.difficulty >= 5:
                obstacle.move_position()
        
    
    # Initialisiert die Hindernisse standartisiert
    def feature_obstacles_initialise(self):
        self.game_modus_obstacle_group.empty()
        # !!!! evtl unterschiedliche Arten von Hindernissen
        for x in range(self.game_modus_feature_obstacle_count):
        
            rand_scale = random.uniform(1,3.5)*0.05

            obstacle_1 = Obstacle.Obstacle(self.screen, rand_scale, self.game_modus_feature_obstacle_difficulty)
            self.game_modus_obstacle_group.add(obstacle_1)
        for ball in self.ball_group.sprites():
            ball.obstacles = self.game_modus_obstacle_group


# --------------------------------------------------------------------------------------- #
#                      Spiel - Initialisierungs / Generierungs Methoden                   #
# --------------------------------------------------------------------------------------- # 


# New Game Methode, die den Speilstand des bisherigen Spiels löscht und mit den neuen Paddels beginnt
    # Erstellen eines Spiels von Spieler gegen AI (es wird also kein zweiter Spieler benötigt, das zweite Spieler Paddel wird von der AI gesteuert)
    def Start_PvAi_Game(self, player_1 : Player.Player):
        
        self.paddle_player_1 = Paddel.Paddel(player_1, self.screen_width - 20, self.screen_height/2, 5, self.screen_height)
        self.player_ai.score = 0
        # Zufälliges Wöhlen eines Paddle-Skins für den AI-Spieler
        self.player_ai.skin = self.player_ai.paddle_img[random.randint(0,4)]
        # entspricht hier einem AI Paddle
        self.paddle_player_2 = Paddel.Paddel(self.player_ai, 20 ,self.screen_width/2, 5, self.screen_height)
        #print(f"die Schwierigkeit der KI-Spieler beträgt: {self.paddle_player_2.difficulty}")
        
        self.general_setUp()
        
        return "PvAi"

    # Erstellen eines PvP Games. Für jeden Spieler wird ein neues Paddle erstellt
    def Start_PvP_Game(self, player_1 : Player.Player, player_2 : Player.Player):
        
        self.paddle_player_1 = Paddel.Paddel(player_1, self.screen_width - 20, self.screen_height/2, 5, self.screen_height)
        self.paddle_player_2 = Paddel.Paddel(player_2,20,self.screen_width/2, 5, self.screen_height)

        self.general_setUp()
        
        return "PvP"

    # Für jeden Spielzustand gleicher Erzeugungs-Prozess:
    def general_setUp(self):
        # Für jdes Spiel werden, abhängig der gewählten Einstellungen neue Bälle erzeugt
        self.paddle_group.empty()
        self.paddle_group.add(self.paddle_player_1)
        self.paddle_group.add(self.paddle_player_2)
        
        # Die Anzahl an gewünschten Bällen wird der Gruppe an Bällen hinzugefügt
        self.ball_group.empty()
        for x in range(self.game_modus_balls_count):
            ball = Ball.Ball('skins/Ball.png', self.screen_width/2, self.screen_height/2, self.paddle_group, self.screen_height, self.screen_width, self.screen)
            self.ball_group.add(ball)
            print(ball.active)
        
        # Wenn gewünscht, wird die Anzahl an Hindernissen initialisiert
        if self.game_modus_feature_obstacle_difficulty != 0:
            self.feature_obstacles_initialise()
        
        # Der Gametimer muss zurückgesetzt werden mit jeder neuen Spiel-Runde
        self.game_timer = 0