class Rectangle():
	"""class that calculates the area of a rectangle"""
	def __init__(self, width, length):
		self.width = width
		self.length = length

	def area(self):
		area = self.width * self.length
		return area
	
	def perimeter(self):
		perimeter = 2*self.width + 2*self.length
		return perimeter

# Using Inheritance. Rectangle is the superclass. Square is the subclass.
class Square(Rectangle):
	def __init__(self, length):
		super().__init__(length, length)

rectangle = Rectangle(2,4)
print(rectangle.area())
print(rectangle.perimeter())

square = Square(2)
print(square.area())
