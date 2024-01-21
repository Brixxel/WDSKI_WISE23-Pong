import pygame
import Ball

class Explosion(pygame.sprite.Sprite):
	"""
	Klasse für eine animierte Explosion

	"""
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		#ruft in diesem Fall die 5 Explosionen in dem Explosionsordner auf
		for num in range(1, 6):
			img = pygame.image.load(f"explosion/exp{num}.png") 
			img = pygame.transform.scale(img, (300, 300))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0


	def update(self, screen):

		explosion_speed = 6
		#updated die Explosionsanimation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#wenn die Animation fertig ist, wird der Animation index zurückgesetzt
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()
		self.rect.draw(screen)
