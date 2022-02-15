from colorama import*
init()
import random, time, sys
def film(x):
	print("You have chosen the movie rocky",x)
def timeStart(a):
	print("Show starts at",a)
def SetFilm(a,b,c,d):
	print("Sekect a movie:\n1)",a,"\n2)",b,"\n3)",c,"\n4)",d)
def TypeFilm(a):
	print("You have chosen a genre of",a)
def SetFilm2(a,b,c,d,q):
	while True: 
		q = int(input("\nFilm № "))
		if q == 1:
			print(a)
			q=a
		elif q == 2:
			print(b)
			q=b
		elif q ==3:
			print(c)
			q=c
		elif q ==4:
			print(d)
			q=d
		else:
			print("Input error. Try again")
		return q
f1="Ghostbusters"
f2="Back to the Future"
f3="Stars Wars"
f4="Alien"
f5="Jaws"
f6="Disappearance"
f7="Hour Wolf"
f8="Die Hard"
f9="Matrix"
f10="Fight Club"
f11="The Godfather"
f12="Shine"
f13="The Shawshank Redemption"
tf1="Horrors"
tf2="Fiction"
tf3="Action"
tf4="Drama"
t1=random.randint(5,9)
t2=random.randint(10,14)
t3=random.randint(15,19)
t4=random.randint(20,24)
modelcard = {'3':'American Express','4':'Visa','5':'MastemCard','6':'China UnionPay'}
price=0
c=0
animation = ("[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]")
print(Fore.MAGENTA+"WELCOME TO THE KINONIA"+Fore.WHITE)
while True: 
	print("Choose a movie genre:\n1)",tf1,"\n2)",tf2,"\n3)",tf3,"\n4)",tf4)
	type = int(input("\nGenre "))
	if type == 1:
		TypeFilm(tf1)
		type=tf1
		break
	elif type== 2:
		TypeFilm(tf2)
		type=tf2
		break
	elif type ==3:
		TypeFilm(tf3)
		type=tf3
		break
	elif type ==4:
		TypeFilm(tf4)
		type=tf4
		break
	else:
		print(Fore.RED+"Input error. Try again"+Fore.WHITE)
if(type==tf1):
	SetFilm(f4,f5,f6,f7)
	c=SetFilm2(f4,f5,f6,f7,c)
elif(type==tf2):
	SetFilm(f1,f2,f3,f4)
	c=SetFilm2(f1,f2,f3,f4,c)
elif(type==tf3):
	SetFilm(f1,f3,f8,f9)
	c=SetFilm2(f1,f3,f8,f9,c)
elif(type==tf4):
	SetFilm(f10,f11,f12,f13)
	c=SetFilm2(f10,f11,f12,f13,c)
else:
	pass
if (c == f1,f5,f6,f7,f12):
	price+=8.50
else:
	pass
if (c == f2,f3,f4,f8,f10,f11,f13):
	price+=10
else:
	pass
print("Select the appropriate session time:\n1)",t1,"\n2)",t2,"\n3)",t3,"\n4)",t4)
while True:
	tt = int(input("\nTime №"))
	if tt == 1:
		timeStart(t1)
		tt=t1
		price-=1.00
		break
	elif tt== 2:
		timeStart(t2)
		tt=t2
		break
	elif tt ==3:
		timeStart(t3)
		tt=t3
		break
	elif tt ==4:
		timeStart(t4)
		tt=t4
		price-=1.00
		break
	else:
		print(Fore.RED+"Input error. Try again"+Fore.WHITE)
print("Chosse a seat in the hall:")
zal = [0] * 100
for i in range(len(zal) - 1):
    i = str(i + 1)
    i = int(i)
    zal[i] = random.randint(0,1)
i=1
while i < 100:
	if i==1:
		print(Fore.YELLOW+"1 Row"+Fore.WHITE)
	elif i==26:
		print(Fore.YELLOW+"2 Row"+Fore.WHITE)
	elif i==51:
		print(Fore.YELLOW+"3 Row"+Fore.WHITE)
	elif i==75:
		print(Fore.YELLOW+"4 Row(VIP place)"+Fore.WHITE)
	else:
		time.sleep(0);
	if zal[i]==1:
		print (Fore.RED + str(zal[i]),"=",i,"Seat" + Fore.WHITE)
		i=i+1
	else:
		print (Fore.GREEN + str(zal[i]),"=",i,"Seat" + Fore.WHITE)
		i=i+1
print(Fore.GREEN+"\nGreen"+Fore.WHITE+" - place is free")
print(Fore.RED +"Red"+Fore.WHITE+" - place is occupided")
while True:
	z = int(input("\nChoose an free seat it the hall №"))
	if zal[z] ==0:
		print(Fore.GREEN+"Place is free"+Fore.WHITE)
		if z>=75:
			price+=15.00
		break
	else:
		print(Fore.RED+"This place is occupied. Choose a location again."+Fore.WHITE)
while True:
	print("Learn more about seating arrangements\nNeed help?\n1)Yes\n2)No")
	m=int(input("Select an option"))
	if (m == 1):
		print("\n          Screen")
		print("-------------------------\n")
	p=0
	for j in range(4):
		for k in range(25):
			p+=1
			if (p==z):
				print(Fore.GREEN+"#",end=""+Fore.WHITE)
				continue
			else:
				pass
			print("*",end="")
		print("<",j+1,"Row")
	break
	if (m == 2):
		break
	else:
		pass
print("Do you want to make an online ticked purchase?\n1)Yes\n2)No\nTo be paid ",price)
while True:
	nub=int(input("Select an option"))
	if ( nub == 1):
		while True:
			card = input("Enter the card number\n")
			q = 0
			counter = 0
			for i in card:
				if i.isdigit():
					counter+=1
				else:
					pass
			if (counter == 16):
				break
			else:
				print("Error input. Try again")
		q=int(card)
		q=q//1000000000000000
		if ( q == 3 ):
			print(modelcard ['3'])
		elif ( q == 4 ):
			print(modelcard ['4'])
		elif ( q == 5 ):
			print(modelcard ['5'])
		elif ( q == 6):
			print(modelcard ['6'])
		else:
			pass
		while True:
			data = list(map(int,input('Enter the card expiration date separeted by a space ').split()))
			if (((data[0] > 0) | (data[0] <= 12))&(data[1] >= 21)):
				break
			else:
				print("Card expired. Try again")
		if nub == 1:
			print("PASS generation")
			for i in range(len(animation)):
				time.sleep(0.4)
				sys.stdout.write("\r" + animation[i % len(animation)])
				sys.stdout.flush()
			pas=''
			for x in range(16): #Количество символов (16)
				pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ$@%&*'))
		else:
			time.sleep(0.00001)
		print(Fore.GREEN+"\nPass has been created"+Fore.WHITE)
		print("Your PASS ",pas)
		print("Do not show your PASS to anyone's faces")
		price = "Paid"
		break
	elif ( nub == 2):
		break
	else:
		print("Error ")
print("\nYou have chosen a movie:",c,"\nGenre of:",type,"\nSession start in ",tt,"\nYour seat №",z,"\nto be paid:",price,"\nNice view!")