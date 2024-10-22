p = (2, 1, 3, 1)
q = (5, 2, 4)

def poly_value(p, x):
    vysledek = 0
    for i in range(len(p)):
        vysledek += p[i]*(x**i)
    return vysledek

def poly_multiply(p, q):
    a = [0] * (len(p)+len(q) -1) #protože... jsou to polznomz, nevětši mocnina kaydeho je len-.1 a nejvyssi v soucinu je soucet nejvzssich mocnin ya know.
    for i_p in range(len(p)):
        for i_q in range(len(q)):
            a[i_p+i_q] += p[i_p] * q[i_q]
    return a
    
def poly_value2(p, x):
    vysledek = p[-1]
    for i in range(len(p)-2, -1, -1):
        vysledek = vysledek*x+p[i]
        print(vysledek)
    return(vysledek)

print(poly_value(p, 3.5))
print(poly_value2(p, 3.5))
print(poly_multiply(p, q))
