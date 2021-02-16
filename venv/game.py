"""
7. game.py:
    ◦ Содержит блок на проверку имени модуля (main)
    ◦ внутри if блок try/except.
    ◦ try запускает функцию play()
    ◦ except обрабатывает два исключения: GameOver - выводит сообщение об ошибке, записывает результат в таблицу
    рекордов. KeyboardInterrupt - pass
    ◦ finally печатает "Good bye!"
8. game.py - play():
    ◦ Ввод имени игрока
    ◦ Создание объекта player
    ◦ level = 1
    ◦ Создание объекта enemy
    ◦ в бесконечном цикле вызывает методы attack и defense объекта player
    ◦ при возникновении исключения EnemyDown повышает уровень игры, создает новый объект Enemy с новым уровнем,
    добавляет игроку +5 очков.
"""
from models import *


def play():
    while True:
        name = input("input your name:\n")
        if len(name) <=8:
            break
        else:
            print("max count char is 8\n")
    player = Player(name)
    level = 1
    while True:
        enemy = Enemy(level)
        print(f"LEVEL {level}")
        while True:
            try:
                player.attack(enemy)
                player.defence(enemy)
            except EnemyDown:
                print("Enemy down")
                player.score += 5
                level += 1
                break


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print("Good Bye!")
        print(score_table.e_table)
