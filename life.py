import time

a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
     [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   ]

def krok(a): # veme pole a vrati pole o krok dál
    out = []
    out = [[0]*len(i) for i in a]

    for rad in range(len(a)):
        for slo in range(len(a[0])):
            living = 0
            '''for r_i in range(-1, 2):
                for s_i in (-1, 0, 1):
                    # modulem zabranime tomu, abz tam skocilo index out of range, nyni je to toroid
                    living += a[(rad+r_i)%len(a)][(slo+s_i)%len(a[0])] 
                living -= a[rad][slo]'''
            for(r_i, s_i) in [[-1,-1], [-1,0], [-1,1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                living += a[(rad+r_i)%len(a)][(slo+s_i)%len(a[0])]
                
            if living == 3 or (living == 2 and a[rad][slo] == 1):
                out[rad][slo] = 1
                
    return(out)

for i in range(5000):
    #pro velke pole bz to chtelo mit dve velke, ktere se budou stridat-> nebudou se tvorit nove *pametove stabilni*
    for r in a:
        print(''.join('X' if j != 0 else ' ' for j in r))
    a = krok(a)
    time.sleep(0.5)
    print('--------------' + str(i) + '--------------')
    
    
