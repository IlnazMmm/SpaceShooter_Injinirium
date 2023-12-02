import pygame

class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 32)
        self.name_input = pygame.Rect(self.width/2, 200, 140, 32)
        self.bullet_speed_input = pygame.Rect(self.width/2, 240, 140, 32)
        self.meteor_speed_input = pygame.Rect(self.width/2, 280, 140, 32)
        self.name = ""
        self.bullet = ""
        self.meteor = ""
        self.done_button = pygame.Rect(self.width/2, 320, 140, 32)
        self.done = False

    def run(self):
        self.done = True
        while self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.name_input.collidepoint(pygame.mouse.get_pos()):
                            self.name = self.name[:-1]

                        elif self.bullet_speed_input.collidepoint(pygame.mouse.get_pos()):
                            self.bullet = self.bullet[:-1]

                        elif self.meteor.collidepoint(pygame.mouse.get_pos()):
                            self.meteor = self.meteor[:-1]
                    else:
                        if self.name_input.collidepoint(pygame.mouse.get_pos()):
                            print('sdfdsf')
                            self.name += event.unicode

                        if self.bullet_speed_input.collidepoint(pygame.mouse.get_pos()):
                            try:
                                if type(int(event.unicode)) == type(int()):
                                    self.bullet += event.unicode
                                else:
                                    self.bullet = ''
                            except ValueError:
                                pass

                        if self.meteor_speed_input.collidepoint(pygame.mouse.get_pos()):
                            try:
                                if type((int(event.unicode))) == type(int()):
                                    self.meteor += event.unicode
                                else:
                                    self.meteor = ''
                            except ValueError:
                                pass

            self.screen.fill((255, 255, 255))
            name_text = self.font.render("Name:", True, (0, 0, 0))
            self.screen.blit(name_text, (10, 200))
            pygame.draw.rect(self.screen, (0, 0, 0), self.name_input, 2)
            name_input_text = self.font.render(self.name, True, (0, 0, 0))
            self.screen.blit(name_input_text, (self.name_input.x + 5, self.name_input.y + 5))


            name_text = self.font.render("Скорость пули:", True, (0, 0, 0))
            self.screen.blit(name_text, (10, 240))
            pygame.draw.rect(self.screen, (0, 0, 0), self.bullet_speed_input, 2)
            name_input_text = self.font.render(self.bullet, True, (0, 0, 0))
            self.screen.blit(name_input_text, (self.bullet_speed_input.x + 5, self.bullet_speed_input.y + 5))

            name_text = self.font.render("Скорость метеорита:", True, (0, 0, 0))
            self.screen.blit(name_text, (10, 280))
            pygame.draw.rect(self.screen, (0, 0, 0), self.meteor_speed_input, 2)
            name_input_text = self.font.render(self.meteor, True, (0, 0, 0))
            self.screen.blit(name_input_text, (self.meteor_speed_input.x + 5, self.meteor_speed_input.y + 5))

            pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((1200, 800))
width = 1200
height = 800

menu = Menu(screen, width, height)
menu.run()