import pygame
import random
pygame.init()

win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background.png")

spaceshipImg = pygame.image.load("spaceship.png")
spaceshipX = 343
spaceshipY = 380
spaceshipX_change = 0

enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 686)
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 30

def spaceship(x, y):
	win.blit(spaceshipImg, (x, y))

def enemy(x, y):
	win.blit(enemyImg, (x, y))

running = True
while running:
	win.blit(background, (0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				spaceshipX_change = -2
			if event.key == pygame.K_RIGHT:
				spaceshipX_change = 2
		if event.type == pygame.KEYUP:
			if event.type == pygame.K_RIGHT or event.type == pygame.K_LEFT:
				spaceshipX_change = 0

	spaceshipX += spaceshipX_change

	spaceshipX = 0 if spaceshipX < 0 else spaceshipX
	spaceshipX = 686 if spaceshipX > 686 else spaceshipX

	enemyX += enemyX_change

	if enemyX < 0:
		enemyX_change = 2
		enemyY += enemyY_change
	if enemyX > 686:
		enemyX_change = -2
		enemyY += enemyY_change
	
	enemy(enemyX, enemyY)
	spaceship(spaceshipX, spaceshipY)
	pygame.display.update()
