d = "Да"
while d.upper()!="НЕТ":
    a = input('число1')
    b = input('число2')
    e = input('введите_действие +-*/')
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        if e == '+':
            print(a+b)
        elif e == '-':
            print(a-b)
        elif e == '*':
            print(a*b)
        elif e == '/':
            if b == 0:
                print('error')
            else: print(a / b)
    else:
        print (" ввели не число!")
    d = input('желаете посчитать еще раз?')
print('до свидания!')

