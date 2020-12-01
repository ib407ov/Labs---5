a = float(input('number type ,float, : '))
n = int(input('number type ,int, : '))

Summ = a

for i in range(n):
    Summ = Summ * (a + (i +1))

print('Summ= {0}' .format(Summ))
