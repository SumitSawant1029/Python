class triangle:
	area = 0
	perimeter = 0
	def __init__(self):
		print("Calculating for triangle:")
	def Area(self,height,base):
		self.area=0.5 * height * base
	def perimeter(self,a,b,c):
		self.perimeter=a+b+c

	def display(self):
		print("The perimeter of triangle is :-",self.perimeter)
		print("The Area of the triangle is:-",self.area)
		
obj1 = triangle()

obj1.Area(100,29)
obj1.perimeter(10,20,30)
obj1.display()
