n = int(input('You can find the number of digits in the numer: '))
i = 0

while n != 0:
    n = n // 10
    i += 1
    print(n)

print('You have {0} numbers'.format(i))