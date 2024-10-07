y = float(input())

x_changes = 0

x1 = x2 = 0

if y > 1:
    x2 = y
elif y< -1:
    x1 = y
else:
    x1 = -1
    x2 = 1

x_dot = 0
presnost = 10**-8

def Dosazeni(x):
    return (x**3)-y

def Abs(number):
    if number < 0:
        number *= -1
    return number

while Abs(x1-x2) >= presnost:
    x_dot = (x1 + x2) / 2
    if(Dosazeni(x_dot) > 0):
        x2 = x_dot
        x_changes += 1
    elif(Dosazeni(x_dot) < 0):
        x1 = x_dot
        x_changes += 1
    else:
        break

print(x_dot)
print("pocet zmen x: " + str(x_changes))