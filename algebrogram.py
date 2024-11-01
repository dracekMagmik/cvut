#import library.mylib as lib
#lib.LoL()

def readInput(name, array):
    f = open(name, "rt")
    while True:
        line = f.readline().strip()
        if line != '':
            array.append(line)
        else:
            break

def unique(ar):
    for a in ar:
        for i in range(len(a)):
            if ord(a[i]) > 64 and ord(a[i]) < 91:
                letters.add(a[i])


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
            values[i[0]] = (1, True)



def third_largest(i,j,k):
    bigger = False
    if len(i) < len(k) and len(j) < len(k):
        return True
    else:
        return False


letters = set()
values = dict()
ar = []
readInput("algebrogram.txt", ar)
ar = plus_multiply(ar)
# all in good format and even only + and / operations :) nice

unique(ar)

print(letters)

for a in ar:
    chunk_sizes(a)


print(ar)

