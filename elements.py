import pygame
from pygame.locals import *
from gamelib import SimpleGame


class Tank(object):
	def __init__(self, pos, speed, hp):
		(self.x, self.y) = pos
		(self.vx, self.vy) = speed
		self.hp = hp
		self.meteor_image = pygame.image.load('enemy.png')
		
	def move(self, delta_t,player):
		self.y += 1
		if player.x >= self.x:
			self.x += self.vx
		elif player.x < self.x:
			self.x -= self.vx
		if self.y > 30:
			self.y = 30
	def render(self, display):
		pos = (int(self.x),int(self.y))
		display.blit(self.meteor_image, (self.x-19, self.y-25))

###################################
class Player(object):
	
	def __init__(self,  pos, height=48):
		(self.x, self.y) = pos
		self.height = height
		self.ship_image = pygame.image.load('mytank.png')

	def move_left(self):
		self.x -= 10
		if self.x < 0:
			self.x = 0

	def move_right(self):
		self.x += 10
		if self.x > 640:
			self.x = 640
		
	def render(self, display):
		display.blit(self.ship_image, (self.x-19, self.y-25))

###################################
class Bullet(object):
	THICKNESS = 5
	
	def __init__(self, pos, color, speed, height=15):
		(self.x, self.y) = pos
		(self.vx, self.vy) = speed
		self.height = height
		self.color = color
		self.missile_image = pygame.image.load('mymissile.png')
		
	def move(self, delta_t, player):
		global score, game_over
		
		self.x += self.vx*delta_t
		self.y -= self.vy*delta_t
	
	def render(self, display):
		display.blit(self.missile_image, (self.x-5, self.y-8))

###################################
class EnemyBullet(Bullet):
	def __init__(self, pos, color, speed, height=15):
		(self.x, self.y) = pos
		(self.vx, self.vy) = speed
		self.height = height
		self.color = color
		self.missileE_image = pygame.image.load('missileE.png')
		
	def move(self, delta_t, player):
		global score, game_over
		self.x += self.vx*delta_t
		self.y += self.vy*delta_t
		
	def render(self, display):
		display.blit(self.missileE_image, (self.x-5, self.y-8))

###################################

class Life(object):
	
	def __init__(self, pos):	
		(self.x, self.y) = pos
		self.life_image = pygame.image.load('heart.png')

	def render(self, display):
		pos = (int(self.x),int(self.y))
		display.blit(self.life_image, (self.x-10, self.y-10))