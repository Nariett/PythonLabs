class Person:
    def __init__(self,name,age,country,street,num,male):# __ -> специальная функция self - ссылка ,(как этот объект)
        self.name = name#инициализация 
        self.age = age
        self.country = country
        self.street = street
        self.num = num
        self.male = male
    def say(self,massege):
        print (massege)
    def say_hell0(self):
        self.say('Hello')
    def display_input(self):
        print(f'name:{self.name};\nage:{self.age};\ncountry:{self.country};\nstreet:{self.street};\nnumber:{self.num};\nmale:{self.male};')
    def show_age(self):
        print ("Age",self.age)
    def __add__(self,other):
        x = self.age+other.age
        return x
    def __sub__(self,other):
        x = self.age-other.age
        return x
    def __mul__(self,other):
        x = self.age*other.age
        return x
    def __truediv__(self,other):
        x = self.age/other.age
        return x
class Student (Person):
    def __init__(self,name,age,country,street,num,male,course,avg):
        Person.__init__(self,name,age,country,street,num,male)
        self.course=course
        self.avg = avg
    def display_input(self):
        Person.display_input(self)
        print(f'course:{self.course};\navg:{self.avg};')
class Worker (Person):
    def __init__(self,name,age,country,street,num,male,education,post):
        Person.__init__(self,name,age,country,street,num,male)
        self.education = education
        self.post = post
    def info2(self):
        Person.display_input(self)
        print(f'education:{self.education};\npost:{self.post};')
class Retiree(Person):
    def __init__(self,name,age,country,street,num,male,pension):
        Person.__init__(self,name,age,country,street,num,male)
        self.pension=pension
    def display_input(self):
        Person.display_input(self)
        print(f'pension:{self.pension}$;')
def decorator(a_func):
    def Data():
        print("\tInfo about person")
        a_func()
    return Data
def decoratorS(a_func):
    def Stud():
        print("\tInfo about Student")
        a_func()
    return Stud
def decoratorW (a_func):
    def Work():
        print("\tInfo about Worker")
        a_func()
    return Work
def decoratorR (a_func):
    def Reti():
        print("\tInfo about Retiree")
        a_func()
    return Reti
def decorator_age(a_func):
    def age():
        print("\tAbout age")
        a_func()
    return age
Pen = Person('Pen',10,'BY','Kolesnikova',33,'M')
Pen.display_input = decorator(Pen.display_input)
Pen.display_input()
Pen.show_age=decorator_age(Pen.show_age)
Pen.show_age()
Jak = Student('jAKSON',18,'UA','Lenina',21,'F',2,34)
Jak.display_input = decoratorS(Jak.display_input)
Jak.display_input()
print ("xtu")
Jim = Worker('Jimmi',35,'USA','LS',124,'M','H','security')
Jim.display_input = decoratorW(Jim.display_input)
Jim.display_input ()
Robert = Retiree('Rober',89,'PL','Kubusia Puchatka','22','M',300)
Robert.display_input()
p2 = Person('Jerry',18,'UK','West Hill',1,'M')
print("\t\tMath calculation")
print ('sum of ages:',Pen+Jak)
print ('age difference:',Robert-Pen)
print ('composition of ages:',Pen*Jim)
print ('age division:',Jim/Jak)