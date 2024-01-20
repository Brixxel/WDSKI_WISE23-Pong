#WDSKI_WISE23-Pong
### PONG GAME ###
Pong - Pygame Projekt

# Projektbeschreibung #
Dieses Projekt wurde im Rahmen des Programmierkurses an der Dualen Hochschule Mannheimim ersten Semseter des Studiengangs Data-Sience und künstliche Intiligenz entwickelt. Die Aufgabe bestand darin, eine Version des klassischen Spiels Pong zu implementieren. Dies sollte mithilfe der Pygame-Bibliothek in Python geschehen. Ziel war es, grundlegende Konzepte der Pygame-Bibliothek zu verstehen und gleichzeitig das klassische Pong-Spiel um eigene kreative Elemente zu erweitern.

# Teammitglieder #
Tom Weber			Matrikel: 7643968
Gina Grünen			Matrikel: 5063426
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
    - Der Skin der AI wird zufällig generiert.
  Spielmodifikatoren:
    - Multiball-Modus: Mehrere Bälle werden gleichzeitig im Spiel sein, was zu einem chaotischen, aber spaßigen Erlebnis führt.
    - Hindernisse: Statische, teleportierende und sich bewegende Hindernisse wurden hinzugefügt. Beim Spawnen wird Rücksicht auf den Spawnbereich des Balls genommen.
    - Härtere Ballreflexion: Die Reflexion des Balls wird im Laufe der Zeit anspruchsvoller.
    - Geschwindigkeitserhöhung: Die Geschwindigkeit des Balls nimmt im Laufe der Zeit zu, um das Spiel intensiver zu gestalten.

# Design #
Wir haben uns dafür entschieden, ein pixel haftes Design und Neonfarben für unser Pong-Spiel auszuwählen, um eine bestimmte ästhetische Atmosphäre zu schaffen und die Spielerfahrung zu verbessern. Hier sind einige Gründe, warum wir diese Designelemente gewählt haben:
  -Einfachheit und Klarheit: Unser Fokus liegt auf einfacher und klarer Gestaltung. Das reduzierte Design ermöglicht es den Spielern, sich auf das Wesentliche zu konzentrieren, ohne von komplexen Details abgelenkt zu werden.
  -Futuristisches Gefühl mit Neonfarben: Neon Farben vermitteln ein futuristisches und lebendiges Gefühl. Die kräftigen Farben machen unser Spiel dynamischer und aufregender, was besonders gut zu einem Pong-Spiel passt.
  -Einzigartige Markenkennzeichnung: Die Kombination aus pixeligen Grafiken und Neonfarben verleiht unserem Spiel eine unverwechselbare Identität. Spieler können unser Spiel leicht erkennen und sich daran erinnern.
Unsere Designentscheidungen basieren auf unseren persönlichen Präferenzen, dem gewünschten Spielerlebnis und dem Stil, den wir für unser Spiel schaffen möchten.

# Quellen #
https://www.pixilart.com/
https://www.python-lernen.de/
https://pythonprogramming.net/
https://www.geeksforgeeks.org/