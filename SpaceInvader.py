import pygame
pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

spaceshipImg = pygame.image.load("spaceship.png")
spaceshipX = 368
spaceshipY = 480
spaceshipX_change = 0

def spaceship(x, y):
	win.blit(spaceshipImg, (x, y))


running = True
while running:
	win.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				spaceshipX_change = -0.3
			if event.key == pygame.K_RIGHT:
				spaceshipX_change = 0.3
		if event.type == pygame.KEYUP:
			if event.type == pygame.K_RIGHT or event.type == pygame.K_LEFT:
				spaceshipX_change = 0

	spaceshipX += spaceshipX_change
	spaceship(spaceshipX, spaceshipY)
	pygame.display.update()
