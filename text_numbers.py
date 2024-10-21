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


def get_index(objekt, list):
    for i in range(len(list)):
        if objekt == list[i]:
            return(i)
    return(-1)

def fail():
    print("ERROR")
    exit()

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
    index_big = 50
    index_small = 50
    for word in vstup:
        for j in range(len(slova)):
            if word == slova[j]:

                #osetreni tisicu atd
                if index_big <= j and j > 27:  # pokud je to nad tisic a je to mensi, nez uz bylo je problem
                    fail()
                elif j > 27:
                    index_big = j
                    index_small = 50
                    break

                if index_small > 8 and index_small < 27  and j == 27:  #když to předtim bylo 10 - 100, tak stovka byt nemuze
                    fail()
                elif index_small < 9 and j == 27:  #kdyz tam byly jednotky a dalsi ma byt 100, tak ok
                    index_small = j
                    break

                if j > 8 and j < 27:  #pokud je to 10 až 90:
                    if index_small == 27 or index_small == 50:  #jde za stovkou nebo samo
                        index_small = j
                        break
                    else:
                        fail()

                #projde jednotka, tak ta muze byt bud jen tak, nebo za stovkou, nebo za 20, 30... ,90
                if j < 9 and (index_small == 50 or (index_small > 18 and index_small < 28)):
                    index_small = j
                    break
                else:
                    fail()

                break
            elif j == len(slova)-1:
                fail()

#za timhle uz by nemel byt vstup s neplatnymy slovy :) a neni( taky blbosi tako 1 20 by měly být ok :) )

    for i in range(len(vstup)):
        index = get_index(vstup[i], slova)
        if index < 19: # pro jednotky až 19 nemusim řešit extra nuly za nimy :)
            print(index+1, end = '')

        elif index > 18 and index < 27:
            print(index-17, end ='') # index je pro 20 i = 19, tudiz pro vypsani 2 na radek, musim dat 19-17
            if i != len(vstup)-1:  # neni posledni
                if get_index(vstup[i+1], slova) < 9:
                    continue
            print('0', end='')

        elif index == 27: # je to stovka
            if i != len(vstup) - 1:  # neni posledni
                dalsi = get_index(vstup[i + 1], slova)
                if dalsi < 9: # nasleduje jednotka
                    print('0', end='')
                    continue
                elif dalsi < 27: # nasleduje 10 až 90
                    continue
            print('00', end = '')

        else:  # je to tisic nebo vic
            nuly = 3  # jako vždy tam budou moct být tri nuly
            k = 0
            j = len(vstup)
            while index - 28 - k > 0:
                k += 1
                j = get_index(slova[index - k], vstup)
                if j == -1:
                    nuly += 3
                else:
                    break

            # mam z whilu stanoveny max. pocet nul
            if j == -1: # je to posledni velka hranice
                if i != len(vstup)-1:
                    zkoumam = vstup [i+1:len(vstup)]
                else:
                    # je to posledni slovo v input textu
                    print('0'*nuly, end = '')
                    break
            else:  #nasli jsem jinou hranici
                zkoumam = vstup[i+1:j]

            #uz mam jen veci mensi nez 1000 a je to, yare yare. Jestli tohle čte někdo někdy. brácho proč by jsi to dělal?
            # ale dik, že jsi se juknul zrovna na muj kod <3

            index_big = 0  # tady to pouziju jako max. pocet nul co mam odebrat lol
            for word in zkoumam:
                j = get_index(word, slova)
                if j < 9 and index_big < 1:
                    index_big = 1
                    continue
                elif j < 27 and index_big < 2:
                    index_big = 2
                    continue
                elif j == 27:
                    index_big = 3
                    break
            nuly -= index_big
            print('0'*nuly, end='')