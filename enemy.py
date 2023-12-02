import pygame
import random
from bullet import Bullet

class Enemy():
    def __init__(self, screen, path, speed):
        self.screen = screen
        self.path = path
        self.rect = pygame.image.load(self.path[random.randint(0, 3)])
        # self.rect = pygame.Rect(0, 0, 50, 50)

        self.rect = pygame.transform.scale(self.rect, (60,60))

        self.x = random.randint(0, 500)
        self.y = random.randint(0, 1)

        self.meteor = self.rect.get_rect(
            bottomright=(self.x, self.y))
        self.speed = speed
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
        self.enemies.append(Enemy(self.screen, self.path, self.speed))

        # pygame.draw.rect(self.screen, (255, 0, 0), self.rect)

    def reset(self):
        self.rect = pygame.image.load(self.path[random.randint(0, 3)])
        self.rect = pygame.transform.scale(self.rect, (random.randint(50, 100), random.randint(50, 100)))
        self.meteor.x = random.randint(0, self.screen.get_width() - self.meteor.width)
        self.meteor.y = random.randint(0, 1)
        self.speed = random.randint(self.speed, self.speed + 1)