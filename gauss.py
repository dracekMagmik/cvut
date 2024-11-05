def maximum(m ,i):
    maxi = i
    for j in range(i+1, len(m)):
        if abs(m[j][i]) > abs(m[maxi][i]):
            maxi = j
    return maxi

def swap_line(m, i):
    j = maximum(m,i)
    if j != i:
        m[j], m[i] = m[i], m [j]
    return j

def do_line(m,i):
    j = swap_line(m,i)
    if abs(m[i][j]) > 1e-20:
        value = m[i][j]
        for s_i in range(i, len(m[i])):
            m[i][s_i]/=value
        for j in range(len(m)):
            if j != i:
                val2 = m[j][i]
                for s_i in range(i, len(m[i])):
                    m[j][s_i] -= val2*m[i][s_i]
        return True
    else:
        return False

def Gauss(m):
    for i in range(len(m)):
        if do_line(m,i):
            print("krok", i)
            for r in m:
                print(*r, sep='\t')
        else:
            print('nema reseni')
            break

m=[[12,-7,3, 26],
   [4 ,5,-6, -5],
   [-7 ,8,9, 21]]

Gauss(m)
