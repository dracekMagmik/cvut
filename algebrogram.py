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

ar = []

readInput("algebrogram.txt", ar)
ar = plus_multiply(ar)
# all in good format and even only + and / operations :) nice

print(ar)