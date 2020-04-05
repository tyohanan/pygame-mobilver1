import pygame
import time
import random
pygame.init()


screenpanjang=600
screenlebar=600
hitam=(0,0,0)
putih=(255,255,255)
red=(255,0,0)
vel=5
x_change=0

clock=pygame.time.Clock()
screen=pygame.display.set_mode((screenpanjang,screenlebar))
pygame.display.set_caption('Car Game')

carimage=pygame.image.load('car1.png')
carimage=pygame.transform.scale(carimage,(80,80))

def car(x,y):
	screen.blit(carimage,(x,y))

def benda1(posisix, posisiy, kotakpanjang, kotaklebar, colorbenda):
	pygame.draw.rect(screen, colorbenda, [posisix, posisiy, kotakpanjang, kotaklebar])


def game_loop():
	x=(screenpanjang*0.5)
	y=(screenlebar*0.5)
	x_change=0
	y_change=0


	finalpos_x=random.randrange(0,screenpanjang)
	finalpos_y=-600
	kotakpanjang=100
	kotaklebar=100
	kecepatanbenda=5

	crash=False
	while not crash:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crash=True
		
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
				elif event.key==pygame.K_UP:
					y_change = -5
				elif event.key==pygame.K_DOWN:
					y_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0
		x+=x_change
		y+=y_change
		screen.fill(putih)

		benda1(finalpos_x, finalpos_y, kotakpanjang, kotaklebar, hitam)
		
		finalpos_y+=kecepatanbenda		
		car(x,y)
		if finalpos_y > screenlebar:
			finalpos_y = 0 - kotakpanjang
			finalpos_x = random.randrange(0,screenlebar)





		pygame.display.update()
		clock.tick(60)
	


game_loop()
pygame.quit()
quit()

