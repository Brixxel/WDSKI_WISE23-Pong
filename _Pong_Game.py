import pygame, sys, random
# More imports...
import Player
import Paddel
import AiPlayer 
import Button
import GameState
import Ball
import os
import Text

# ######################################### #
# Version 1.1                               #
# @Felix Regler, @Tom Weber, @Gina Grünen   #
# 21.01.2024                                #
# ######################################### #

# ######################################### #
# Initialisieren des Spiels - Grundzustand  #
# ######################################### #

# Allgemeines Setup
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
clock = pygame.time.Clock()


# Bildschirm - Screen 
os.environ["SDL_VIDEO_CENTERED"] = "1" 
screen_width_monitor = pygame.display.Info().current_w
screen_height_monitor = pygame.display.Info().current_h
screen_height = (screen_height_monitor - 100)
screen_width = (2)*(screen_height - 100)

#monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
#screen = pygame.display.set_mode((screen_width,screen_height))
screen = pygame.display.set_mode(( screen_width  , screen_height ), pygame.RESIZABLE) ########fullscreen#####
pygame.display.set_caption('Pong')

# Spiel-Variablen - (Start-Zustand, bei erst Initialisierung)
game_paused = True                                 # Gibt an, ob das Spiel pausiert ist
game_in_menue = True                               # Gibt an, ob man sich im Menü befindet
game_in_menue_create = False                       # Gibt an, ob man sich im Create-Menü befindet
game_modus = "PvAi"                                # Gibt den Spiel-Modus an

# ------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# Bilder importieren und zu Grafiken speichern
resume_img = pygame.image.load("grafics/button_resume.png").convert_alpha()
options_img = pygame.image.load("grafics/button_options.png").convert_alpha()
quit_img = pygame.image.load("grafics/button_quit.png").convert_alpha()
home_img = pygame.image.load("grafics/button_home.png").convert_alpha()
start_img = pygame.image.load("grafics/button_start.png").convert_alpha()
pong_img = pygame.image.load("grafics/PONG.png").convert_alpha()
lightning_img = pygame.image.load("grafics/lightning.png").convert_alpha()
change_img = pygame.image.load("grafics/button_change.png").convert_alpha()
skin_img = pygame.image.load("grafics/button_skins.png").convert_alpha()
creategame_img = pygame.image.load("grafics/button_creategame.png").convert_alpha()
# Für Buttons, die mehrere Zustände haben, wird ein Tupel aus allen möglichen Bildern eines Zustands angelegt:
getting_faster_imges = (pygame.image.load(r"grafics/button_getting_faster_01.png").convert_alpha() , pygame.image.load(r"grafics/button_getting_faster_02.png").convert_alpha())
increasingReflektion_imges = (pygame.image.load(r"grafics/button_harder_reflektion_01.png").convert_alpha() , pygame.image.load(r"grafics/button_harder_reflektion_02.png").convert_alpha())
moving_obstacle_imges = (pygame.image.load(r"grafics/button_obstacle_01.png").convert_alpha() , pygame.image.load(r"grafics/button_obstacle_02.png").convert_alpha() , 
                        pygame.image.load(r"grafics/button_obstacle_03.png").convert_alpha() , pygame.image.load(r"grafics/button_obstacle_04.png").convert_alpha() ,
                        pygame.image.load(r"grafics/button_obstacle_05.png").convert_alpha() , pygame.image.load(r"grafics/button_obstacle_06.png").convert_alpha() ,
                        pygame.image.load(r"grafics/button_obstacle_07.png").convert_alpha() , pygame.image.load(r"grafics/button_obstacle_08.png").convert_alpha())

paddle_img = [pygame.image.load("skins/Paddle_blue.png").convert_alpha(), pygame.image.load("skins/Paddle_green.png").convert_alpha(), 
            pygame.image.load("skins/Paddle_white.png").convert_alpha(), pygame.image.load("skins/Paddle_yellow.png").convert_alpha(), 
            pygame.image.load("skins/Paddle.png").convert_alpha()]

