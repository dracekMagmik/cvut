import sys
class Card:
    x = -1
    y = -1
    vys = 0
    sir = 0
    vals = []
    colors = []
    def __init__(self, vys, sir, vals, x=-1, y=-1):
        self.x = x
        self.y = y
        self.vys = vys
        self.sir = sir
        self.vals = vals
        for i in range(vys):
            for j in range(sir):
                if vals[i][j] > 0 and  not (vals[i][j] in self.colors):
                    self.colors.append(vals[i][j])

    def print_in_line(self):
        print(self.vys, self.sir, sep=' ', end=' ')
        for i in range(self.vys):
            for j in range(self.sir):
                print(self.vals[i][j], end = ' ')

    def print_in_cube(self):
        print(self.vys, self.sir, sep=' ')
        for i in range(self.vys):
            for j in range(self.sir):
                print(self.vals[i][j], end = ' ')
            print('')

    def spin(self): #rotace o 90° clockwise
        other = []
        for _ in range(self.sir):
            other.append([0]*self.vys)

        for i in range(self.vys):
            for j in range(self.sir):
                other[j][self.vys-1-i] = self.vals[i][j]
        self.vals = other
        self.vys, self.sir = self.sir, self.vys

    def space_check(self, pole, y, x):
        '''if self.x == 1 and self.y == 4:
            print("a")'''

        for i in range(self.vys):
            if y+i >= len(pole) or x+self.sir-1 >= len(pole[0]):
                return False
            elif pole[y+i][x] != -1 or pole[y+i][x+self.sir-1] != -1:
                return False
        for i in range(self.sir):
            if x+i >= len(pole[0]) or y+self.vys-1 >= len(pole):
                return False
            elif pole[y][x+i] != -1 or pole[y+self.vys-1][x+i] != -1:
                return False
        if pole[y +(self.vys//2)][x+(self.sir//2)] != -1:
            return False
        return True

    def try_outside(self, pole, point, control, nalezici):
        #projet tou matici vsechny mozne pozice na tom bodu
        best = (0,0)
        self.y, self.x, colour = point
        '''if point[0] == 4 and point[1] == 15:
            print("now")'''

        while(self.x > point[1]-self.sir+1 and self.x > 0):
            best = self.try_spot(colour, control, nalezici, pole, best, point)
            self.x-=1


        while (self.y > point[0] - self.vys + 1 and self.y > 0):
            best = self.try_spot(colour, control, nalezici, pole, best, point)
            self.y -= 1


        while (self.x < point[1] and self.x < len(pole[0])-1):
            best = self.try_spot(colour, control, nalezici, pole, best, point)
            self.x += 1


        while (self.y < point[0] and self.y < len(pole)-1):
            best = self.try_spot(colour, control, nalezici, pole, best, point)
            self.y += 1


        return best

    def try_spot(self, colour, control, nalezici, pole, best, point):
        '''if self.x == 1 and self.y == 4 and colour == 1:
            print("now")'''
        if colour in self.colors:
            if self.space_check(pole, self.y, self.x):
                new = self.card_in_pole(pole, control, nalezici, point)
                if best[0] < new:
                    best = (new, (self.y, self.x, self.vys, self.sir, self.vals))
        return best

    def card_in_pole(self, pole, control, nalezici, point):
        '''if self.x == 12 and self.y == 1:
            print("a")'''
        skore = 0

        for i in range(self.vys):
            for j in range(self.sir):
                pole[self.y+i][self.x+j] = self.vals[i][j]
                nalezici[self.y+i][self.x+j] = 1000

        for i in range(len(control)):
            for j in range(len(control[0])):
                control[i][j] = 0

        for i in range(self.vys):
            for j in range(self.sir):
                skore += search(self.y + i, self.x + j, pole, control, nalezici)

        for i in range(self.vys):
            for j in range(self.sir):
                pole[self.y+i][self.x+j] = -1
                nalezici[self.y + i][self.x + j] = -1

        for i in range(len(control)):
            for j in range(len(control[0])):
                control[i][j] = 0

        return skore

        #check zda se vejde do pole a dej to tam
        #search
        #spin a opakovat


def check_score(pole, control, nalezici):
    skore = 0
    for i in range(len(pole)):
        for j in range(len(pole[0])):
            if pole[i][j] > 0 and control[i][j] != 1:
                skore += search(i, j, pole, control, nalezici)
    del i, j
    return skore

def search(y, x, pole, control, nalezici):
    pridavam = False
    connected = 1
    id = nalezici[y][x]
    color = pole[y][x]
    if color < 1:
        return 0
    control[y][x] = 1
    stack = [(y,x)]

    while len(stack)>0:
        y,x = stack.pop()

        if nalezici[y][x] != id:
            pridavam = True

        if(y-1 >= 0 and control[y-1][x] != 1 and pole[y-1][x] == color):
            control[y - 1][x] = 1
            stack.append((y-1,x))
            connected+=1

        if(y+1 < len(pole) and control[y+1][x] != 1 and pole[y+1][x] == color):
            control[y + 1][x] = 1
            stack.append((y+1,x))
            connected+=1

        if(x-1 >= 0 and control[y][x-1] != 1 and pole[y][x-1] == color):
            control[y][x-1] = 1
            stack.append((y,x-1))
            connected+=1

        if(x+1 < len(pole[0]) and control[y][x+1] != 1 and pole[y][x+1] == color):
            control[y][x+1] = 1
            stack.append((y,x+1))
            connected+=1

    if pridavam: return connected
    else: return 0

def find_free(y,x, pole):
    free = []
    if y+1 < len(pole) and pole[y+1][x] == -1:
        free.append((y+1,x, pole[y][x]))
    if y > 0 and pole[y-1][x] == -1:
        free.append((y-1,x, pole[y][x]))
    if x+1 < len(pole[0]) and pole[y][x+1] == -1:
        free.append((y,x+1, pole[y][x]))
    if x-1 > 0 and pole[y][x-1] == -1:
        free.append((y,x-1, pole[y][x]))
    return free

file = open(sys.argv[1], 'rt')
#file = open("uloha8/test.txt", 'rt')

poleY, poleX = map(int, file.readline().split())

karta_index = 0
pole = []
checked = []
nalezici = []
for _ in range(poleY):
    checked.append([0]*poleX)
    pole.append([-1]*poleX)
    nalezici.append([-1]*poleX)

polozeno, drzim = map(int, file.readline().strip().split())

for _ in range(polozeno): # lupnu na pole all cards that are there already
    karta = list(map(int, file.readline().strip().split()))
    x0 = karta[1]
    y0 = karta[0]

    for i in range(karta[2]):
        for j in range(karta[3]):
            pole[y0+i][x0+j] = karta[4+(karta[3]*i)+j]
            nalezici[y0+i][x0+j] = karta_index
    del i, j
    karta_index += 1

#for i in range(poleY): print(pole[i])

karty = []

for _ in range(drzim):
    karta = list(map(int, file.readline().strip().split()))
    vals = []

    for _ in range(karta[0]):
        vals.append([0]*karta[1])

    for i in range(karta[0]):
        for j in range(karta[1]):
            vals[i][j] = karta[2+j+i*karta[1]]
    del i, j
    karty.append(Card(karta[0], karta[1], vals))

del karta
#print(check_score(pole, checked[:], nalezici))


#najdu pozice, kde je barva a -1 vedle sebe
join_point = []
for i in range(poleY):
    for j in range(poleX):
        if pole[i][j] > 0:
            if (i-1 > 0 and pole[i-1][j] == -1 ) or (j-1 > 0 and pole[i][j-1] == -1) or (j+1 < len(pole[0]) and pole[i][j+1] == -1) or ( i+1 < len(pole) and pole[i+1][j] == -1):
                join_point.append((i,j, pole[i][j]))
del i, j
# mam vsechny karty, mam body, kde lze napojit cestu mezi kartou a zbytek a mam barvu, ktera tam musi byt

free = []
for point in join_point:
    free += find_free(point[0], point[1], pole)

best = (0,0)

for point in free:
    for karta in karty:
        for _ in range(4):
            new = karta.try_outside(pole, point, checked[:], nalezici)
            if new[0] > best[0]:
                best = new
            karta.spin()

#print(best)
if best == (0,0):
    print("NOSOLUTION")
else:
    print(best[1][0], best[1][1],best[1][2],best[1][3], end=' ')
    for i in range(len(best[1][4])):
        for j in best[1][4][i]:
            print(j, end = ' ')


file.close()