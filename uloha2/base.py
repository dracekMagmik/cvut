zaklad = int(input())

# cisla jako 0-9 + a-z -> 0-9(48-57) + a-z(97 - 122)

input1 = input().strip()
input2 = input().strip()
input3 = input().strip()


def CheckNum(a): # koukne zda to jsou spravne znaky atd

	if len(a) == 1 and a[0]=='.':
		return False
	
	tecka = False
	for letter in a:
		letter_ord = ord(letter)
		if letter_ord > 47 and letter_ord < 58:# cislo < 10
			if int(letter) > zaklad-1:# moc velke cisl pro zaklad
				return False

		elif zaklad > 9 and letter_ord > 96 and letter_ord < 123:# cislo >= 10
			if letter_ord - 97 > zaklad-11: # moc velke cislo pro zaklad
				return False

		elif letter_ord == 46: # tecka
			if tecka: # najde druhou tečku
				return False
			else:
				tecka=True

	return True            

#prevede do privetijsi hodnoty(vsecko soupnu od 48 do(58+(122-97))) <=> a = 58, z =83
def zmensi(s):
	novy_str =''
	for letter in s:
		if letter == '.':
			novy_str += letter
		elif ord(letter)>96 and ord(letter)<123:
			novy_str += chr(ord(letter)-39)
		else:
			novy_str += letter
	return novy_str
			
def roztahni(s):#Prevede vysledek zpet na pismena
	new  = ""
	for letter in s:
		if letter =='.':
			new += letter
		elif ord(letter)> 47 and ord(letter) < 58:
			new += letter
		else:
			new += chr(ord(letter)+39)
	return new
	
# obrati string
def obrat(s):
	novy_str=''
	for i in range(len(s)):
		novy_str += s[len(s)-(1+i)]
	return novy_str
			
#doplni 0 na zacatek a konec A i B, tak aby bylo B stejne dloube jako A
def srovnej_delku(a, b):
	
	a_predT = a_zaT = 0
	for i in range(len(a)):
		if a[i] =='.':
			a_predT= i #pocet cisel pred .
			a_zaT = len(a)-(1+i)#pocet za .
			break
		elif i == len(a)-1:
			a_predT  = len(a)
			a += '.'
			
	b_predT = b_zaT = 0
	for i in range(len(b)):
		if b[i] =='.':
			b_predT= i #cisla pred . v b
			b_zaT = len(b)-(1+i)#cisla za . v b
			break
		elif i == len(b)-1:
			b_predT = len(b)
			b+= '.'


	#vyrovnani pred teckou
	if a_predT > b_predT:
		b = ('0'*(a_predT-b_predT)) + b
	elif a_predT < b_predT:
		a = ('0'*(b_predT-a_predT)) + a
		
	#vytovnani za teckou
	if a_zaT > b_zaT:
		b += '0'*(a_zaT - b_zaT)
	elif b_zaT > a_zaT:
		a += '0'*(b_zaT - a_zaT)

	return(a, b)

	#return a + '!' + b#desperation taken form
	# nevermind, thanks lecture dude
	
#program
if  not (CheckNum(input1) and CheckNum(input2) and CheckNum(input3)):  
	#konec, kdyz zlobi
	print('ERROR')
	exit()
#po sem ok

if input1 != input2:
	input1, input2 = srovnej_delku(input1, input2)

#sem ok :)

input1 = obrat(zmensi(input1))
input2 = obrat(zmensi(input2))
input3 = obrat(zmensi(input3))
#sem kk, puda pripravena pojdme pocitat
#"no waiter, this input is not perfect enough, eugh"" no more

vysledek =''
preteceni = 0


for i in range(len(input1)): # len(in1) == len(in2)
	if input1[i] != '.':
		soucet =ord(input1[i])+ord(input2[i])+preteceni-96
		vysledek += chr((soucet%zaklad)+48)
		preteceni = soucet//zaklad
	else:
		vysledek += '.'

if preteceni != 0:
	vysledek += chr((preteceni)+48)

#print(obrat(roztahni(vysledek)))

#scita woohoo, makin bacon *tf2 engineer dance*
if input1 != input3:
	input1, input3 = srovnej_delku(vysledek, input3)

minus = False
if obrat(input3)> obrat(input1):#strnigs that are numbers so this works ok :)
	minus = True
	input2=input3
	input3=input1
	input1=input2

vysledek = ""
preteceni = 0

for i in range(len(input1)):
	if input1[i] == '.' or False:
		vysledek += '.'
	else:
		rozdil = ord(input1[i])-ord(input3[i])-preteceni # preteceni odecte jednicku kdyby náhodou
		preteceni = 0
		if rozdil < 0:
			rozdil = rozdil + zaklad
			preteceni = 1
		vysledek += chr((rozdil+48))
if preteceni != 0:
	vysledek += '1'

vysledek = obrat(roztahni(vysledek)).strip('0')

if vysledek[0] == '.':
	vysledek = '0' + vysledek

if minus:
	print('-' + vysledek)
else:
	print(vysledek)