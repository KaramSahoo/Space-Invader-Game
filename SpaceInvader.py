import pygame
import math
import random
from pygame import mixer

pygame.init()

win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background.png")

mixer.music.load("background.wav")
mixer.music.play(-1)
explosion_sound = mixer.Sound("explosion.wav")
bullet_sound = mixer.Sound("bullet_sound.wav")
					
spaceshipImg = pygame.image.load("spaceship.png")
spaceshipX = 343
spaceshipY = 380
spaceshipX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_count = 6

for i in range(enemy_count):
	enemyImg.append(pygame.image.load("enemy.png"))
	enemyX.append(random.randint(0, 686))
	enemyY.append(random.randint(50, 150))
	enemyX_change.append(2)
	enemyY_change.append(30)

bulletImg = pygame.image.load("bullet.png")
bulletX = 365
bulletY = 380
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score_val = 0
font = pygame.font.Font("ARCADECLASSIC.ttf", 16)

def display_score(x, y):
	score = font.render("Score " + str(score_val), True, (255,255,255))
	win.blit(score, (x, y))

def spaceship(x, y):
	win.blit(spaceshipImg, (x, y))

def enemy(x, y, i):
	win.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
	global bullet_state
	bullet_state = "fire"
	win.blit(bulletImg, (x+16, y+10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
	proximity = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))
	if proximity < 29:
		return True
	return False

running = True
while running:
	win.blit(background, (0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				spaceshipX_change = -2.5
			if event.key == pygame.K_RIGHT:
				spaceshipX_change = 2.5
			if event.key == pygame.K_SPACE:
				if bullet_state is "ready":
					bullet_sound.play()
					bulletX = spaceshipX
					fire_bullet(bulletX, bulletY)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				spaceshipX_change = 0

	spaceshipX += spaceshipX_change

	spaceshipX = 0 if spaceshipX < 0 else spaceshipX
	spaceshipX = 686 if spaceshipX > 686 else spaceshipX

	for i in range(enemy_count):
		
		enemyX[i] += enemyX_change[i]
		if enemyX[i] < 0:
			enemyX_change[i] = 2 + (score_val*0.1)
			enemyY[i] += enemyY_change[i]
		elif enemyX[i] > 686:
			enemyX_change[i] = -2 - (score_val*0.1)
			enemyY[i] += enemyY_change[i]
		
		collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
		if collision is True:
			explosion_sound.play()
			bulletY = 380
			bullet_state = "ready"
			score_val += 1
			enemyX[i] = random.randint(0, 686)
			enemyY[i] = random.randint(50, 150)

		enemy(enemyX[i], enemyY[i], i)
	
	if bulletY < 0:
		bulletY = 380
		bullet_state = "ready"
	if bullet_state is "fire":
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change

	spaceship(spaceshipX, spaceshipY)
	display_score(10, 10)
	pygame.display.update()
