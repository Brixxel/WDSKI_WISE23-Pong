#WDSKI_WISE23-Pong
# PONG GAME #

## Projektbeschreibung ##
Dieses Projekt wurde im Rahmen des Programmierkurses an der Dualen Hochschule Mannheimim ersten Semseter des Studiengangs Data-Sience und künstliche Intiligenz entwickelt. Die Aufgabe bestand darin, eine Version des klassischen Spiels Pong zu implementieren. Dies sollte mithilfe der Pygame-Bibliothek in Python geschehen. Ziel war es, grundlegende Konzepte der Pygame-Bibliothek zu verstehen und gleichzeitig das klassische Pong-Spiel um eigene kreative Elemente zu erweitern.

## Teammitglieder ##
Tom Weber			Matrikel: 
Gina Grünen			Matrikel: 
Felix Regler			Matrikel: 

## Installationsanleitung ##
Bevor Sie das Pong-Spiel starten können, stellen Sie sicher, dass Python und Pygame auf Ihrem System installiert sind. Falls Sie Pygame noch nicht installiert haben, können Sie es mit dem folgenden Befehl in Ihrer virtuellen Umgebung installieren.

pip install pygame

Nach der Installation können Sie das Spiel mit dem folgenden Befehl starten:

python _Pong_Game.py


## Spielanleitung ##

  Spieler 1 (rechts): 
    Steuerung mit den Pfeiltasten nach oben und unten.
  Spieler 2 (links): 
    Steuerung mit den Tasten W (nach oben) und S (nach unten). 

Das Ziel ist es, den Ball am Gegenspieler vorbeizuspielen und Punkte zu erzielen.

## Funktionen und Spielmodi ##
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
    
## Design:
Wir haben uns dafür entschieden, ein pixel haftes Design und Neonfarben für unser Pong-Spiel auszuwählen, um eine bestimmte ästhetische Atmosphäre zu schaffen und die Spielerfahrung zu verbessern. Hier sind einige Gründe, warum wir diese Designelemente gewählt haben:

- Einfachheit und Klarheit: Unser Fokus liegt auf einfacher und klarer Gestaltung. Das reduzierte Design ermöglicht es den Spielern, sich auf das Wesentliche zu konzentrieren, ohne von komplexen Details abgelenkt zu werden.
- Futuristisches Gefühl mit Neonfarben: Neon Farben vermitteln ein futuristisches und lebendiges Gefühl. Die kräftigen Farben machen unser Spiel dynamischer und aufregender, was besonders gut zu einem Pong-Spiel passt.
- Einzigartige Markenkennzeichnung: Die Kombination aus pixeligen Grafiken und Neonfarben verleiht unserem Spiel eine unverwechselbare Identität. Spieler können unser Spiel leicht erkennen und sich daran erinnern.

Um dem Pixeldesign gerecht zu werden und eine zusätzliche kreative Note einzuführen, haben wir uns zudem dafür entschieden, Minecraft-Blöcke als Obstacles zu verwenden. 
Unsere Designentscheidungen basieren auf unseren persönlichen Präferenzen, dem gewünschten Spielerlebnis und dem Stil, den wir für unser Spiel schaffen möchten.

## Soundeffekte: 
Wir haben bewusst einfache Pixelklänge für die Soundeffekte unseres Pong-Spiels gewählt, um eine gezielte akustische Atmosphäre zu schaffen und die Spielerfahrung zu optimieren. 

- Passendes Design: Die Auswahl einfacher Pixelklänge wurde strategisch getroffen, um sicherzustellen, dass die Klangästhetik harmonisch mit dem Gesamtdesign des Spiels interagiert. Diese Entscheidung trägt dazu bei, eine ansprechende Spielerfahrung zu schaffen.
- Vermeidung von Überlagerungen: Die Priorität lag darin, größere Soundüberlagerungen zu vermeiden. Durch die Nutzung einfacher und kurzer Klänge minimieren wir potenzielle Störungen und ermöglichen den Spielern, sich voll und ganz auf das Gameplay zu konzentrieren, ohne von unerwünschten akustischen Ablenkungen beeinträchtigt zu werden.
- Countdown-Soundüberlegungen: Obwohl wir den Wunsch hatten, einen Sound zum Countdown hinzuzufügen, haben wir uns letztendlich dagegen entschieden, insbesondere im Kontext der Multiballspielvariante. Diese Entscheidung wurde getroffen, um unnötige Soundüberlagerungen zu vermeiden und das Gesamterlebnis für die Spieler nicht zu beeinträchtigen.


## Quellen:
- Allgemeines:
- - https://www.pixilart.com/
- - https://www.python-lernen.de/
- - https://pythonprogramming.net/
- - https://www.pygame.org/docs/ref/draw.html
- - https://www.youtube.com/watch?v=Qf3-aDXG8q4
- - https://www.geeksforgeeks.org/returning-a-function-from-a-function-python/
- - https://mimo.org/glossary/python
- - https://stackoverflow.com/questions/12738031/creating-a-new-function-as-return-in-python-function
- - https://docs.python.org/3/tutorial/errors.html
- - https://www.geeksforgeeks.org/
- Explosion: 
- - https://youtu.be/d06aVDzOfV8?si=WFE4O6DN88ly1rx5

- Random Image: 
- - https://stackoverflow.com/questions/65187875/how-do-i-get-a-random-image-from-a-folder-python

- Sounds: 
- - https://youtu.be/3Yhhzflmxfs?si=gqRBs6Ha99mPmsAa
- - https://creatorassets.com/a/8bit-explosion-sound-effects
- - https://pixabay.com/sound-effects/one-beep-99630/
- - https://pixabay.com/sound-effects/game-start-6104/

- Blöcke: 
- - https://www.pngkey.com/maxpic/u2e6q8t4y3t4w7w7/
- - https://www.vectorstock.com/royalty-free-vector/pixel-minecraft-style-land-block-background-vector-36579671
- - https://www.pixilart.com/art/minecraft-tnt-block-e69ed81d12df81a
- - https://www.pixilart.com/art/minecraft-stone-block-f1ec53c57ac5a99
- - https://www.pixilart.com/art/creeper-face-95dd8f9417de36a?ft=user&ft_id=82300
- - https://www.pixilart.com/art/minecraft-skeleton-8180be903f3d75c?ft=user&ft_id=82300+#