import pygame
from settings import *
class Player:
    @property
    def pos(self):
        return(self.x, self.y)
    def __init__(self):
        self.x, self.y = player_pos
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x += player_speed
        if keys[pygame.K_a]:
            self.x -= player_speed
        if keys[pygame.K_w]:
            self.y -= player_speed
        if keys[pygame.K_s]:
            self.y += player_speed