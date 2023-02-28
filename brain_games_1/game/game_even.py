import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_even():
    quest = random.randint(1, 1000)

    if is_even(quest):
        answer = 'yes'
    else:
        answer = 'no'

    return answer, quest


def is_even(num):
    return num % 2 == 0
