import random
import operator
import prompt
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
        a, b = random.randint(1, 50), random.randint(1, 20)
        oper = random.choice(list(action))
        quest = action[oper](a, b)
        print(f'Question: {a} {oper} {b}')
        answer_player = prompt.string('Your answer: ')
        if int(answer_player) == quest:
            print('Correct!')
        else:
            print(f"{answer_player} is wrong answer ;(. Correct answer was {quest}.")
            print(f"Let's try again, {cli.name}!")
            break
    else:
        print(f'Congratulations, {cli.name}!')


if __name__ == '__main__':
    main()
