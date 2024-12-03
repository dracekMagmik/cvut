import sys

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
    file.close()
    return ar

def find_postfix(ar, konc):
    pocet_fix = 0
    krat = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    for a in ar:
        for i in range(1, len(konc)):
            if a[i*-1] == konc[i*-1]:
                pass
            else:
                break
            
            if i == (len(konc)-1):
                pocet_fix += 1

                if len(a) < len(krat):
                    krat = a
                    
                    
    if pocet_fix == 0:
        krat = None
    return pocet_fix, krat
                



path = sys.argv[1]
koncovka = sys.argv[2]

ar = read_input(path)
#ar = knihovnica.read_input("text.txt")

count, nej = find_postfix(ar, koncovka)

print(count)
print(nej)


