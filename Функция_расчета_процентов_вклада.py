#расчет прибыли от денежного вклада
print('Эта програма позволяет расчитать сумму которую вы получите положив деньги на вклад в банке за определенный срок')
def input1():
    while True:
        srok = input("Введите срок на который хотите положить вклад")
        if not srok.isdigit():
            print('вы ввели не число')
            continue
        break
    while True:
        procent = input('введите процент под который делается вклад')
        if not procent.isdigit():
            print('вы ввели не число')
            continue
        break
    while True:
        summa = input('введите сумму которую хотите положить')
        if not summa.isdigit():
            print('вы ввели не число')
            continue
        break

    return (srok,procent,summa)


def res(srok,procent,summa):
    resultat = (summa * procent * srok)/100
    resultat1 = summa + resultat
    print("Через" + ' ' + str(srok) + ' ' + 'год\а сумма на вашем счету составит' + ' ' + str(resultat1))

spisok = input1()
a = int(spisok[0])
b = int(spisok[1])
c = int(spisok[2])
res(a,b,c)