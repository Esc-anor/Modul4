# Создаем модуль true_math
from math import inf


# создаём функцию divide
def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second
