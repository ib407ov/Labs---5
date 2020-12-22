x=float(input("Введіть змінну x=\n"))
e=float(input("Введіть точність е=\n"))

import math
n = 1
Summ = 2

while math.fabs(2+((1 / 2 * n - 1) * ((x - 1 / x + 1) ** (2 * n - 1))))>e:
    Summ = ((1 / 2 * n - 1) * ((x - 1 / x + 1) ** (2 * n - 1)))
    n += 1
    if n == x:
        break
Summ += 2

print("Добуток:{0}".format(Summ))


if math.log1p(x) - Summ < e:
    print("Рівність справедлива Summ = ln(x)")
else:
     print("Рівнсть не справедлива")

