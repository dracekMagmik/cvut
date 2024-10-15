text = input()
target = input()


def my_find(a,b): # oboji string, hledam v nekde v 'a' 'b'
    if len(a) < len(b):
        return -1
    
    for i in range(len(a) - len(b)+1):  #abcd cd -> 4-2 = 2, ok
        if(a[i:i+len(b)] == b):
            return(i)
        
    return -1

def my_replace(a,b,c):
    if len(a) < len(b):
        return -1

    for i in range(len(a)): # asi udělam while, at větší/mensi delka a nema vliv
        if my_find(a[i:].b) != -1:
            #dá tam ten replace
    
print(my_find(text, target))
