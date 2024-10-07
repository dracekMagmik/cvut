cislo = float(input())
presnost_des_mist = int(input())
x_changes = 0

if(cislo < 0):
    print("i", end = "")

odmocnina = 0

for i in range (0, (presnost_des_mist *-1)-1, -1):
    while ((odmocnina+(10 ** i)) **3) < cislo:
        odmocnina += 10**i
        x_changes += 1


print(odmocnina)
print("pocet zmen x: " + str(x_changes))