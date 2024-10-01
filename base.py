zaklad = int(input())

# cisla jako 0-9 + a-z -> 0-9 + 97 - 122
a = input()
b = input()
c = input()


def CheckNum(a): # koukne yda to jsou spravne znaky atd
    tecka = False
    for letter in a:
        letter_ord = ord(letter)
        if letter_ord > 47 and letter_ord < 58:# cislo < 10
            if int(letter) > zaklad-1:# moc velke cisl pro zaklad
                return False
            
        elif zaklad > 9 and letter_ord > 96 and letter_ord < 123:# cislo > 10
            if letter_ord - 97 > zaklad-10: # moc velke cislo pro zaklad
                return False

        elif letter_ord == 46: # tecka
            if tecka: # najde druhou tečku
                return False
            tecka = True
        else:
            return False
        
    return True            


if !CheckNum(a) or !CheckNum(b) or !CheckNum(c): # konec, pokud blbe
    print(ERROR)
    exit

# a+b-c



