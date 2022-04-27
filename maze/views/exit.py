import pygame
import pygame.locals

class Exit(pygame.sprite.Sprite):
    """
    Creates exit sprite
    """

    def __init__(self):
        image = pygame.image.load('Sprites/door.png')
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
