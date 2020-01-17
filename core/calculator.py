from decorators import cache_decorator

def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    return {
        '+':lambda a,b: a+b,
        '-':lambda a,b: a - b,
        '/':lambda a,b: a / b,
        '*':lambda a,b: a * b,
        '**':lambda a,b: a ** b
    }[operation](a,b)

if __name__ == '__main__':
    while True:
            try:
            a = int(input('Введите число: '))
            break
        except ValueError:
            print("Ошибка! Неверный ввод")
    while True:
        try:
            b = int(input('Введите число: '))
            break
        except ValueError:
            print("Ошибка! Неверный ввод")
    while True:
        try:
           operation = input('Введите операцию: ')
            break
        except ValueError:
            print("Ошибка! Неверный ввод") 

    print('Результат: ', calculator(a, b, operation))