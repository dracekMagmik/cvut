#import library.mylib as lib
#lib.LoL()

def read_input(name):
    ar=list()
    if name != None:
        file = open(name, "rt")
        while True:
            line = file.readline().strip()
            if line != '':
                ar.append(line)
            else:
                break
    else:
        ar.append(input())
        ar.append(input())
        ar.append(input())

    ar[1] = ar[1].split()
    cisla = list()
    for a in range(len(ar[1])):
        cisla.append(int(ar[1][a]))

    ar[1] = cisla
    del cisla

        #vrati pocet radku, sloupcu a velikost podmatic, matici cisel a matici textu
    return int(ar[0].split()[0]),int(ar[0].split()[1]), int(ar[0].split()[2]), delej_matici(ar[1], int(ar[0].split()[0]), int(ar[0].split()[1])), delej_matici(ar[2], int(ar[0].split()[0]), int(ar[0].split()[1]))

def delej_matici(data, radky, sloupce):
    matice = list()
    for i in range(radky):
        matice.append(data[i*sloupce:(i+1)*sloupce])
    print(matice)
    return matice


def res(file_path):
    rad, slp, pod, matice, text = read_input(file_path)
    output = ''
    podmatice = list()
    for i in range(0,slp,pod):
        for j in range(0,rad,pod):
            for k in range(pod):
                podmatice.append(matice[j+k][i:i+pod])
            r, s = nejvetsi(podmatice)
            output += text[r+j][s+i]
            podmatice = list()
    return output

def nejvetsi(matice):
    delka = len(matice)
    hodnota = 0
    Imax = Jmax = 0
    for i in range(delka):
        for j in range(delka):
            soucet = matice[i][j] + matice[(i+1)%delka][j] + matice[(i-1)%delka][j] + matice[i][(j+1)%delka] + matice[i][(j-1)%delka]
            print(soucet)
            if hodnota < soucet:
                hodnota = soucet
                Imax = i
                Jmax = j
    return (Imax, Jmax)






#print(res("uloha5/test3.txt"))
res(None)






