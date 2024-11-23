import knihovnica


def Convert(ar): #array
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            if i == 0 or (i != 0 and ar[i-1][j] == 0):
                if ar[i][j] < 0:
                    ar[i][j] = 1
                else:
                    ar[i][j] = 0

            elif ar[i][j] < 0:
                ar[i][j] = ar[i-1][j]+1

            else:
                ar[i][j] = 0

def nejvetsi(ar):
    best = [0, 0, 0, 0] # ulozeni nej vysledku so far
    for i in range(len(ar)):
        pred = [(0, 0)] # stack predchozivh cisel
        po = [(0, 0)] #stack pro nejvetsi mensi cilso za
        mensi_l = [0]*len(ar[i]) # list na index cisel pred
        mensi_p = [0]*len(ar[i]) # na cisla po

        meze(ar, i, pred, po, mensi_l, mensi_p)

        #print(mensi_l, ar[i], mensi_p, ) #fuck yeah! (ok, tak tohle fachá, ty hranice jsou vztyčený, už jen najit ten bjem a je to
        #print(ar[i])

        for j in range(len(ar[i])):
            if ar[i][j] != 0:
                objem = ar[i][j]*(mensi_p[j][1] - mensi_l[j][1] - 1)
                if objem > best[0]:
                    best = [objem, i-ar[i][j]+1, mensi_l[j][1]+1, i, mensi_p[j][1]-1]

    return best


def meze(ar, i, pred, po, mensi_l, mensi_p):
    for j in range(len(ar[i])):
        nove = ar[i][j]
        nov = (nove, j)

        if nove == 0:
            pred = [(0, j)]

        elif nove > pred[-1][0]:
            mensi_l[j] = pred[-1][:]
            pred.append(nov)

        elif nove == pred[-1][0]:
            pred.pop()
            mensi_l[j] = pred[-1][:]
            pred.append(nov)

        else:
            mensi_l[j] = pred_mensi(nove, pred)
            pred.append(nov)


        if nove > po[-1][0]:
            po.append(nov)
        elif nove == po[-1][0]:
            po.append(nov)
        else:
            po_mensi(nove, po, mensi_p, j)
            po.append(nov)

        if j == len(ar[i])-1:
            po_mensi(0, po, mensi_p,j)


def po_mensi(nove, po, mensi_p,j):
    min = (nove, j)

    while nove < po[-1][0]:
        mensi_p[po.pop()[1]] = min

def pred_mensi(nove, pred): # pokud cislo na ktere zrovna koukam je mensi nez posledni ve stacku
    while nove <= pred[-1][0]:
        pred.pop()
    return pred[-1][:]



path = input()
ar = knihovnica.read_input(path)

#ar = knihovnica.read_input("uloha6/smat_4.txt")

knihovnica.split_pole(ar)
knihovnica.list_all_to_int(ar)
Convert(ar)

best = nejvetsi(ar)
print(best[1], best[2])
print(best[3], best[4])
