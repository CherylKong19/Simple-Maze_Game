import pygame
import pygame.locals

class Wall(pygame.sprite.Sprite):
    """
    Creates wall sprite
    """

    def __init__(self):
        image = pygame.image.load('Sprites/wall.png')
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()