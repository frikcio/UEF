class Table(object):
    """ score table """
    def __init__(self):
        self.max_length = 10
        self.column_1 = "    Name    "
        self.column_2 = " Score "
        self.header = f"| № |{self.column_1}|{self.column_2}|"
        self.e_table = []

    def update_table(self, name, score):
        """ update table """
        file = open("scores.txt", "r+").readlines()
        for string in file[3:-1:2]:
            string = string.rstrip().split("|")
            name_from_table = string[-3].rstrip().lstrip()
            score_from_table = int(string[-2])
            self.e_table.append([name_from_table, score_from_table])
        if len(self.e_table) == 0:
            self.e_table.append([name, score])
        elif len(self.e_table) > 0 and len(self.e_table) <= self.max_length:
            for index, place in enumerate(self.e_table):
                if score >= place[1] and len(self.e_table) <= self.max_length:
                    if len(self.e_table) < self.max_length:
                        self.e_table.insert(index, [name, score])
                    elif len(self.e_table) == self.max_length:
                        self.e_table = self.e_table[:-2]
                        self.e_table.insert(index, [name, score])
                        break
                    break
                elif len(self.e_table) < self.max_length and score < self.e_table[-1][1]:
                    self.e_table.append([name, score])
                    break


        file = open("scores.txt", "r+").truncate(0)
        self.create_table()

    def create_table(self):
        """ create table """
        dam = f"+---+------------+-------+\n"
        for index, place in enumerate(self.e_table):
            current_score = "|{: ^3}| {: <11}|{: >6} |\n".format(index + 1, place[0], place[1])
            if index == 0:
                file = open("scores.txt", "w")
                file.write(dam)
                file.write(self.header + "\n")
                file.write(dam)
                file.write(current_score)
                file.write(dam)

            else:
                if len(self.e_table) <= 11:
                    file = open("scores.txt", "a+")
                    file.write(current_score)
                    file.write(dam)


score_table = Table()


class GameOver(Exception):
    """ Game Over """
    def __init__(self, name, score):
        score_table.update_table(name, score)


class EnemyDown(Exception):
    """ Enemy down """
    pass
