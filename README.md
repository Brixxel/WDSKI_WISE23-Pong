#WDSKI_WISE23-Pong
### PONG GAME ###
Pong - Pygame Projekt

# Projektbeschreibung #
Dieses Projekt wurde im Rahmen des Programmierkurses an der Dualen Hochschule Mannheimim ersten Semseter des Studiengangs Data-Sience und künstliche Intiligenz entwickelt. Die Aufgabe bestand darin, eine Version des klassischen Spiels Pong zu implementieren. Dies sollte mithilfe der Pygame-Bibliothek in Python geschehen. Ziel war es, grundlegende Konzepte der Pygame-Bibliothek zu verstehen und gleichzeitig das klassische Pong-Spiel um eigene kreative Elemente zu erweitern.

# Teammitglieder #
Tom Weber			Matrikel: 
Gina Grünen			Matrikel: 
Felix Regler			Matrikel: 

# Installationsanleitung #
Bevor Sie das Pong-Spiel starten können, stellen Sie sicher, dass Python und Pygame auf Ihrem System installiert sind. Falls Sie Pygame noch nicht installiert haben, können Sie es mit dem folgenden Befehl in Ihrer virtuellen Umgebung installieren.

pip install pygame

Nach der Installation können Sie das Spiel mit dem folgenden Befehl starten:

python _Pong_Game.py


# Spielanleitung #

  Spieler 1 (rechts): 
    Steuerung mit den Pfeiltasten nach oben und unten.
  Spieler 2 (links): 
    Steuerung mit den Tasten W (nach oben) und S (nach unten). 

Das Ziel ist es, den Ball am Gegenspieler vorbeizuspielen und Punkte zu erzielen.

# Funktionen und Spielmodi #
Unsere erweiterte Pong-Version enthält die folgenden Funktionen und Spielmodi:
  Spielmodi:

    - Player vs. Player (PvP): Klassisches Pong-Spiel, bei dem zwei menschliche Spieler gegeneinander antreten.

    - Player vs. AI (PvAI): Einzelspielermodus gegen eine computergesteuerte KI. Die KI passt sich dem Schwierigkeitsgrad an.

  Spieleranpassungen:

    - Skin-Wahl des einen Spielers: Ein Spieler kann seinen Paddle-Skin aus verschiedenen verfügbaren Optionen auswählen.

  Spielmodifikatoren:

    - Multiball-Modus: Mehrere Bälle werden gleichzeitig im Spiel sein, was zu einem chaotischen, aber spaßigen Erlebnis führt.

    - Hindernisse: Statische, teleportierende und sich bewegende Hindernisse wurden hinzugefügt. Beim Spawnen wird Rücksicht auf den Spawnbereich des Balls genommen.

    - Härtere Ballreflexion: Die Reflexion des Balls wird im Laufe der Zeit anspruchsvoller.

    - Geschwindigkeitserhöhung: Die Geschwindigkeit des Balls nimmt im Laufe der Zeit zu, um das Spiel intensiver zu gestalten.
    
