seconds = int(input())

print(str(seconds//(3600*24)) + "dni")
seconds = seconds % (24 * 3600)

print(str(seconds // 3600) + "hodin")

seconds = seconds % 3600

print(str(seconds//60) + "minut")
print(str(seconds % 60) + "sekund")