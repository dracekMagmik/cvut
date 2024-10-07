nums = list(map(int, input().split()))

largestStart = 0
lastStart = 0

largestLenght = 0
lastLenght = 0

def GetSize(start, count): 
    # spocita kolik celkem da posloupnost na indexu strat s delkou count
    size = 0
    for i in range(count):
        size += nums[i+start]
    return size


for i in range(len(nums)): # projede všechny čísla
    if nums[i] % 3 == 0: # když je delitelne tremi
        if lastLenght == 0: # a zacina novou posloupnost
            lastStart = i # zapiseme, kde zacina posloupnost
        lastLenght += 1 # pridame jednu delku
        if i != len(nums)-1: # pokud to neni posledni prvek, pokracujeme.
            # u posledniho cisla musime zkontrolovat, zda nebyla poslounost delsi, nez predchoci nejvetsi
            continue

    if lastLenght > largestLenght: # kdyz je posloupnost delsi, prepisu zaznam nejdelsi
        largestLenght = lastLenght
        largestStart = lastStart
    elif lastLenght == largestLenght and GetSize(largestStart, largestLenght) < GetSize(lastStart, lastLenght):
        # stejne dlouhe, ale nove je delsi
        largestLenght = lastLenght
        largestStart = lastStart

    lastLenght = 0 # jsme na konci posloupnost, takze delku soudobe posloupnosti dame an nulu, abychom mohly hcytnou dalsi

print(largestStart, largestLenght, GetSize(largestStart, largestLenght))