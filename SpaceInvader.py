import pygame
pygame.init()

win = pygame.display.set_mode((700,500))
pygame.display.set_caption("DEMO")

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
