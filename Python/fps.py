import pygame

pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 50)


def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 3, pygame.Color("coral"))
	return fps_text


loop = 1
while loop:
	screen.fill((0, 0, 0))
	screen.blit(update_fps(), (10,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = 0
	clock.tick(60)
	pygame.display.update()

pygame.quit()