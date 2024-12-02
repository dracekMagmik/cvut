
def cull(ar, goal):
    if ar[0] == goal:
        ar = [ar[0]]
        return
    for i in range(len(ar)):
        if ar[i] > goal:
            ar = ar[:i]

def najdi(ar, goal):
    current = 0
    for depth in range(len(ar)):
        for i in range(len(ar)):
            #current = ar[i]

            for j in range(i, len(ar)-1):
                p = plus(ar, goal, current, j-1, 0, depth)
                if p[0] == True:
                    return (True, p[1][1:])
                del p

                m = mul(ar, goal, current, j-1, 0, depth)
                if m[0] == True:
                    return (True, m[1][1:])
                del m

    return (False, [0])


def plus(ar, goal, current, i, depth, strop):
    c = '+'
    i+= 1
    depth += 1

    #if depth == 3 and current == 305 and  i == 15:
       # print(current)

    current += ar[i]

   # if depth == 1 and current == 5:
       # print(current)

   # if depth == 2 and current == 305:
       # print(current)

    if current == goal:
        return (True, [c, ar[i]])
    elif current > goal:
        current -= ar[i]
        return (False, [0])

    if depth > strop:
        current -= ar[i]
        return (False, [0])

    for j in range(i, len(ar)-1):
        p = plus(ar, goal, current, j, depth, strop)
        if p[0] == True:
            return (True, [c, ar[i]]+p[1])
        else:
            #current -= ar[i]
            pass
        del p

        m = mul(ar, goal, current, j, depth, strop)
        if m[0] == True:
            return (True, [c, ar[i]]+m[1])
        else:
            #current -= ar[i]
            pass
        del m

    return (False, [0])



def mul(ar, goal, current, i, depth, strop):
    c = '*'
    i+=1
    depth += 1

    if i >= len(ar):
        if current == goal:
            return (True, [])
        else:
            return (False, [0])

    current *= ar[i]

    if current == goal:
        return (True, [c, ar[i]])
    elif current > goal:
        current //= ar[i]
        return (False, [0])


    if depth > strop:
        current //= ar[i]
        return (False, [0])


    for j in range(i, len(ar)-1):
        p = plus(ar, goal, current, j, depth, strop)
        if p[0] == True:
            return (True, [c, ar[i]]+p[1])
        else:
            pass
            #current //= ar[j]
        del p

        m = mul(ar, goal, current, j, depth, strop)
        if m[0] == True:
            return (True, [c, ar[i]]+m[1])
        else:
            pass
            #current //= ar[j]
        del m

    return (False, [0])


# main
ar = []
for a in input().strip().split():
    ar.append(int(a))
del a

goal = int(input())

ar.sort()

cull(ar, goal)

output = najdi(ar, goal)
if output[0] == True:
    for a in output[1]:
        print(a, end = ' ')
else:
    print("NEEXISTUJE")

