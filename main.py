import random
import pygame

def main():
    import pygame
    from player import Player
    from enemy import Enemy
    from bullet import Bullet
    from menu import Menu
    from scoreboard import Scoreboard
    from example import Example

    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    pygame.mixer.music.load('sounds/background.mp3')
    pygame.mixer.music.play(-1)

    explostion_sounds =(pygame.mixer.Sound('sounds/bom1.mp3'),
                        pygame.mixer.Sound('sounds/bom2.mp3'),
                        pygame.mixer.Sound('sounds/bom3.mp3'))

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Shooter")

    menu = Menu(screen, 800, 600)
    player = Player(screen)

    enemy = Enemy(screen)
    bullet = Bullet(screen, 10, 10)
    scoreboard = Scoreboard(screen)
    # all_sprites = pygame.sprite.Group()
    # for i in range(50):
    #     Example(all_sprites)

    menu.run()
    player.speed = int(menu.bullet_speed)
    player.name = menu.name


    font = pygame.font.SysFont(None, 30)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((0, 0, 0))
        # Example(all_sprites)

        player.update()
        enemy.update()
        bullet.update()
        # all_sprites.update()

        # for example in all_sprites:
        #     if pygame.sprite.spritecollideany(bullet, all_sprites):
        #         all_sprites.remove(example)
        #         pygame.mixer.Channel(0).play(explostion_sounds[random.randint(0, 2)])
        #         enemy.reset()
        #         player.bullets.remove(bullet)
        #         score += 10

        #Проверка столкновения пуль и врагов
        for bullet in player.bullets:
            if enemy.meteor.colliderect(bullet.rect):
                pygame.mixer.Channel(0).play(explostion_sounds[random.randint(0, 2)])
                enemy.reset()
                player.bullets.remove(bullet)
                score += 10

        if enemy.meteor.colliderect(player.player):
            #scoreboard.add_score(player.name, score)
            #scoreboard.show_top_5()

            scoreboard.add_score(player.name, score)
            y = 100
            # получение топ-5 игроков и вывод их имен и очков на экран
            top_scores = scoreboard.get_top_scores()
            for i, (name, score) in enumerate(top_scores):
                text = f'{i + 1}. {name}: {score}'
                text_surface = font.render(text, True, (255, 255, 255))
                screen.blit(text_surface, (300, y))
                y += text_surface.get_height() + 5
            #pygame.display.flip()
            pygame.time.delay(1000)
            # окончание игры
            menu.done = False
            # pygame.quit()
            # exit()



        player.draw()
        enemy.draw()
        bullet.draw()
        # all_sprites.draw(screen)

        # Обновление счета игрока на экране
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.time.delay(5)
        pygame.display.update()

main()
