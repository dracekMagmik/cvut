def abs(n): # n jako number
    if n >= 0:
        return n
    else:
        return n*(-1)

a = 5
print("absolutni hodnota z", a, "je" , abs(a))
a = -5
print("absolutni hodnota z", a, "je" , abs(a))