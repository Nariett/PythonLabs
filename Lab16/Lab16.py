from math import*
class rhombus:
	def __init__(self,side,corner):
		self.side=side 
		self.corner=corner
		self.Ax=0#point 10,2,3,0,0,-2,-3,0
		self.Ay=2
		self.Bx=3#point 2
		self.By=0
		self.Cx=0#point 3
		self.Cy=0
		self.Dx=-3#point 4
		self.Dy=0
	def display_input(self):
		 print(f'side:{self.side};\ncorner:{self.corner};')
	def area(self):
		area = pow(self.side,2)*sin(self.corner)
		if area < 0:
			area=area*-1
		area = str(area)
		print ("Area rhombus "+ area)
	def perimeter(self):
		per = str (self.side*4)
		print ("perimeter rhombus " + per)
	def display_inputcor(self):
	 	print(f'Ax:{self.Ax};\nAy:{self.Ay};\nBx:{self.Bx};\nBy:{self.By};\nCx:{self.Cx};\nCy:{self.Cy};\nDx:{self.Dx};\nDy:{self.Dy};')
	def up(self,step):
		self.Ay+=step
		self.By+=step
		self.Dy+=step
		self.Cy+=step
	def down(self,step):
		self.Ay-=step
		self.By-=step
		self.Dy-=step
		self.Cy-=step
	def right(self,p):
		self.Ax+=step
		self.Bx+=step
		self.Dx+=step
		self.Cx+=step
	def left(self,p):
		self.Ax-=step
		self.Bx-=step
		self.Dx-=step
		self.Cx-=step
x = int(input("Enter side x:"))
y = int(input("Enter corner alfa:"))
ABCD = rhombus(x,y)
print("About rhombus")
ABCD.display_input()
ABCD.area()
ABCD.perimeter()
print("About the location")
while True:
	ABCD.display_inputcor()
	x = int (input("Do you want to move the figure?\n 1 - yes \n 2 - no \n Choice = "))
	if x == 1:
		select = int (input ("Select direction \n 1 - up \n 2 - down \n 3 - right \n 4 - left\nChoice = "))
		if select == 1:
			step = int (input ("Enter step:"))
			ABCD.up(step)
			continue 
		elif select == 2:
			step = int (input ("Enter step:"))
			ABCD.down(step)
			continue 
		elif select == 3:
			step = int (input ("Enter step:"))
			ABCD.right(step)
			continue 
		elif select == 4:
			step = int (input ("Enter step:"))
			ABCD.left(step)
			continue 
		else:
			print ("you entered an incorrect value. Try again")
	elif x == 2:
		break
	else:
		print("you entered an incorrect value. Try again")
print("final result")
ABCD.display_inputcor()

      