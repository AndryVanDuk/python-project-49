import random
import operator


RULES = 'What is the result of the expression?'


def get_game():
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    a, b = random.randint(1, 50), random.randint(1, 20)
    operand = random.choice(list(action))
    answer = action[operand](a, b)
    quest = f'{a} {operand} {b}'
    return str(answer), quest
