import sqlite3
import pygame


class Scoreboard:
    def __init__(self, screen, db_name='scores.db'):
        self.screen = screen
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            score INTEGER)''')

    def add_score(self, name, score):
        query = f"SELECT * FROM scores WHERE name = '{name}';"
        result = self.cursor.execute(query).fetchall()
        if result:
            # игрок уже есть в базе данных, обновляем его счет
            current_score = result[0][2]  # получаем текущий счет игрока
            if score > int(current_score):
                # обновляем счет, только если текущий счет меньше нового
                query = f"UPDATE scores SET score = {score} WHERE name = '{name}';"

                self.cursor.execute(query)
                self.connection.commit()
        else:
            # игрока еще нет в базе данных, добавляем новую запись
            query = f"INSERT INTO scores (name, score) VALUES ('{name}', {score});"
            self.cursor.execute(query)
            self.connection.commit()


    def get_top_scores(self, limit=5):
        self.cursor.execute('SELECT DISTINCT  name, score FROM scores ORDER BY score DESC LIMIT ?', (limit,))
        return self.cursor.fetchall()

    def __del__(self):
        self.connection.close()

    def show_top_5(self):
        top_scores = self.get_top_scores()
        y = 500
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            for i, (name, score) in enumerate(top_scores):
                text = f'{i + 1}. {name}: {score}'
                text_surface = pygame.font.Font(None, 32).render(text, True, (255, 255, 255))
                self.screen.blit(text_surface, (500, y))
                y += text_surface.get_height() + 5
            pygame.display.update()