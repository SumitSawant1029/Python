class shape:
	area = 0
	perimeter = 0
	def __init__(self):
		print("Calculating for triangle:")
	def AreaT(self,height,base):
		self.area=0.5 * height * base
	
	def AreaR(self,height,base):
		self.area=height*base
	
	def perimeter(self,a,b):
		self.perimeter=(2*a)+(2*b)
		
	def perimeter(self,a,b,c):
		self.perimeter=a+b+c

	def display(self):
		print("The perimeter of triangle is :-",self.perimeter)
		print("The Area of the triangle is:-",self.area)


obj1 = shape()

obj1.AreaT(100,29)
obj1.perimeter(10,20,30)
obj1.display()

obj2 = shape()
obj2.AreaR(10,30)
obj2.perimeter(20,12)
obj2.display()
