'''  1000 <= a < 10000, a = b**3 + c**3, a je nejmenši takhle ziskatelne cislo'''

nejmensi = 10000
count = 1

for i in range(11):
    for j in range(i, 11):
        cislo = (i**3)+(j**3)
        if cislo >= 1000 and cislo < 10000:
            print(count, cislo)
            count += 1
            if cislo < nejmensi:
                nejmensi = cislo

print(nejmensi)

# je to 1000 -> 10**3 + 0**3, když o je v přirozených čislech, jinak je to 1001