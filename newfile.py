import pygame
from game.settings import *
from game.player import Player
pygame.init()
player = Player()
FPS = 60
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    player.movement()
    pygame.draw.circle(sc, GREEN, player.pos, 12)
    pygame.display.flip()
    clock.tick(FPS)