import pygame
import pygame.locals

class Key(pygame.sprite.Sprite):
    """
    Creates item sprite
    """

    def __init__(self):
        image = pygame.image.load('Sprites/key.png')
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
