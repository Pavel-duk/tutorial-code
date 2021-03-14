#Игра угадай слово
login = input('Введите логин')
a_dict1 = {}
a_dict = [login]
import random
q = "да"
while q == "да":
    worde = ('словей',"птеродактиль","синхрофазотрон","мяскомбинат","соленоид","предохранитель","распределитель","транзистор","иммобилайзер")

    a = random.choice(worde)
    b = a.split()
    for i,word in enumerate(map(list,b)):
        random.shuffle(word)
        b[i] = ''.join(word)

    c = "Угадай слово:"
    print(c,b)
    correct = input("Твой ответ")
    m = int(0)
    if correct == a:
        print('Верно!')
        if correct == a:
             n = int(1)
    else:
        n = int(0)
        print('не верно!')
    q = input('Хочешь сыграть еще раз?')
print('До свидания !')
a_dict1[login] = (m + n)
print(a_dict1)