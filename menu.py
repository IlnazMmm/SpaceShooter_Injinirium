import pygame

class Menu:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font(None, 32)
        self.name_input = pygame.Rect(self.screen_width / 2, 200, 140, 32)
        self.bullet_speed_input = pygame.Rect(self.screen_width / 2, 240, 140, 32)
        self.enemy_speed_input = pygame.Rect(self.screen_width / 2, 280, 140, 32)
        self.name = ""
        self.bullet_speed = ""
        self.enemy_speed = ""
        self.done_button = pygame.Rect(self.screen_width / 2, 320, 140, 32)
        self.done = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.done_button.collidepoint(event.pos):
                    return True
        return None

    def input_limit(self):
        if self.name.__len__() > 8:
            self.name = self.name
            return True
        return False

    def run(self):
        self.done = False
        while not self.done :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.done = True
                    elif event.key == pygame.K_BACKSPACE:
                        if self.name_input .collidepoint(pygame.mouse.get_pos()):
                            self.name = self.name[:-1]
                        elif self.bullet_speed_input.collidepoint(pygame.mouse.get_pos()):
                            self.bullet_speed = str(self.bullet_speed)[:-1]
                        elif self.enemy_speed_input.collidepoint(pygame.mouse.get_pos()):
                            self.enemy_speed = self.enemy_speed[:-1]
                    else:
                        if self.name_input.collidepoint(pygame.mouse.get_pos()):
                            if not self.input_limit():
                                self.name += event.unicode

                        elif self.bullet_speed_input.collidepoint(pygame.mouse.get_pos()):
                            try:
                                if type(int(event.unicode)) == type(int()):
                                        self.bullet_speed += event.unicode
                                elif self.enemy_speed == "":
                                    pass ## допиши мразь
                            except ValueError:
                                pass

                        elif self.enemy_speed_input.collidepoint(pygame.mouse.get_pos()):
                            try:
                                if type(int(event.unicode)) == type(int()):
                                    self.enemy_speed += event.unicode
                                if self.enemy_speed == "":
                                    pass ## допиши мразь
                            except ValueError:
                                pass

            self.screen.fill((255, 255, 255))
            name_text = self.font.render("Name:", True, (0, 0, 0))
            self.screen.blit(name_text, (10, 200))
            pygame.draw.rect(self.screen, (0, 0, 0), self.name_input, 2)
            name_input_text = self.font.render(self.name, True, (0, 0, 0))
            self.screen.blit(name_input_text, (self.name_input.x + 5, self.name_input.y + 5))

            bullet_speed_text = self.font.render("Player Speed:", True, (0, 0, 0))
            self.screen.blit(bullet_speed_text, (10, 240))
            pygame.draw.rect(self.screen, (0, 0, 0), self.bullet_speed_input, 2)
            bullet_speed_input_text = self.font.render(self.bullet_speed, True, (0, 0, 0))
            self.screen.blit(bullet_speed_input_text, (self.bullet_speed_input.x + 5, self.bullet_speed_input.y + 5))

            enemy_speed_text = self.font.render("Enemy Speed:", True, (0, 0, 0))
            self.screen.blit(enemy_speed_text, (10, 280))
            pygame.draw.rect(self.screen, (0, 0, 0), self.enemy_speed_input, 2)
            enemy_speed_input_text = self.font.render(self.enemy_speed, True, (0, 0, 0))
            self.screen.blit(enemy_speed_input_text, (self.enemy_speed_input.x + 5, self.enemy_speed_input.y + 5))

            # pos = pygame.mouse.get_pos()
            # p = self.font.render("Играть", True, (0, 0, 0))#pygame.Rect(self.screen_width / 2, 320, 140, 32), 2)
            # if p.collidepoint(pygame.mouse.get_pos()):
            #     self.screen.blit(p, (250, 250))
            # else:
            #     self.screen.blit(p, (245, 245))
            #if self.enemy_speed_input.collidepoint(pygame.mouse.get_pos()):
            pygame.display.update()