multiball_img = (pygame.image.load(r"grafics/button_multiball_01.png").convert_alpha(),pygame.image.load(r"grafics/button_multiball_02.png").convert_alpha(),
                pygame.image.load(r"grafics/button_multiball_03.png").convert_alpha(),pygame.image.load(r"grafics/button_multiball_04.png").convert_alpha(),)
playerone_img = pygame.image.load("grafics/player_one.png").convert_alpha()
player_img = (pygame.image.load("grafics/player_two.png").convert_alpha(),  pygame.image.load("grafics/ai_player.png").convert_alpha())
blöckeanzahl_img = pygame.image.load("grafics/anzahl_blöcke.png").convert_alpha()
ai_imgs = (pygame.image.load(r"grafics/button_easy.png").convert_alpha(), pygame.image.load(r"grafics/button_medium.png").convert_alpha(),pygame.image.load(r"grafics/button_hard.png").convert_alpha())

# ------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Allgemeine Instanzen:
# Buttons im Pausenmenü: 
resume_button = Button.Button(screen_width / 2 - resume_img.get_width() / 2, 8 * screen_height / 20, resume_img, 1)
home_button = Button.Button(screen_width / 2 - home_img.get_width() / 2, 10 * screen_height / 20, home_img, 1)
quit_button = Button.Button(screen_width / 2 - quit_img.get_width() / 2, 12 * screen_height / 20, quit_img, 1)
#Buttons im main Menü:
change_button = Button.Button(screen_width / 20 * 17 - change_img.get_width() / 2, 1 * screen_height / 20, change_img, 1)
skin_button = Button.Button(screen_width / 20 * 3 - skin_img.get_width() / 2, 4 * screen_height /20, skin_img, 1)
skin2_button = Button.Button(screen_width / 20 * 17 - skin_img.get_width() / 2, 4 * screen_height /20, skin_img, 1)
creategame_button = Button.Button(screen_width / 20 * 10 - creategame_img.get_width(), 14 * screen_height / 20, creategame_img, 2)
paddle_button = Button.Button(screen_width / 20 * 3, 8 * screen_height / 20, paddle_img[4],1)
paddle2_button = Button.Button(screen_width / 20 * 17, 8 * screen_height / 20, paddle_img[4],1)
playerone_button = Button.Button(screen_width / 20  - playerone_img.get_width() / 2, (3/5) * screen_height / 20, playerone_img, 5)
playertwo_ai_button = Button.Button(screen_width / 20 * 15 - player_img[1].get_width() / 2, (3/5) * screen_height / 20, player_img[1], 5)
ai_button = Button.Button(screen_width / 20 * 16 - ai_imgs[1].get_width() / 2, 9 * screen_height / 20, ai_imgs[0], 4)
# Buttons im create Game Menü:
getting_faster_button = Button.Button(screen_width / 2 - (resume_img.get_width()/2)*3, screen_height -  5 * screen_height / 12, getting_faster_imges[0] , 4)
increasing_Reflektion_button = Button.Button(screen_width / 2 - (resume_img.get_width() / 2)*3, screen_height -  4 * screen_height / 12, increasingReflektion_imges[0] , 4)
moving_obstacle_button = Button.Button(screen_width / 2 - (resume_img.get_width() / 2)*3, screen_height -  3 * screen_height / 12, moving_obstacle_imges[0] , 4)
obstacle_counter = ''
multiball_button = Button.Button(screen_width / 2 - (resume_img.get_width() / 2)*3, screen_height -  2 * screen_height / 12, multiball_img[0] , 4)
start_button = Button.Button(screen_width / 2 - start_img.get_width()/2, screen_height -  9 * screen_height / 12, start_img ,1)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Spieler-Objekte
player_1 = Player.Player()
player_2 = Player.Player()
player_Ai = AiPlayer.AIPlayer()
Game = GameState.GameState(screen, player_Ai)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# ######################################### #
# Spiel - Loop                              #
# ######################################### #

