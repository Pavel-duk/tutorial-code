#функция замены невведенных слов (не обязательные аргументы
def forma(name,age='не указан',gender='не указан'):
        print('имя' + ' ' + name,'\n' + 'возраст'+ ' ' + str(age),'\n' + 'пол' + ' ' + gender)

print('Добро пожаловать на нашем сайте!','\n' + 'Заполните анкету')
name = input('Введите имя')
while True:
    age = input('Введите ваш возраст')
    if age.isalpha():
        print('Введите число!')
    elif age == '':
        break
    else:
        break

while True:
    gender = input('Введите пол: муж или жен')
    if gender.isalpha() or gender.isdigit():
            if not gender=='муж' or gender=='жен':
                print('Введите муж или жен!')
            else:
                break
    elif gender == "":
        break
    else:
        break

if age == '' and gender == '':
    forma(name)
elif gender == '':
    forma(name,age)
elif age == '':
    age = 'не указан'
    forma(name,age,gender)
else:
    forma(name,age,gender)