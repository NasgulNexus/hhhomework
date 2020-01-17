from random import randint
# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    answer = []
    for i in range(N):
        answer.append(randint(1, 100))
    return answer
# написать генераторное выражение, которое делает то же самое
generatorAnswer = (randint(1, 100) for i in range(N))
