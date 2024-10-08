#dokonale cislo - treba 6, D. cislo = suma jeho delitelu -> 6 =1+2+3

def dokonale(n):  #number
    cislo = 0
    for i in range(1, n):
        if n % i == 0:
            cislo += i

    if cislo == n:
        return True
    else:
        return False

limit = int(input())

for i in range(1, limit):
    if dokonale(i):
        print(i)

