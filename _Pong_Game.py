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
# Version 1.1 Beta                          #
# @Felix Regler, @Tom Weber, @Gina G        #
# 14.02.2024                                #
# ######################################### #

# ######################################### #
# Initialisieren des Spiels - Grundzustand  #
# ######################################### #

# Allgemeines Setup
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
clock = pygame.time.Clock()

# Bildschirm - Screen - (Größe evtl anpassen)
os.environ["SDL_VIDEO_CENTERED"] = "1" 
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
#monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
#screen = pygame.display.set_mode((screen_width,screen_height))
screen = pygame.display.set_mode((screen_width -70, screen_height -120), pygame.RESIZABLE) ########fullscreen#####
pygame.display.set_caption('Pong')

# Spiel-Variablen - Stati
game_paused = False                                 # Gibt an, ob das Spiel pausiert ist
game_in_menue = False                               # Gibt an, ob man sich im Menü befindet
game_modus = "PvAi"                                 # Gibt den Spiel-Modus an !!!! Variable von GameState


# Zu reduzierende globale Variablen
# Farben und Bilder
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

# -------------------------------------------------------------------------
# Allgemeine Instanzen:

# Buttons:  !!!!! Zentrierung relativ zur Höhe !!!!!
resume_button = Button.Button(screen_width / 2 - resume_img.get_width() / 2, screen_height / 5, resume_img, 1)    #########optimierte Positionene############
options_button = Button.Button(screen_width / 2 - options_img.get_width() / 2, screen_height / 3.2, options_img, 1)  ###ungefäre Höhe abgeschätzt####
home_button = Button.Button(screen_width / 2 - home_img.get_width() / 2, screen_height / 2.3, home_img, 1)
quit_button = Button.Button(screen_width / 2 - quit_img.get_width() / 2, screen_height / 1.85, quit_img, 1)

change_button = Button.Button(screen_width / 1.33 - change_img.get_width() / 2, screen_height /6, change_img, 1)
skin_button = Button.Button(screen_width / 3.85 - skin_img.get_width() / 2, screen_height /6, skin_img, 1)
creategame_button = Button.Button(screen_width / 2 - creategame_img.get_width()/2, screen_height / 1.5, creategame_img,1)

start_button = Button.Button(screen_width / 2 - start_img.get_width()/2, screen_height / 1.5, start_img,1)
# -------------------------------------------------------------------------



# -------------------------------------------------------------------------
# Spiel-Objekte (evtl auch wo anders initialisieren / in Abhängigkeit des Speilmodi initialisieren)
# !!!!!! hier evtl alten Spielstand laden !!!!!! #
player_1 = Player.Player()
player_2 = Player.Player()
# --------------------------------------------------------------------------

# Spiel - Startzustand initialisieren: 
Game = GameState.GameState_Manager(screen)
#(Wird später im Menü ausgeführt):
game_modus = Game.Start_PvAi_Game(player_1) # !!!!!
# game_modus = Game.Start_PvP_Game(player_1, player_2)

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
            if event.key ==pygame.K_ESCAPE:
                game_paused = True

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
         
       
         
    # Hintergrund des Bildschirms
    screen.fill('#2F373F')

    ##### Player 1 Schrift erzeugen #####
 
    playerone_text = Text.Text(" -Player One- ", screen_width/6 , screen_height/6)  
    playertwo_text = Text.Text(" -Player Two- ", screen_width/1.5, screen_height/6)  
    ai_text = Text.Text(" -AI- ", screen_width/1.39, screen_height/6)  
    
    # ##### Main - Menü ##### #
    # Überprüfen auf Spielzustand:
    if game_paused == True and game_in_menue == True:
        #Pong und Blitz einfügen
        screen.blit(pong_img,(screen_width / 2 - pong_img.get_width()/2, screen_height / 8))
        screen.blit(lightning_img,(screen_width / 2 - lightning_img.get_width()/2, screen_height / 3))

        #Spieler 1 anzeigen
        playerone_text.blitnew(screen)
        playertwo_text.blitnew(screen)
    
        #startbutton einfügen
        if creategame_button.draw(screen):
            game_in_menue = False
            game_paused = False

        if change_button.draw(screen) == True:
            ai_text.blitnew(screen)

        if skin_button.draw(screen):
            pass

    
    
    # ##### Pausen - Menü ##### #
    # Überprüfen ob Spiel pausiert ist:
    if game_paused == True and game_in_menue == False:
        # Spiel Pausen-Menü
        if resume_button.draw(screen):
            game_paused = False
        if options_button.draw(screen):
            pass # !!!!!!! Lautstärke Einstellungen z.B. !!!!!!
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