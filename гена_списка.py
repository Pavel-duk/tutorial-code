u = []
zapros = input('введите размер списка')
import random
if zapros.isdigit():
    for i in range(int(zapros)):
        d = random.randint(1,1000)
        u.append(d)
    print(u)
else:
    print('ввели не число')