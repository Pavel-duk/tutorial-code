def summa(n):
    if n == 0:
        return 0
    else:
        return n % 10 + summa(n//10)

print(summa(25))