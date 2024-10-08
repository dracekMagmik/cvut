# prvocila co odectu a bude to 6
# vypiseme všecky do g(jako goal) - int co zadá uzivatel
def prime(n):  # on n jdu dál a najdu další prvočíslo
    n = int(n)
    delitel = 2
    while True:
        if n == delitel:
            return True
        elif n % delitel == 0:
            return False
        else:
            delitel += 1


g = int(input())
for i in range(3, g):
    if prime(i):
        if prime(i+6):
            print(i, i+6)
