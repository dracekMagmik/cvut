
class point:
    x = 0
    y= 0
    
    def __init__(self, x,y):
        self.x = x
        self.y =y

    def distance(self):
        return (self.x*self.x+ self.y*self.y)

    def Tdistance(self,t):
        return (t[0]-self.x)*(t[0]-self.x)+ (t[1]-self.y)*(t[1]-self.y)
    

vstup = list(map(float, input().split(" ")))
points = []

#print(vstup)

for i in range(0, len(vstup), 2):
    points.append(point(vstup[i], vstup[i+1]))

teziste = [0,0]

for i in range(len(points)):
    teziste[0] += points[i].x
    teziste[1] += points[i].y

teziste[0] /=i+1
teziste[1] /=i+1

#print(teziste)
# teziste done

Tnej  = 1000
Ti = 0
delky = []
for i in range(len(points)):
    Tnew = points[i].Tdistance(teziste)
    new = points[i].distance()
    delky.append((new, i))
    #print(str(new) + " " + str(points[i].x) + " " +str(points[i].y) + " " + str(nejblize))
    if  Tnew < Tnej:
        Tnej = Tnew
        Ti = i

def a(t):
    return(t[0])

#print(delky)
delky.sort(key = a)
#print(delky)

print(Ti, delky[len(points)//2-1][1])

'''
print("nejblizsi: " + str(points[index ].x) + str(points[index ].y))
'''
