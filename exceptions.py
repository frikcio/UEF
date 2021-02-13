"""
4. exceptions.py:
    ◦ Содержит класс GameOver - унаследованный от Exception. В классе должен быть реализован механизм сохранения
    финального счета игрока по завершению игры в файл scores.txt
    ◦ Содержить класс EnemyDown - унаследованный от Exception. Функционал не обязателен.
    ▪ Создать механизм сохранения только 10 лучших счетов игроков. Можно реализовать через класс Score.
"""


class Table():
    def __init__(self):
        self.current_length = 0
        self.max_length = 10
        self.column_1 = "   Name   "
        self.column_2 = " Score "
        self.header = f"| № |{self.column_1}|{self.column_2}|"
        self.e_table = []

    def update_table(self, name, score):
        if len(self.e_table) == 0:
            self.e_table.append([name, score])
        elif len(self.e_table) > 0 and len(self.e_table) < 10:
            for index, place in enumerate(self.e_table):
                if score >= place[1]:
                    self.e_table.insert(index, [name, score])
                    break
                elif len(self.e_table) < 10 and score < self.e_table[-1][1]:
                    self.e_table.append([name, score])
                    break
        file = open("scores.txt", "r+").truncate(0)
        self.create_table()

    def create_table(self):
        file = open("scores.txt", "r+").read()
        dam = f"+---+----------+-------+\n"
        for index, place in enumerate(self.e_table):
            current_score = f"| {index + 1} |  {place[0]} | {place[1]} |\n"
            if index == 0:
                file = open("scores.txt", "w")
                file.write(dam)
                file.write(self.header + "\n")
                file.write(dam)
                file.write(current_score)
                file.write(dam)

            else:
                if len(self.e_table) <= 10:
                    file = open("scores.txt", "a+")
                    file.write(current_score)
                    file.write(dam)





class GameOver(Exception):
    def __init__(self, name, score):
        score_table = Table()
        score_table.update_table(name, score)


class EnemyDown(Exception):
    pass

