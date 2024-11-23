import time

def fill(a, x_in, y_in, fronta):
    pole = []
    pole.append((x_in,y_in,2)) #hodim dovnitr dvojici
    #s pop() je to zasobnik, fronta ma pop(0)
    a[y_in][x_in] = 2
    while len(pole) >0:
        for radek in a: print(radek)

        if fronta: print("----------------" + "f")
        else: print("----------------" + "z")
        time.sleep(0.5)
        
        if fronta:
            x,y,val = pole.pop(0)
        else:
            x,y,val = pole.pop()
            
        
        
        if x+1 < len(a[0]) and a[y][x+1]==0:
            pole.append((x+1,y, val))
            a[y][x+1] = val
            
        if x-1 >= 0 and a[y][x-1]==0:
            pole.append((x-1,y,val))
            a[y][x-1] = val
            
        if y+1 < len(a) and a[y+1][x]==0:
            pole.append((x,y+1,val))
            a[y+1][x] = val
            
        if y-1 >=0 and a[y-1][x]==0:
            pole.append((x,y-1,val))
            a[y-1][x] = val
            
    return a


m=[
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,1,0,1,0,0,0,1],
[0,0,1,0,0,0,1,0,1,0],
[0,0,1,0,0,0,0,1,0,0],
[0,0,1,1,0,1,0,0,0,0],
[0,0,1,0,1,1,1,1,0,0],
[0,0,1,0,0,1,0,1,1,1],
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0,0] ]
n=[
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,1,0,1,0,0,0,1],
[0,0,1,0,0,0,1,0,1,0],
[0,0,1,0,0,0,0,1,0,0],
[0,0,1,1,0,1,0,0,0,0],
[0,0,1,0,1,1,1,1,0,0],
[0,0,1,0,0,1,0,1,1,1],
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0,0] ]

m = fill(m,4,4, False)
n = fill(n,4,4, True)



