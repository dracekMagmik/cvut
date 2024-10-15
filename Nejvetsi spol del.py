def nsd(a, b):
    if a <b:
        a,b=b,a
    while b!=0:
        a, b = b, a%b
    return a

print(10, 15, nsd(10, 15))
print(154435576, 13127023965, nsd(154435576, 13127023965))
