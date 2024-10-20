#bere text snad do (10^18)-1 a prevede na cislo, a obracene
# používáme jen číslice a slova: one, two, three, four, five, six, seven,
# eight, nine, ten, eleven, twelve, thirteen, fourteen,fifteen, sixteen, seventeen, eighteen, nineteen,
# twenty, thirty, forty,fifty, sixty, seventy, eighty, ninety, hundred, thousand, million, billion, trillion,
# quadrillion

slova = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
         "ten", "eleven", "twelve", "thirteen", "fourteen","fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
         "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety","hundred",
         "thousand", "million", "billion", "trillion", "quadrillion"]
# cisla do 1 do 9: 0-8,  od 10 do 19: 9-18,  destiky(20, 30... ,90): 19-26,  stovka: 27,  tisice-quadrilion: 28-32


def deset_na_treti(cislo, rad):
    while rad > -1:
        Stovky((cislo // 10 ** (rad * 3))%1000)
        if ((cislo // (10**(rad*3)))%1000) != 0 and rad > 0:
            print(slova[27+rad], end = ' ')
        rad -= 1

def Stovky(a):
    if a > 100:
        print(slova[(a//100)-1] + ' ' + slova[27], end = ' ')
        a = a%100
    elif a == 100:
        print(slova[0] + ' ' + slova[27], end=' ')
        a = a%100

    if a > 19:
        print(slova[17+ a//10], end = ' ') # takze pri nejmensim to bude 17+2 = 20
        a = a%10

    elif a > 9:
        print(slova[a-1], end = ' ')
        a = 0

    if a > 0:
        print(slova[a-1], end = ' ')



vstup = input()

cislo = True




# kouknu, zda je to cislo

if not vstup.isnumeric():
    cislo = False

if cislo:
    vstup = int(vstup)
    #Stovky(int(vstup))
    rad = 0
    for i in range(1, 6):
        if vstup > 10**(3*i):
            rad = i
        else:
            break

    deset_na_treti(vstup, rad)
else:
    vstup = vstup.strip().split()

    for word in vstup:
        for j in range(len(slova)):
            if word == slova[j]:
                break
            elif j == len(slova)-1:
                print("ERROR")
                exit()

# za timhle uz by nemel byt vstup s neplatnymy slovy :) a neni

