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
    name = input("input your name:\n")
    player = Player(name)
    level = 1
    enemy = Enemy(level)
    while True:
        player.attack(enemy)
        player