
def cull(ar, goal):
    for i in range(len(ar)):
        if ar[i] > goal:
            ar = ar[:i]

def najdi(ar, goal):
    current = 0
    for depth in range(len(ar)):
        for i in range(len(ar)):
            current = ar[i]

            p = plus(ar, goal, current, i, depth)
            if p[0] == True:
                return (True, [(ar[i])]+ p[1])

            m = mul(ar, goal, current, i, depth)
            if m[0] == True:
                return (True, [(ar[i])] + m[1])


def plus(ar, goal, current, i, depth):
    c = '+'
    i+=1
    current += ar[i]

    if current == goal:
        return (True, [c, ar[i]])

    if depth <= i:
        return (False, [0])

    for j in range(i, len(ar)):
        p = plus(ar, goal, current, j, depth)
        if p[0] == True:
            return (True, [c, ar[i]]+p[1])

        m = mul(ar, goal, current, j, depth)
        if m[0] == True:
            return (True, [c, ar[i]]+m[1])



def mul(ar, goal, current, i, depth):
    c = '*'
    i+=1
    current *= ar[i]

    if current == goal:
        return (True, [c, ar[i]])

    if depth <= i:
        return (False, (0))

    for j in range(i, len(ar)):
        p = plus(ar, goal, current, j, depth)
        if p[0] == True:
            return (True, [c, ar[i]]+m[1])

        m = mul(ar, goal, current, j, depth)
        if m[0] == True:
            return (True, [c, ar[i]]+m[1])


# main
ar = []
for a in input().strip().split():
    ar.append(int(a))
del a

goal = int(input())
ar.sort()


cull(ar, goal)

output = najdi(ar, goal)
for a in output[1]:
    print(a, end = ' ')

