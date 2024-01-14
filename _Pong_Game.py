import pygame, sys, random
# More imports...
import Player
import Paddel
import AiPlayer
import Button

# ######################################### #
# Version 1.1 Beta                          #
# @Felix Regler, @Tom Weber, @Gina G        #
# 14.02.2024                                #
# ######################################### #

# ######################################### #
# Initialisieren des Spiels - Grundzustands #
# ######################################### #

# Allgemeines Setup
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
clock = pygame.time.Clock()

# Bildschirm - Screen - (Größe evtl anpassen)
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Spiel-Variablen - Stati
game_paused = False
game_modus = "PvAi"

# Zu reduzierende globale Variablen
# Farben und Bilder

resume_img = pygame.image.load("grafics/button_resume.png").convert_alpha()

# Spiel-Objekte (evtl auch wo anders initialisieren / in Abhängigkeit des Speilmodi initialisieren)
# !!!!!! hier evtl alten Spielstand laden !!!!!! #
# player_1 = Player.Player()
# player_2 = Player.Player()

# Allgemeine Instanzen:
resume_button = Button.Button(304, 125, resume_img, 1)

# paddle_player_1 = 



# ######################################### #
# Spiel - Loop                              #
# ######################################### #

while True:
    
    # Überprüfen ob Spiel im Menü ist
    if game_paused == True:
        # Spiel Menü
        resume_button.draw(screen)
    
    # Inputs
    for event in pygame.event.get():
        # genereller Abbruch:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Menü aufrufen und Spiel pausieren?:
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_ESCAPE:
                print(f"pause {game_paused}")
                game_paused = True

        # -------------------------------------------------------------------------------------- #
        # Inputs - Abhängig von der Situation in der Ausführung (im Menü, oder währed des Spiels)

        # # Spiel-Situation: Spieler gegen Ai
        # if game_modus == "PvAi":
        # # Input der Pfeiltasten -- Bewegung des Spieler Paddles
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_UP:
        #             player.movement -= player.speed
        #         if event.key == pygame.K_DOWN:
        #             player.movement += player.speed
                    
        #     if event.type == pygame.KEYUP:
        #         if event.key == pygame.K_UP:
        #             player.movement += player.speed
        #         if event.key == pygame.K_DOWN:
        #             player.movement -= player.speed
                    
    # Hintergrund
    screen.fill('#2F373F')
    
    # Rendering
    pygame.display.flip()
    clock.tick(120)
    