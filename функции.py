#создать функцию которая возвращает количество гласных букв в строке
def kol_glasnih(a):
    gla = "уеаоэяиюё"
    lena = len(a)
    i = 0
    koll_gla = 0
    while i<lena:
        if a[i] in gla:
            koll_gla+=1
        i+=1
    return koll_gla

vvod = input("Введите слово для подсчета гласных")

print(kol_glasnih(vvod))




#удаление гласснх из строки
def delit(b):
    a = 'уеыаоэяиюё'
    i = 0
    c = len(b)
    while i < c:
        if b[i] in a:
            b = b[:i] + b[i+1:]
            c-=1
            i-=1
        i+=1
    return b

wer = input("введите слово для удаления гласнх")

print(delit(wer))
