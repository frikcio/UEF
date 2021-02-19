import models
import settings
import exceptions


def play():
    """ start game """
    while True:
        name = input("input your name:\n")
        if len(name) <= 10:
            break
        else:
            print("max count char is 10\n")
    player = models.Player(name)
    level = 1
    enemy = models.Enemy(level)
    print(f"LEVEL {level}")
    while True:
        try:
            if player.attack(enemy) == "done":
                if player.defence(enemy) == "done":
                    settings.pause()
                    settings.clear_area()
        except exceptions.EnemyDown:
            print("Enemy down")
            player.score += 5
            level += 1
            enemy = models.Enemy(level)
            break


if __name__ == '__main__':
    try:
        play()
    except exceptions.GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print("Good Bye!")
        print(exceptions.score_table.e_table)
