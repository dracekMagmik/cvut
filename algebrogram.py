#import library.mylib as lib
#lib.LoL()
import sys

def readInput(name, array):
    f = open(name, "rt")
    while True:
        line = f.readline().strip()
        if line != '':
            array.append(line)
        else:
            break

def word_bubble(ar):
    done = False
    while done == False:
        done = True
        for i in range(1, len(ar)):
            j = i-1
            if ord(ar[i]) < ord(ar[j]):
                ar[j], ar[i] = ar[i], ar[j]
                done = False
    return ar

def unique(ar):
    letters = []
    for a in ar:
        for i in range(len(a)):
            if ord(a[i]) > 64 and ord(a[i]) < 91:
                if len(letters) == 0:
                    letters.append(a[i])
                else:
                    clear = True
                    for b in letters:
                        if b == a[i]:
                            clear = False
                            break
                    if clear:
                        letters.append(a[i])
    return word_bubble(letters)


def replace(str, ch, op, eq): # op = index of operand, eq = index of equals
    new = str[eq+1:] + ch + str[op+1:eq] + '=' + str [:op]
    return new

def plus_multiply(array):
    for i in range(len(array)):
        c = ''
        k = 0
        for j in range(len(array[i])):
            if array[i][j] == '/':
                c = '*'
                k = j
            elif array[i][j] == '-':
                c = '+'
                k = j

            if c != '' and array[i][j] == '=':
                array[i] = replace(array[i], c, k, j)
    return array

#mrkne na algebrogram a vrati velikosti cisel
def chunk_sizes(str, taken):
    i = j = k = ''
    index = 0
    plus = True
    for a in str:
        if ord(a) > 64 and ord(a) < 91:
            if index == 0: i = i + a
            elif index == 1: j = j + a
            elif index == 2: k = k + a
        else:
            if a == '*':
                plus = False
            index += 1

    # hodnoty na prvních místech nebudou nula
    if 0 in values[i[0]][3] == False:
        values[i[0]][3].append(0)

    if 0 in values[j[0]][3] == False:
        values[j[0]][3].append(0)

    if 0 in values[k[0]][3] == False:
        values[k[0]][3].append(0)

    #algebrogramy? more like algebrolamy (im very sad)
    # tohle se koukna na prvni mista v nasobeni a kdyz se vsechny cisla lisi, pak tak sčítanci(jemnuje se to tak, lol?)
    # nejsou nula. podobny princip s jednickou v nasobeni
    if i[-1] != k[-1] and j[-1] != k[-1]:
        if plus:
            if values[i[-1]][3] == False:
                values[i[-1]][3].append(0)
            if values[j[-1]][3] == False:
                values[j[-1]][3].append(0)
        else:
            if values[i[-1]][3] == False:
                values[i[-1]][3].append(0)
                values[i[-1]][3].append(1)
            if values[j[-1]][3] == False:
                values[j[-1]][3].append(0)
                values[j[-1]][3].append(1)



    if plus:
        # ok, takže tady budu zkoušet ja nevimmmm, tak optimalizace dve a je to tyjo ugh....
        # no jako, když je to třeba AB+CD=EB, tak potom D je 0, to asi hodim do toho if plus dole
        if i[-1] == k[-1] and i[-1] != j[-1]:
            if taken[0] and values[j[-1]][0] != 0:
                return False
            values[j[-1]][0] = 0
            values[j[-1]][1] = True
            taken[0] = True
        elif j[-1] == k[-1] and i[-1] != j[-1]:
            if taken[0] and values[i[-1]][0] != 0:
                return False
            values[i[-1]][0] = 0
            values[i[-1]][1] = True
            taken[0] = True

        if(third_largest(i,j,k)):
            if taken[1] and values[k[0]][0] != 1:
                return False
            else:
                values[k[0]][0] = 1
                values[k[0]][1] = True
                taken[1] = True
    return True


