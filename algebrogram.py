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
def chunk_sizes(str):
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

    if plus:
        if(third_largest(i,j,k)):
            values[k[0]] = (1, True)

def third_largest(i,j,k):
    bigger = False
    if len(i) < len(k) and len(j) < len(k):
        return True
    else:
        return False

def ini_dict(dict, letters):
    for i in letters:
        dict[i] = [-1, False]

def diff_vals(dict, letters, taken): # koukne, zda jsou vsechny lockly hodnoty jiny
    for i in letters:
        if (dict[i][1]):
            if(taken[dict[i][0]] == False):
                taken[dict[i][0]] = True
                continue
            else:
                return False
    return True

def try_values(dict, letters, index, taken):
    if(dict[letters[index]][1]): #hodnota je lockla
        if index != len(letters)-1:
            if try_values(dict, letters, index+1, taken):
                return True
        else:
            if dosad(dict):
                return True

    else:
        for i in range(10):
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

'''ar = list()
readInput("algebrogram.txt", ar)'''

ar = []
for l in sys.stdin:
    ar.append(l.strip())

ar = plus_multiply(ar)
# all in good format and even only + and / operations :) nice

letters = unique(ar)
#print(letters)
# mam všechny pismena a to v abecednim poradi :)

ini_dict(values, letters)

for a in ar:
    chunk_sizes(a)

# dve stejne lockle hodnoty
taken = [False]*10
if(diff_vals(values, letters, taken) == False):
    print('NEEXISTUJE')
    exit()

#print(values)
#print(ar)

''' !!!!!!!!!!!!!!!!ok, takže nikdy nejsou na začátku nuly. + je třeba další optimatizace!!!!!!!!!!!!!!!!!!'''

if try_values(values, letters, 0, taken):
    for i in range(len(letters)):
        if i == len(letters)-1:
            print(values[letters[i]][0])
        else:
            print(values[letters[i]][0], end = ' ')
else:
    print('NEEXISTUJE')