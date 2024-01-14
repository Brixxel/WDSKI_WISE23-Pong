import pygame, sys, random
# More imports...
import Player

# ######################################### #
# Version 1.1 Beta                          #
# @Felix Regler, @Tom Weber, @Gina G        #
# 14.02.2024                                #
# ######################################### #



# ######################################### #
# Initialisieren des Spiels - Grundzustands #
# ######################################### #


# ######################################### #
# Hier läuft das ganze Spiel                #
# ######################################### #

Game_status = "PvAi"

while True:
    
    # inputs
    for event in pygame.event.get():
        # genereller Abbruch:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Inputs - Abhängig von der Situation in der Ausführung (im Menü, oder währed des Spiels)

        # Spiel-Situation: Spieler gegen Ai
        if Game_status == "PvAi":
            ... # Input der Pfeiltasten -- Bewegung des Spieler Paddles