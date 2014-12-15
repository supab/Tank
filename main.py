import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import Player,Tank, Bullet, Life,EnemyBullet
import random

class TankWar(SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	COLOR = [pygame.Color('red'), pygame.Color('green'), pygame.Color('blue'), pygame.Color('yellow')]
	YELLOW = pygame.Color('yellow')
	RED = pygame.Color('red')
	
	def __init__(self):
		super(TankWar, self).__init__('Tank Breaker', TankWar.BLACK)
		self.player = Player(pos=(self.window_size[0]/2, self.window_size[1]-25))
		self.tanks = [Tank( pos=(random.randrange(0,640),-25), speed=(1, 0), hp=10)]
		self.bullets = []
		self.enemybullets = []
		self.score = 0
		self.life = 5
		self.lives = [Life(pos=(160,20)), Life(pos=(140,20)), \
						Life( pos=(120,20)), Life(pos=(100,20)), \
						Life(pos=(80,20))]
		
	
	def init(self):
		super(TankWar, self).init()
		self.render_score()
		self.render_life()

	def render(self, display):
		self.player.render(display)
		
		for tank in self.tanks:
			tank.render(display)

		for bullet in self.bullets:
			bullet.render(display)

		for enemybullet in self.enemybullets:
			enemybullet.render(display)

		for life in self.lives:
			life.render(display)

		display.blit(self.score_image, (460,10))
		display.blit(self.life_image, (10,10))

	def update(self):
		if self.is_key_pressed(K_LEFT):
			self.player.move_left()
		if self.is_key_pressed(K_RIGHT):
			self.player.move_right()
		if self.is_key_pressed(K_SPACE) and pygame.time.get_ticks()%3 == 0 :
			self.newBullet = Bullet(pos=(self.player.x, self.player.y-25), color=TankWar.YELLOW, speed=(0,400))
			self.bullets.append(self.newBullet)


		for tank in self.tanks:
			tank.move(1./self.fps,self.player)
			if self.player.x+25>= tank.x > self.player.x-25:
				self.newEnemyBullet = EnemyBullet(pos=(self.player.x, 30), color=TankWar.YELLOW, speed=(0,400))
				self.enemybullets.append(self.newEnemyBullet)

		for enemybullet in self.enemybullets:
			enemybullet.move(1./self.fps, self.player)
			if enemybullet.y >=640 :
				self.enemybullets.remove(enemybullet)

		for bullet in self.bullets:
			bullet.move(1./self.fps, self.player)
			if bullet.y <=0 :
				self.bullets.remove(bullet)
		if pygame.time.get_ticks()/1000 <=20:
			if pygame.time.get_ticks()%100 == 0:
				self.newtank = Tank(pos=(random.randrange(0,640),-20), speed=(1, 0), hp=10)
				self.tanks.append(self.newtank)

		elif 20 < pygame.time.get_ticks()/1000 <=40:
			if pygame.time.get_ticks()%80 == 0:
				self.newtank = Tank( pos=(random.randrange(0,640),-20), speed=(1.2,0), hp=15)
				self.tanks.append(self.newtank)

		elif 40 < pygame.time.get_ticks()/1000 <=60:
			if pygame.time.get_ticks()%60 == 0:
				self.newtank = Tank( pos=(random.randrange(0,640),-20), speed=(1.5,0), hp=20)
				self.tanks.append(self.newtank)

		else :
			if pygame.time.get_ticks()%40 == 0:
				self.newtank = Tank( pos=(random.randrange(0,640),-20), speed=(1.7,0), hp=25)
				self.tanks.append(self.newtank)

		for tank in self.tanks:
			for bullet in self.bullets:
				if (tank.y-25 < bullet.y < tank.y+25) and (tank.x-19 < bullet.x < tank.x+19):
					self.bullets.remove(bullet)
					tank.hp -= 1
					if (tank.hp == 0):
						self.tanks.remove(tank)
						self.score += 1
						self.render_score()
		for enemybullet in self.enemybullets:
			if self.player.x-19<enemybullet.x <self.player.x+19 and self.player.y-25<enemybullet.y <self.player.y+25 :
				self.enemybullets.remove(enemybullet)
				self.life -= 1
				self.render_life()
				self.lives.remove(self.lives[0])
				if (self.life == 0):
					print '#################Game Over!!!!!#################'
					print '#################Your score = %d#################' % self.score
					print '++++++++++++++Play Again main.py++++++++++++++++'
					self.terminate()

	def render_score(self):
		self.score_image = self.font.render("Score = %d" % self.score, 1, TankWar.WHITE)

	def render_life(self):
		self.life_image = self.font.render("Life :", 0, TankWar.WHITE)

def main():
	game = TankWar()
	game.run()

if __name__ == '__main__':
	main()