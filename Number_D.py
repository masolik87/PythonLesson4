# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, ? = 3.141   
# Ввод: 0.01: Вывод 3.14 / Ввод: 0.001: Вывод: 3.141

import math

d = input('enter the number: ')
d = d[2:len(d)]
print(round(math.pi,len(d)))