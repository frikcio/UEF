""" import exception from exceptions.py """
import exceptions
import os
import time


def pause():
    """ pause for console """
    time.sleep(2)


def clear_area():
    """ clear console """
    os.system("cls")


difficulty = {"easy": 5,  "medium": 4, "hard": 2, "one": 1}


def aid():
    """ print all commands """
    print("Commands:\nshow scores\nexit \nhelp\n")


def show_scores():
    """ shows table score """
    file = open("scores.txt", "r").readlines()
    for line in file:
        print(line.rstrip())


def out():
    """ close game """
    raise exceptions.GameOver("", 0)


class Style(object):
    """ class with colors """
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


""" dictionary with all commands """
commands = {"show scores": show_scores, "exit": out, "help": aid}
