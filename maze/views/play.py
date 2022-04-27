import pygame
import pygame.locals

class Play(pygame.sprite.Sprite):
    """
    Creates player sprite
    """

    def __init__(self):
        image = pygame.image.load('Sprites/player.png')
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()