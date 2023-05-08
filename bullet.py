import pygame

class Bullet:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 20)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 5


    def update(self):
        self.rect.y -= self.speed

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 255), self.rect)


    def is_colliding_with(self, sprite):
        return self.rect.colliderect(sprite.rect)