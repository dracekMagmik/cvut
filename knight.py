m=[[0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,4,0], 
   [0,0,0,0,1,0,0,0], 
   [1,1,1,1,1,1,0,0], 
   [1,1,1,1,1,1,0,0], 
   [0,2,0,0,1,1,0,0], 
   [0,0,0,0,0,1,0,0], 
   [0,0,0,0,1,1,0,0]]


for r in range(len(m)):
    for s in range(len(m[0])):
        if m[r][s] == 2:
            start = [r, s]
    
m[start[0]][start[1]] = 3 # tady to znamena ze uz jsem v tom stavu byl

def cil(s): # vrati true pokud hotovo
    return m[s[0]][s[1]] == 4

fronta = [[start, '('+str(start[0]) + ', '+str(start[1])+')']]
konec = False

while not konec and len(fronta) > 0:
    stav, cesta = fronta.pop(0) #bude se to chovat jako fronta
    r = stav[0]
    s = stav [1]
    for dr, ds in ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)):
        if r + dr >= 0 and r+dr < len(m) and s+ds >= 0 and s+ds < len(m[0]):
            if m[r+dr][s+ds]%2 == 0:
                novy_stav = [r+dr, s+ds]
                nova_cesta = cesta + '('+str(novy_stav[0]) + ', '+str(novy_stav[1])+')'
                
                if cil(novy_stav):
                    print(nova_cesta)
                    konec = True
                    break
                
                m[r+dr][s+ds] = 3
                fronta.append([novy_stav, nova_cesta])
    
if not konec:
    print("neex cesta")
