import settings
import exceptions
import random



class Enemy(object):
    """ Enemy class """
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """ enemy's attack """
        return random.randint(1, 3)

    def decrease_lives(self):
        """ enemy's decrease lives """
        if self.lives > 0:
            self.lives -= 1
        else:
            raise exceptions.EnemyDown()


class Player(object):
    """ Player class """
    def __init__(self, name):
        self.name = name
        self.score = 0
        key = input("Chose difficulty: (easy, medium, hard, one)\n: ")
        self.lives = settings.difficulty[key]

    @staticmethod
    def fight(attack, defence, kind):
        """ fight player vs enemy """
        if kind == "att":
            draw_color = settings.Style.YELLOW
            hit_color = settings.Style.BLUE
            miss_color = settings.Style.RED
        else:
            draw_color = settings.Style.BLUE
            hit_color = settings.Style.RED
            miss_color = settings.Style.BLUE
        end_color = settings.Style.RESET
        if attack == defence:
            print(draw_color + "It's a draw!\n" + end_color)
            return 0
        elif defence - attack == 1 or defence - attack == -2:
            print(hit_color + "Gotcha!\n" + end_color)
            return 1
        else:
            print(miss_color + "missed!\n" + end_color)
            return -1

    def attack(self, enemy_obj):
        """ player's attack """
        enemy_defence = enemy_obj.select_attack()
        print("ATTACK!")
        player_input = input("Waiting for your input:\n")
        if player_input in settings.commands:
            settings.commands[player_input]()
        elif player_input.isnumeric():
            player_input = int(player_input)
            if player_input < 4:
                result = self.fight(player_input, enemy_defence, "att")
                if result == 1:
                    self.score += 1
                    enemy_obj.decrease_lives()
                return "done"
            else:
                print("input out of range")
        else:
            print("Please enter a number or 'help'")

    def defence(self, enemy_obj):
        """ player's defence """
        enemy_attack = enemy_obj.select_attack()
        print("DEFENCE!")
        player_input = input("Waiting for your input:\n")
        if player_input in settings.commands:
            settings.commands[player_input]()
        elif player_input.isnumeric():
            player_input = int(player_input)
            if player_input < 4:
                result = self.fight(enemy_attack, player_input, "def")
                if result == 1:
                    self.decrease_lives()
                return "done"
            else:
                print("input out of range")
        else:
            print("Please enter a number or 'help'")

    def decrease_lives(self):
        """ player's decrease lives """
        if self.lives == 0:
            raise exceptions.GameOver(self.name, self.score)
        else:
            self.lives -= 1
