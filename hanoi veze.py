ga = []
gb = []
gc = []

l = 10
for i in range(l):
    ga.append(l-i)

# má z a přesouvat na c, b je pomocná
def hanoi(n,  a,b,c):
    if n <= 0:
        return
    hanoi(n-1, a,c,b)
    disk = a.pop()
    c.append(disk)
    print(ga,gb,gc)
    hanoi(n-1, b,a,c)
    


hanoi(len(ga), ga,gb,gc)
