import time

a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   ]

b = a

prehod = True

def krok(inn, out): # veme pole a vrati pole o krok dál
    for i in range(len(out)):
        for j in range(len(out[0])):
            out [i][j] = 0
            
    for rad in range(len(inn)):
        for slo in range(len(inn[0])):
            living = 0
            for r_i in range(-1, 2):
                for s_i in (-1, 0, 1):
                    # modulem zabranime tomu, abz tam skocilo index out of range, nyni je to toroid
                    living += inn[(rad+r_i)%len(inn)][(slo+s_i)%len(inn[0])]
            living -= inn[rad][slo]
            '''for(r_i, s_i) in [[-1,-1], [-1,0], [-1,1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                living += a[(rad+r_i)%len(a)][(slo+s_i)%len(a[0])]
                
            if living == 3 or (living == 2 and a[rad][slo] == 1):
                out[rad][slo] = 1'''

            if living == 3:
                out[rad][slo] = 1

for i in range(5000):
    #pro velke pole bz to chtelo mit dve velke, ktere se budou stridat-> nebudou se tvorit nove *pametove stabilni*
    if prehod:
        for r in b:
            print(''.join('X' if j != 0 else ' ' for j in r))
        krok(a, b)
        print(b)
        prehod = False
    else:
        for r in a:
            print(''.join('X' if j != 0 else ' ' for j in r))
        krok(b, a)
        print(a)
        prehod = True
    
    time.sleep(0.5)
    print('--------------' + str(i) + '--------------')
    
    
