def fib(n, m, pocet):
    print(n)
    if pocet == 0:
        return n
    pocet -= 1
    n = m+n
    return(fib(m, n, pocet))


pocet = 100
print(fib(0, 1, pocet))
