from n3 import generalHeterogeneousSolution
from taskСondition import a, b, c, d_func, f0, f1, f2, n


def f(n):
    if n == 0:
        return f0
    if n == 1:
        return f1
    if n == 2:
        return f2

    return a * f(n - 1) + b * f(n - 2) + c * f(n - 3) + d_func(n - 3) #рекурсивная функция 1 способ

for i in range(5):
    print(f'{f(i)} | {generalHeterogeneousSolution.subs(n, i)}') #1 способ | 2 способ через общее неоднородное


