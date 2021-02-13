"""
5. models.py - class Enemy:
    ◦ свойства - level, lives.
    ◦ конструктор принимает уровень. Уровень жизней противнка = уровень противника.
    ◦ содержит два метода:
        1. Статический - select_attack(): возвращает случайное число от одного до трёх.
        2. decrease_lives(self): уменьшает количество жизней. Когда жизней становится 0 вызывает исключение EnemyDown.

6. models.py - class Player:
    ◦ свойства: name, lives, score, allowed_attacks.
    ◦ конструктор принимает имя игрока. Количество жизней указывается из настроек. Счет равен нулю.
    ◦ методы: статический fight(attack, defense) - возвращает результат раунда:
        0 если ничья,
        -1 если атака неуспешна,
        1 если атака успешна.

    decrease_lives(self) - то же, что и Enemy.decrease_lives(), вызывает исключение GameOver.

    attack(self, enemy_obj) - получает ввод от пользователя (1, 2, 3), выбирает атаку противника из объекта enemy_obj;
    вызывает метод fight(); Если результат боя 0 - вывести "It's a draw!", если 1 = "You attacked successfully!" и
    уменьшает количество жизней противника на 1, если -1 = "You missed!"

    defence(self, enemy_obj) - то же самое, что и метод attack(), только в метод fight первым передается атака
    противника, и при удачной атаке противника вызывается метод decrease_lives игрока.
"""
from exceptions import *
import random
from settings import lives_count


class Enemy(object):
    def __init__(self, level):
        self.level = level
        self.lives = level

    def select_attack(self):
        return random.randint(1, 3)

    def decrease_lives(self):
        if self.lives == 0:
            raise EnemyDown()
        else:
            self.lives -= 1


class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = lives_count

    def fight(self, attack, defence):
        if attack == defence:
            return "It's a draw!"


    def attack(self, enemy_obj):
        enemy_defence = enemy_obj.get_attack()
        self.player_input = input("input number: (1, 2, 3)\n")
        self.fight(self.player_input, enemy_defence)

    def decrease_lives(self):
        if self.lives == 0:
            raise GameOver(self.name, self.score)
        else:
            self.lives -= 1
