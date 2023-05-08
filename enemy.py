import pygame
import random
from bullet import Bullet

class Enemy():
    def __init__(self, screen):
        self.screen = screen
        # self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect = pygame.image.load('pictures/amir-transformed.png')
        self.rect = pygame.transform.scale(self.rect, (60,60))
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 1)

        self.meteor = self.rect.get_rect(
            bottomright=(self.x, self.y))
        self.speed = 1
        self.enemies = []

    def update(self):
        self.meteor.y += self.speed
        # self.enemies.append(Enemy(self.screen))
        #
        # for enemy in self.enemies:
        #     enemy.update()

        if self.meteor.y > self.screen.get_height():
            self.reset()

    def draw(self):
        self.screen.blit(self.rect, self.meteor)
        self.enemies.append(Enemy(self.screen))

        # pygame.draw.rect(self.screen, (255, 0, 0), self.rect)

    def reset(self):
        self.meteor.x = random.randint(0, self.screen.get_width() - self.meteor.width)
        self.meteor.y = random.randint(0, 1)
        self.speed = random.randint(1, 3)