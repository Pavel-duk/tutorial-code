def spravka(*args):
    dict1 = {}
    for i in range(0,len(args),2):
        dict1[args[i]] = args[i+1]
    print(dict1)

spisok = []
answer = 'да'
while answer == 'да':
    while True:
        name = input('Введите имя друга')
        if name.isalpha():
            spisok.append(name)
            break
        else:
            print('Введите имя состоящее только из букв')
    while True:
        namber = input ('Введите его номер')
        if namber.isdigit():
            spisok.append(namber)
            break
        else:
            print('В номере телефона не может быть букв')
    answer = input('хотите добавить еще один контакт?(да\нет)')

spravka(spisok)
