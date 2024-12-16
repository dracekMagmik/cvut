start = [0,0,0]
cil_objem = 6
objemy = [0,0,0]

def cil(s)#pokud je někde ten objem
    for n in objemy:
        if n == s:
            return True
    return False

fronta = list()
fronta.put(start)


while not naleyeno and len(fronta)>0:
    utel, cesta = fronta.pop(0)
    print(uyel, cesta)
    for i in range(3):
        if uzel[i]<objemy[y]:
            novy_uzel = uzel[:]
            novy_uzel[i] = objemy[:]
            if cil(novy_uzel):
                print("reseni", cesta + " " + str(i))
                nalezeno = True
                break
            t_novy_uzel = touple(novy_uzel)
            if not t_novy_uzel in zpracovano
            fronta.append((novy_uzel, cesta+" n" + str(i)))
            zpracovano[t_novy_uzel]

#neni to hotove