def re_chunk_size(str, taken):
    i = j = k = ''
    index = 0
    plus = True
    for a in str:
        if ord(a) > 64 and ord(a) < 91:
            if index == 0:
                i = i + a
            elif index == 1:
                j = j + a
            elif index == 2:
                k = k + a
        else:
            if a == '*':
                plus = False
            index += 1

    if plus:
        if (third_largest(i, j, k)):
            if taken[1] and values[k[0]][0] != 1:
                return False
            else:
                values[k[0]][0] = 1
                values[k[0]][1] = True
                taken[1] = True

            if values[k[1]][0] == 0:
                # takže vysledek je treba 105, a to ze dvou dvoucif. cisel, takže A+B+1(cislo z i, j a preteceni) = 10. jinak se tam 0 nedostane.
                # tim padem A+B+1 = 10 -> A+B = 9
                if i[0] == k[1]:  # je to nula
                    if taken[9] and values[j[0]][0] != 9:
                        return False
                    values[j[0]][0] = 9
                    values[j[0]][1] = True
                elif j[0] == k[1]:  # je to nula
                    if taken[9] and values[i[0]][0] != 9:
                        return False
                    values[i[0]][0] = 9
                    values[i[0]][1] = True

                # tady uz to nemusi byt nutne s pretecenim 10+9s = 10s a 's+0 nepretece'
                elif i[0] == k[0]:  # je to 1
                    if not taken[8]:
                        values[j[0]][2].append(8)
                    if not taken[9]:
                        values[j[0]][2].append(9)

                elif j[0] == k[0]:  # je to 1
                    if not taken[8]:
                        values[i[0]][2].append(8)
                    if not taken[9]:
                        values[i[0]][2].append(9)

                else:
                    values[i[0]][3].append(8)
                    values[i[0]][3].append(9)
                    values[j[0]][3].append(8)
                    values[j[0]][3].append(9)

    #nejaka nasobeni optimalizace potreba :skull: ale COOOO!?!?!?!!!!! uz to mam, ale dal jsem to do puvodni chunks, nahoře
    # to nestacilo. takze kdyby nahodou bylo posledni cislo v nasobku 0, a nebyla tam jinde nula, muselo to byt 5*sude cislo
    else:
        if values[k[-1]][0] == 0:
            if 0 in values[i[-1]][3] and 0 in values[j[-1]][3]:
                values[i[-1]][3].append(3)
                values[i[-1]][3].append(7)
                values[i[-1]][3].append(9)

                values[j[-1]][3].append(3)
                values[j[-1]][3].append(7)
                values[j[-1]][3].append(9)

    return True


def third_largest(i,j,k):
    if len(i) < len(k) and len(j) < len(k):
        return True
    else:
        return False

def ini_dict(dict, letters):
    for i in letters:
        dict[i] = [-1, False, list(), list()]# me, going actually insane dude

def try_values(dict, letters, index, taken):
    if(dict[letters[index]][1]): #hodnota je lockla
        if index != len(letters)-1:
            if try_values(dict, letters, index+1, taken):
                return True
        else:
            if dosad(dict):
                return True

    else:
        for n in dict[letters[index]][2]:
            if taken[n] == False:
                taken[n] = True
                dict[letters[index]][0] = n

                if index != len(letters) - 1:
                    if try_values(dict, letters, index + 1, taken):
                        return True

                else:
                    if dosad(dict):
                        return True

                taken[n] = False

        for i in range(10):
            if i in dict[letters[index]][3] or i in dict[letters[index]][2]:
                continue
            if taken[i] == False:
                taken[i] = True
                dict[letters[index]][0] = i

                if index != len(letters) - 1:
                    if try_values(dict, letters, index+1, taken):
                        return True

                else:
                    if dosad(dict):
                        return True

                taken[i] = False

    return False

def dosad(dict):
    global ar
    for a in ar:

        right = left1 = left2 = 0
        index = 0
        plus = False

        for i in range(len(a)-1, -1, -1):
            if(a[i] == '='):
                right = left2
                left2 = 0
                index = 0
                continue

            elif a[i] == '*':
                index = 0
                left1 = left2
                left2 = 0
                continue

            elif a[i] == '+':
                index = 0
                left1 = left2
                left2 = 0
                plus = True
                continue

            left2 += dict[a[i]][0] * (10**index)
            index += 1

        if plus:
            if(left1+left2) != right:
                return False
        else:
            if (left1 * left2) != right:
                return False

    return True





values = dict()
ar = []

'''input method'!!!!!!!!!!!!!!!!!!!!'''


#readInput("algebrogram.txt", ar)

for l in sys.stdin: ar.append(l.strip())



ar = plus_multiply(ar)
# all in good format and even only + and / operations :) nice

letters = unique(ar)
#print(letters)
# mam všechny pismena a to v abecednim poradi :)

ini_dict(values, letters)
taken = [False]*10

for a in ar:
    if chunk_sizes(a, taken) == False:
        print('NEEXISTUJE')
        exit()

for a in ar:
    if re_chunk_size(a, taken) == False:
        print('NEEXISTUJE')
        exit()

#print(values)
#print(ar)

''' !!!!!!!!!!!!!!!!ok, takže nikdy nejsou na začátku nuly. + je třeba další optimatizace!!!!!!!!!!!!!!!!!!'''
# no fakt dík. teĎ to musim dělat já a ty jsi si byl schrupnout.

if try_values(values, letters, 0, taken):
    for i in range(len(letters)):
        if i == len(letters)-1:
            print(values[letters[i]][0])
        else:
            print(values[letters[i]][0], end = ' ')
else:
    print('NEEXISTUJE')

