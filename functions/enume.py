"""
enumerate возвращает итератор (ленивый)
То есть он не создаёт список сразу.

Хорошо для больших данных и потоков.
Если вам нужен список пар - можно явно материализовать

"""

a = [10, 20, 30, 40, 50]
print(list(enumerate(a)))
for index, item in enumerate(a):
    print(index, item)

import sys, time
def teleprint(*args, delay=0.1, str_join=' '):
    """ Замедленный вывод текста в консоли """
    text = str_join.join(str(x) for x in args)
    n = len(text)
    for i, char in enumerate(text, 1):
        # если количество символов
        # равно текущему счетчику.
        if i == n:
            # печать последнего символа с переводом строки '\n'
            char = f'{char}\n'
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

teleprint('Привет Python!')
