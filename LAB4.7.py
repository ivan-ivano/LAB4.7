# < Іваньо Іван >
# Лабораторна робота № 4.7
# Обчислення суми ряду Тейлора за допомогою ітераційних циклів та рекурентних співвідношень.
# Варіант 0.6

import math

X_start = float(input("X_поч: "))
X_end = float(input("X_кін: "))
dX = float(input("dX: "))
eps = float(input("eps: "))

print('----------------------------------------')
print('|   X   |   ln(1 - x)  |   S   |   n   |')
print('----------------------------------------')

x = X_start
while x <= X_end:
    n = 1
    a = x
    S = a
    while True:
        n += 1
        R = x * (n - 1) / n
        a *= R
        S += a
        if abs(a) <= eps:
            break
    ln = math.log(1 - x)
    print('|   {0}   |   {1}   |   {2}   |   {3}   |'.format(str(round(x, 4)), str(round(ln, 4)), str(round(-S, 4)), str(n)))
    x += dX

print('----------------------------------------')
