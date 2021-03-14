input1 = 'abcd'
def new(a):
    new_stroka = []
    raz = '-'
    for i in range(len(a)):
        new_stroka.append(a[i]*(i+1))
    new_stroka = raz.join(new_stroka)
    new_stroka = new_stroka.title()

    print(new_stroka)

new(input1)
