import pygame
pygame.init()

win = pygame.display.set_mode((750,500))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background.png")

spaceshipImg = pygame.image.load("spaceship.png")
spaceshipX = 343
spaceshipY = 380
spaceshipX_change = 0

def spaceship(x,y):
	win.blit(spaceshipImg, (x, y))


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

	spaceshipX = 0 if spaceshipX < 0 else spaceshipX
	spaceshipX = 686 if spaceshipX > 686 else spaceshipX

	spaceshipX += spaceshipX_change
	spaceship(spaceshipX, spaceshipY)
	pygame.display.update()
