import random
import prompt
from brain_games_1 import cli


def main():
    cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_even()


def game_even():
    num_atem = 0
    while num_atem < 3:
        quest = random.randint(1, 1000)
        print(f'Question: {quest}')
        answer_player = prompt.string('Your answer: ')
        if is_even(quest) and answer_player == 'yes':
            print('Correct!')
            num_atem += 1
        elif not is_even(quest) and answer_player == 'no':
            print('Correct!')
            num_atem += 1
        else:
            print(f"{answer_player} is wrong answer ;(. Correct answer was {back_ans(answer_player)}.")
            print(f"Let's try again, {cli.name}!")
            break
    else:
        print(f'Congratulations, {cli.name}!')


def is_even(num):
    return num % 2 == 0


def back_ans(ans):
    if ans == 'yes':
        return 'no'
    elif ans == 'no':
        return 'yes'


if __name__ == '__main__':
    main()