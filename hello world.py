import pygame

pygame.init()

DISPLAY = pygame.display.set_mode([330, 600])
FPSCLOCK = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
left = 40
top = 50
width = 40
height = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    DISPLAY.fill((0, 0, 0))
    pygame.draw.rect(DISPLAY, white, (left, top, width, height))

    left += 5

    pygame.display.update()
    FPSCLOCK.tick(20)