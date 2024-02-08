# My_Shape
class My_Shape:
    def __init__(self , color , is_filled):
        self.color = color
        self.is_filled = False
    # def print_char(self):
    #     print(self.color , self.is_filled)
    def __str__(self):
        return f'The color is {self.color} , Is filled ? {self.is_filled}'
    def getArea():
        return 0
    

Oval = My_Shape('blue' , False)
# print(Oval)
print(Oval)


class Rectangle(My_Shape):
    def __init__(self, color, is_filled , x_top_left, y_top_left, length, width):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width
    def __str__(self):
        return (f'The color is {self.color} , Is filled: {self.is_filled}, Top Left:({self.x_top_left} , {self.y_top_left}) , Length={self.length} , Width={self.width}')
    def getArea(self):
        return self.length*self.width

def input_Rectangle_datas():
    color = input('Enter the color of your rectangle: ')
    is_filled = bool(input("Is your rectangle filled (True/False): "))
    x_top_left = float(input("Enter the top left of value x: "))
    y_top_left = float(input("Enter the top left of value y: "))
    length = float(input("Enter the length of your Rectangle: "))
    width = float(input("Enter the width of your Rectangle: "))
    return Rectangle(color , is_filled , x_top_left , y_top_left , length , width)

givenrectangle = input_Rectangle_datas()
print(givenrectangle , "The area of Rectangle:" , givenrectangle.getArea())
# print(givenrectangle)

class Circle(My_Shape):
    def __init__(self, color, is_filled , x_center, y_center, radius):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
    def __str__(self):
        return (f'The color is {self.color} , Is filled: {self.is_filled}, Top Left:({self.x_center} , {self.y_center}) , Radius={self.radius}')
    def getArea(self):
        return 3.14*self.radius*self.radius

givencircle = Circle('red' , False , 0 , 1 , 3)
print(givencircle)
print(givencircle.getArea())



        
