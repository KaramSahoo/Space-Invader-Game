import pygame
pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("DEMO")

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

spaceshipImg = pygame.image.load("spaceship.png")
spaceshipX = 368
spaceshipY = 480

def spaceship():
	win.blit(spaceshipImg, (spaceshipX , spaceshipY))


running = True
while running:
	win.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	spaceship()
	pygame.display.update()
