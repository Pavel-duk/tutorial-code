import random
def matrix(a,b):
    matrix=[]
    b+=1
    for i in range(a):
        c = []
        for j in range (b):
            c.append(random.randint(10,20))
        matrix.append(c)
    for i in range(a):
        for j in range(b):
            print(matrix[i][j], end ="")
        print()

a = int(input("сколько строк"))
b = int(input("сколько столбцов"))
matrix(a,b)
