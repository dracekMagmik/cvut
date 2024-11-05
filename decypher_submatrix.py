#import library.mylib as lib
#lib.LoL()

def readInput(name):
    ar=list()
    file = open(name, "rt")
    while True:
        line = file.readline().strip()
        if line != '':
            array.append(line)
        else:
            break
    return(ar)


readInput("uloha5/test1.txt", ar)
print(ar)


