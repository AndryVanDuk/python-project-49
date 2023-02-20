import random
import operator
from brain_games_1 import cli


def main():
    cli.welcome_user()
    print('What is the result of the expression?')
    game_calc()


def game_calc():
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    for _ in range(3):
        quest = action[](random.randint(1, 100), random.randint(1, 100))
        print(f'Question: {quest}')




if __name__ == '__main__':
    main()
