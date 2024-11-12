def binominal(n, k):
    if n <0 or k < 0 or k > n:
        print("nelze")
        return None
    print(n, k)
    if k == 0 or k ==n:
        return 1
    if k == 1 or k ==n-1:
        return n
    return binominal(n-1, k) + binominal(n-1, k-1)

print(binominal(5,4))
