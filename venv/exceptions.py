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
        file = open("../scores.txt", "r+").readlines()
        for string in file[3:-1:2]:
            string = string.rstrip().split("|")
            name_from_table = string[-3].rstrip().lstrip()
            score_from_table = int(string[-2])
            self.e_table.append([name_from_table, score_from_table])
        if len(self.e_table) == 0:
            self.e_table.append([name, score])
        elif len(self.e_table) > 0 and len(self.e_table) <= 10:
            for index, place in enumerate(self.e_table):
                if score >= place[1] and len(self.e_table) <= 10:
                    if len(self.e_table) < 10:
                        self.e_table.insert(index, [name, score])
                    elif len(self.e_table) == 10:
                        self.e_table = self.e_table[:9]
                        self.e_table.insert(index, [name, score])
                        break
                    break
                elif len(self.e_table) < 10 and score < self.e_table[-1][1]:
                    self.e_table.append([name, score])
                    break


        file = open("../scores.txt", "r+").truncate(0)
        self.create_table()

    def create_table(self):
        dam = f"+---+----------+-------+\n"
        for index, place in enumerate(self.e_table):
            if len(place[0]) <= 10:
                name = str(place[0]) + " " * (8 - len(place[0]))
            if len(str(place[1])) <= 7:
                score = " " * (5 - len(str(place[1]))) + str(place[1])
            current_score = f"| {index + 1} | {name} | {score} |\n"
            if index == 0:
                file = open("../scores.txt", "w")
                file.write(dam)
                file.write(self.header + "\n")
                file.write(dam)
                file.write(current_score)
                file.write(dam)

            else:
                if len(self.e_table) <= 11:
                    file = open("../scores.txt", "a+")
                    file.write(current_score)
                    file.write(dam)


score_table = Table()


class GameOver(Exception):
    def __init__(self, name, score):
        score_table.update_table(name, score)


class EnemyDown(Exception):
    pass
