
import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 0, 0])
pygame.draw.circle(screen, [150, 150, 150], [320, 240], 100, 0)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUTT:
            Ssys.exit()
