class Person:
	counter = 0
	def __init__(self,name,age,country,male):
		self.name = name
		self.age = age
		self.country = country
		self.male = male
	def display_input(self):
		print(f'\nName:{self.name};\nage:{self.age};\ncountry:{self.country};\nmale:{self.male};')
class Astronaut(Person):
	def __init__(self,name,age,country,male,rank,flights):
		Person.__init__(self,name,age,country,male)
		self.__rank = rank;
		self.__flights = flights;
		Person.counter = Person.counter + 1 
	def display_input(self):
		print ("Info about Austronaut")
		Person.display_input(self)
		print(f'rank:{self.__rank};\nflights:{self.__flights};')
class MKS:
	def __init__(self,name):
		self.name = "MKS"
	def MKS_info():
		print ('Info about mks')
		print(f'Astronau in MKS:{Person.counter}')
Jak = Person('Jak',30,'BY','M')
Jak.display_input()
Jim = Astronaut('Jim',20,'PL','M','Captain',4)
Jim.display_input()

MKS.MKS_info()

	


