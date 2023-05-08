import pygame
from bullet import Bullet


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.image.load('pictures/player-IxSoUMj1F-transformed.png')
        self.player = self.rect.get_rect(
            bottomright=(250, 500))
        self.speed = 1
        self.bullets = []

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.player.left > 0:
            self.player.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.player.right < self.screen.get_width():
            self.player.x += self.speed
        elif keys[pygame.K_UP] and self.player.top > 0:
            self.player.y -= self.speed
        elif keys[pygame.K_DOWN] and self.player.bottom < self.screen.get_height():
            self.player.y += self.speed


        if keys[pygame.K_SPACE]:
            pygame.mixer.Sound('sounds/blaster_shoot.mp3').play()
            bullet = Bullet(self.screen, self.player.centerx, self.player.top)
            bullet.rect.x = self.player.x + 16
            bullet.rect.y = self.player.y - 32
            self.bullets.append(bullet)

        for bullet in self.bullets:
            bullet.update()

    def draw(self):
        self.screen.blit(self.rect, self.player)
        # pygame.draw.rect(self.screen, (255, 0, 0), self.rect)

        for bullet in self.bullets:
            bullet.draw()
