import random

import pygame

class Example(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('pictures/meteor-transformed.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(750)
        self.rect.y = random.randrange(1)

    def update(self):
        pygame.time.Clock()
        self.rect.y += 1
