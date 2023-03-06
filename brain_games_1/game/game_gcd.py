import random
import math


RULES = 'Find the greatest common divisor of given numbers.'

def get_game():
    a, b = random.randint(1, 100), random.randint(1, 100)
    answer = math.gcd(a, b)
    quest = f'{a} {b}'
    return str(answer), quest