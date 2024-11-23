def hello():
    print("hello")


#vrati list ve kterem jsou radky v txt jakozto polozky pole, stripne
def read_input(name):
    ar=list()
    if name != None:
        file = open(name, "rt")
        while True:
            line = file.readline().strip()
            if line != '':
                ar.append(line)
            else:
                break
    file.close()
    return ar

def split_pole(ar):
    for i in range(len(ar)):
        ar[i] = ar[i].split()


def list_all_to_int(ar):#vezme list ve kterem jsou cisla ve frome str/int/flt.. asi jakkoliv actually a listy cisel a vse da do intu
    if type(ar) == list:
        for i in range(len(ar)):
            if type(ar[i]) != list:
                ar[i] = int(ar[i])
            else:
                list_all_to_int(ar[i])