run = True
while run:

    # Inputs
    for event in pygame.event.get():
        # genereller Abbruch:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Menü aufrufen und Spiel pausieren?:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = True
            
            # Im Menü um Anzahl an Hindernissen anzugeben:
            
            if event.key == pygame.K_BACKSPACE:
                obstacle_counter = obstacle_counter[:-1]
            else:
                obstacle_counter += event.unicode
            
        # -------------------------------------------------------------------------------------- #
        # Inputs - Abhängig von der Situation in der Ausführung (im Menü, oder währed des Spiels)

        # Spiel-Typ: Spieler gegen Ai
        if game_modus == "PvAi":
            #Player 1: (wird mit Pfeiltasten gesteuert)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Game.paddle_player_1.movement -= Game.paddle_player_1.speed
                if event.key == pygame.K_DOWN:
                    Game.paddle_player_1.movement += Game.paddle_player_1.speed
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    Game.paddle_player_1.movement += Game.paddle_player_1.speed
                if event.key == pygame.K_DOWN:
                    Game.paddle_player_1.movement -= Game.paddle_player_1.speed
            #AI Player wird von Ai gesteuert, daher keine weiteren Inputs benötig
        
        # # Spiel-Typ: Spieler gegen Spieler
        if game_modus == "PvP":                         # Tasten Belegung / Events für PvP
            #Player 1: (wird mit Pfeiltasten gesteuert)
            #Player 2: (wird mit W- und S-Taste gesteuert)
            if event.type == pygame.KEYDOWN:
                # Player 1:
                if event.key == pygame.K_UP:
                    Game.paddle_player_1.movement -= Game.paddle_player_1.speed
                if event.key == pygame.K_DOWN:
                    Game.paddle_player_1.movement += Game.paddle_player_1.speed
                #Player 2:
                if event.key == pygame.K_w:
                    Game.paddle_player_2.movement -= Game.paddle_player_2.speed
                if event.key == pygame.K_s:
                    Game.paddle_player_2.movement += Game.paddle_player_2.speed                
                    
            if event.type == pygame.KEYUP:
                # Player 1:
                if event.key == pygame.K_UP:
                    Game.paddle_player_1.movement += Game.paddle_player_1.speed
                if event.key == pygame.K_DOWN:
                    Game.paddle_player_1.movement -= Game.paddle_player_1.speed
                # Player 2:
                if event.key == pygame.K_w:
                    Game.paddle_player_2.movement += Game.paddle_player_2.speed
                if event.key == pygame.K_s:
                    Game.paddle_player_2.movement -= Game.paddle_player_2.speed                                  
        
            # ------------------------------------------------------------------------------------------------------- #
            #           User Input in Menu         
            
    # Hintergrund des Bildschirms
    screen.fill('#2F373F')
    
    # --------------------------------------------------------------------------------------------------------------- #
    #                                                    MENÜS                                                        #
    # --------------------------------------------------------------------------------------------------------------- #
    
    # ---------------------------------------------   Main - Menü   ------------------------------------------------- #
    # -------------------                         Spieler-Auswahl-Menü                     -------------------------- #
    """ 
    In diesem Menü müssen folgende Eigenschaften vom Spieler eingestellt werden:
            1.) PvP oder PvAi
            2.) Ai Schweirigkeit
            3.) Skin von Spieler 1 und 2 (wenn keine Ai)       
    """ 
    # Überprüfen auf Spiel- / Menü-zustand:
    if game_paused == True and game_in_menue == True and game_in_menue_create == False:
        
        #Pong, Paddle und Blitz einfügen
        screen.blit(pong_img,(screen_width / 2 - pong_img.get_width()/2, screen_height / 8))
        screen.blit(lightning_img,(screen_width / 2 - lightning_img.get_width()/2, screen_height / 3))
        paddle_button.draw(screen)
        
        #Player One und Two einfügen
        playerone_button.draw(screen)
        playertwo_ai_button.draw(screen)
    
        #Create Game Button einfügen 
        if creategame_button.draw(screen):
            # Ein neues Spiel wird erstellt und das alte somit "gelöscht"
            current_time = pygame.time.get_ticks()
            Game = GameState.GameState(screen, player_Ai)
            # Jetzt wird im nächsten Menu die Zustände des Spiel eingestellt
            game_in_menue_create = True
        

        # change Button zum AI oder PLayer auswählen
        if change_button.draw(screen) == True:
            change_button.counter += 1
            playertwo_ai_button.change_picture(player_img[change_button.counter % len(player_img)])
            if change_button.counter % 2 == 0:
                game_modus = "PvP"

            else:
                game_modus = "PvAi"      

        # Button zum skins bei Player2 aussuchen
        if game_modus == "PvP":
            paddle2_button.draw(screen)
            if skin2_button.draw(screen) == True:
                skin2_button.counter += 1
                paddle2_button.change_picture(paddle_img[skin2_button.counter % len(paddle_img)])
                player_2.skin = paddle_img[skin2_button.counter % len(paddle_img)]
            score_person2 = Text.Text(f"score: {player_2.score}", screen_width/20 * 15 , 15 * screen_height/20)
            score_person2.blitnew(screen)
            player_2.update_highscore()        
            highscore_person2 = Text.Text(f"highscore: {player_2.highscore}", screen_width/20 * 15 , 16 * screen_height/20)
            highscore_person2.blitnew(screen) 

        # Button zum Schwierigkeitsgrad einstellen der AI
        if game_modus == "PvAi":
            if ai_button.draw(screen):
                ai_button.counter += 1
                ai_button.change_picture(ai_imgs[ai_button.counter % len(ai_imgs)])
                # Anpassen der Schwierigkeit des AI-Spielers 
                player_Ai.difficulty = ai_button.counter % len(ai_imgs) 

        # Button zum skins bei Player1 aussuchen
        if skin_button.draw(screen) == True:
            skin_button.counter += 1
            paddle_button.change_picture(paddle_img[skin_button.counter % len(paddle_img)])
            player_1.skin = paddle_img[skin_button.counter % len(paddle_img)]

        #Score und Highscore einblenden
        score_person1 = Text.Text(f"score: {player_1.score}", screen_width/20 * 1 , 15 * screen_height/20)
        score_person1.blitnew(screen)
        player_1.update_highscore()   
        highscore_person1 = Text.Text(f"highscore: {player_1.highscore}", screen_width/20 * 1, 16 * screen_height/20)
        highscore_person1.blitnew(screen)    



    # -------------------                        Create Game Menü                     -------------------------- #
    """ In diesem Menü müssen folgende Eigenschaften vom Spieler eingestellt werden:
            1.) Block-Spielmodus            (Keine Blöcke, statische Blöcke, sich zunehmend teleportierende Blöcke, sich bewegende Blöcke)
                Anzahl an Hindernissen      (User-Typer-Input)
            2.) Geschwindigkeits Änderung   (An / Aus)
            3.) Reflektionsverstärkung      (An / Aus)
            4.) Multiball                   (An / Aus)
    """ 
    # Überprüfen auf Spiel- / Menü-zustand:
    if game_paused == True and game_in_menue == True and game_in_menue_create == True:
        
        # Abfrage über den Spiel-Modus: Ball wird schneller
        if getting_faster_button.draw(screen) == True:
            # Der Knopf wurde gedrückt, daher die Erhöhung des Counters
            getting_faster_button.counter += 1
            # Abhängig von der Anzahl an Drückungen kann bestimmt werden, in welchen Modus der Spieler getoggelt ist, so wird das Bild bestimmt:
            getting_faster_button.change_picture(getting_faster_imges[getting_faster_button.counter % len(getting_faster_imges)])

        # Abfrage über Spiel-Modus: Ball wird härter reflektiert
        if increasing_Reflektion_button.draw(screen) == True:
            # Der Knopf wurde gedrückt, daher die Erhöhung des Counters
            increasing_Reflektion_button.counter += 1
            # Abhängig von der Anzahl an Drückungen kann bestimmt werden, in welchen Modus der Spieler getoggelt ist, so wird das Bild bestimmt:
            increasing_Reflektion_button.change_picture(increasingReflektion_imges[increasing_Reflektion_button.counter % len(increasingReflektion_imges)])

        # Abfrage nach geünschter Anzahl von Hindernissen:
        text_count_obstacle = Text.Text(f"Geben Sie die Anzahl an Hindernissen ein: {obstacle_counter}", screen_width - 5.15*screen_width/8, screen_height -  6 * screen_height / 12)
        if moving_obstacle_button.counter % len(moving_obstacle_imges) != 0: 
            text_count_obstacle.blitnew(screen)
        
        # Abfrage über Spiel-Modus: Hindernisse!!!
        if moving_obstacle_button.draw(screen) == True:
            # Der Knopf wurde gedrückt, daher die Erhöhung des Counters
            moving_obstacle_button.counter += 1
            # Abhängig von der Anzahl an Drückungen kann bestimmt werden, in welchen Modus der Spieler getoggelt ist, so wird das Bild und daraus später der übergebene Wert bestimmt:
            moving_obstacle_button.change_picture(moving_obstacle_imges[moving_obstacle_button.counter % len(moving_obstacle_imges)])
            
            if moving_obstacle_button.counter % len(moving_obstacle_imges) > 0:
                text_count_obstacle.remove()
            
        if multiball_button.draw(screen):
            # Der Knopf wurde gedrückt, daher die Erhöhung des Counters
            multiball_button.counter += 1
            # Abhängig von der Anzahl an Drückungen kann bestimmt werden, in welchen Modus der Spieler getoggelt ist, so wird das Bild bestimmt:
            multiball_button.change_picture(multiball_img[multiball_button.counter % len(multiball_img)])
            pass      
            
        
        
        if start_button.draw(screen) == True:
            # Das Spiel befindet sich nicht mehr im Menü, somit müssen die Menü-Methoden nciht länger auzsgeführt werden
            game_paused, game_in_menue, game_in_menue_create = False,False,False
            
            if increasing_Reflektion_button.counter % len(increasingReflektion_imges) == 0:
                Game.game_modus_feature_increasingReflektion = False
            elif increasing_Reflektion_button.counter % len(increasingReflektion_imges) == 1:
                Game.game_modus_feature_increasingReflektion = True

            
            if getting_faster_button.counter % len(getting_faster_imges) == 0:
                Game.game_modus_feature_increasingSpeed = False
            elif getting_faster_button.counter % len(getting_faster_imges) == 1:
                Game.game_modus_feature_increasingSpeed = True

            
            Game.game_modus_feature_obstacle_difficulty = moving_obstacle_button.counter % len(moving_obstacle_imges)
            Game.game_modus_balls_count =  2 ** (multiball_button.counter % len(multiball_img))
            
            try:
                Game.game_modus_feature_obstacle_count = int(obstacle_counter)

                obstacle_counter = ''
            except:
                print("Sie haben keine Valide Anzahl eingegeben")
                Game.game_modus_feature_obstacle_count = 0
                obstacle_counter = ''
            
            print(f"gewählte Spiel Modi: getting faster: {Game.game_modus_feature_increasingSpeed}; harder Reflektion:  {Game.game_modus_feature_increasingReflektion}; Hindernisse: {Game.game_modus_feature_obstacle_difficulty}")
            
            #Game im jeweiligen Modus starten und Highscore updaten
            if game_modus == "PvAi":
                player_1.update_highscore()
                player_2.update_highscore()
                player_1.score = 0
                player_2.score = 0
                Game.Start_PvAi_Game(player_1)
            elif game_modus == "PvP":
                player_1.update_highscore()
                player_2.update_highscore()
                player_1.score = 0
                player_2.score = 0
                Game.Start_PvP_Game(player_1, player_2)    
    
    
    
    # ##### Pausen - Menü ##### #
    # Überprüfen ob Spiel pausiert ist:
    if game_paused == True and game_in_menue == False:
        # Spiel Pausen-Menü
        if resume_button.draw(screen):
            game_paused = False
        if home_button.draw(screen):
            game_in_menue = True
        if quit_button.draw(screen):
            run = False
        
                    
    # ##### Wenn gespielt wird, für alle Spiel Modi und Spiel Typen: ##### #
    if game_paused == False and game_in_menue == False:
        Game.run_game()
    
    # Rendering
    pygame.display.flip()
    clock.tick(60)