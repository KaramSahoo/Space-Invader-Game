import pygame
pygame.init()

win = pygame.display.set_mode((700,500))
pygame.display.set_caption("DEMO")

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

running = True
while running:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.display.update()
