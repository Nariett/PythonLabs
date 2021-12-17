from colorama import*
init()
import random, time, sys
def film(x):###Функция для вывода фильма
	print("Вами выбран фильм",x)
def timeStart(a):###Функция для вывода временени
	print("Время начала сеанса в",a,"часа(ов)")
def SetFilm(a,b,c,d):
	print("Выберите фильм:\n1)",a,"\n2)",b,"\n3)",c,"\n4)",d)
def TypeFilm(a):
	print("Вы выбрали жанр",a)
def SetFilm2(a,b,c,d,q):
	while True: 
		q = int(input("\nФильм № "))
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
			print("Ошибка ввода. Повторите попытку ввода")
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
tf1="Ужасы"
tf2="Фантастика"
tf3="Боевик"
tf4="Драма"
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
	print("Выберите жанр фильма:\n1)",tf1,"\n2)",tf2,"\n3)",tf3,"\n4)",tf4)
	type = int(input("\nЖанр "))
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
		print(Fore.RED+"Ошибка ввода. Повторите попыкту ввода"+Fore.WHITE)
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
	exit(0)
	print("Ошибка программы")
if (c == f1,f5,f6,f7,f12):
	price+=8.50
if (c == f2,f3,f4,f8,f10,f11,f13):
	price+=10
print("Выберите подходящее время сеанса:\n1)",t1,"\n2)",t2,"\n3)",t3,"\n4)",t4)
while True:
	tt = int(input("\nВремя №"))
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
		print(Fore.RED+"Ошибка ввода. Повторите попыкту ввода"+Fore.WHITE)
print("Выберите место в зале:")
zal = [0] * 100##Создание списка
for i in range(len(zal) - 1):
    i = str(i + 1)
    i = int(i)
    zal[i] = random.randint(0,1)
i=1
while i < 100:
	if i==1:
		print(Fore.YELLOW+"1 Ряд"+Fore.WHITE)
	elif i==26:
		print(Fore.YELLOW+"2 Ряд"+Fore.WHITE)
	elif i==51:
		print(Fore.YELLOW+"3 Ряд"+Fore.WHITE)
	elif i==75:
		print(Fore.YELLOW+"4 Ряд(VIP-Места)"+Fore.WHITE)
	else:
		time.sleep(0);
	if zal[i]==1:
		print (Fore.RED + str(zal[i]),"=",i,"Место" + Fore.WHITE)
		i=i+1
	else:
		print (Fore.GREEN + str(zal[i]),"=",i,"Место" + Fore.WHITE)
		i=i+1
print(Fore.GREEN+"\nЗеленый"+Fore.WHITE+" - место свободно")
print(Fore.RED +"Красный"+Fore.WHITE+" - место занято")
while True:
    z = int(input("\nВыберите свободное местов зале №"))
    if zal[z] ==0:
        print(Fore.GREEN+"Место свободно"+Fore.WHITE)
        if z>=75:
        	price+=15.00
        break
    else:
        print(Fore.RED+"Данное место занято. Выберите место повторно."+Fore.WHITE)
while True:
	print("Узнать подробность о рассадке\nНужна помощь?\n1)Да\n2)Нет")
	m=int(input("Введите вариант "))
	if (m == 1):
		print("\n          Экран")
		print("-------------------------\n")
	p=0
	for j in range(4):
		for k in range(25):
			p+=1
			if (p==z):
				print(Fore.GREEN+"#",end=""+Fore.WHITE)
				continue
			else:
				time.sleep(0)
			print("*",end="")
		print("<",j+1,"Ряд")
	break
	if (m == 2):
		break
	else:
		time.sleep(0)
print("Хотите совершить онлайн покупку билета?\n1)Да\n2)Нет\nК опалате ",price)
while True:
	nub=int(input("Выберите вариант "))
	if ( nub == 1):
		while True:
			card = input("Введите номер карты\n")
			q = 0
			counter = 0
			for i in card:
			    if i.isdigit():
			        counter+=1
			    else:
			    	time.sleep(0)
			if (counter == 16):
				break
			else:
				print("Ошибка ввода. Повторите попытку")
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
			print("Ошибка ввода карты. Перезапустите программу.")
			exit(0)
		while True:
			data = list(map(int,input('Введите срок действия карты через пробел ').split()))
			if (((data[0] > 0) | (data[0] <= 12))&(data[1] >= 21)):
				break
			else:
				print("Карта просроченна. Повторите попытку ввода")
		if nub == 1:
			print("Генерая PASS ID")
			for i in range(len(animation)):
				time.sleep(0.4)
				sys.stdout.write("\r" + animation[i % len(animation)])
				sys.stdout.flush()
			pas=''
			for x in range(16): #Количество символов (16)
				pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ$@%&*'))
		else:
			time.sleep(0.00001)
		print(Fore.GREEN+"\nID-pass готов"+Fore.WHITE)
		print("Ваш ID-pass ",pas)
		print("Не показывайте свой PASS ID 3-лицам")
		price = "Оплачено"
		break
	elif ( nub == 2):
		break
	else:
		print("Ошибка ввода")
print("\nВы выбрали фильм:",c,"\nЖанр:",type,"\nНачало сеанса в",tt,"часа(ов)\nВаше место №",z,"\nК опате:",price,"\nПриятного просмотра!")