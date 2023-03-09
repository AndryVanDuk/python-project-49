import random


RULES = 'What number is missing in the progression?'


def get_game():
    length = random.randint(5, 10)
    start = random.randint(0, 50)
    step = random.randint(1, 10)
    data = list()
    data.append(start)

    for i in range(length-1):
        data.append(data[i]+step)
    index = random.randint(0, length-1)
    data = [str(x) for x in data]
    answer = data[index]
    data[index] = '..'
    quest = ' '.join(data)
    return answer, quest
