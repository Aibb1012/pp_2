# rectangle
class My_Shape:
   def __init__(self) -> None:
      pass
    
    # def __str__(self):
    #     return (f'given shape = ')

   def area(self):
      return 0
# shape = My_Shape()

class Rectangle(My_Shape):
   def __init__(self, length = 0 , width = 0):
      My_Shape.__init__(self)
      self.length = length
      self.width = width

   def area(self):
      return self.length * self.width


x = int(input())
y = int(input())
s = Rectangle(x , y)
print(s.area())

print(Rectangle().area())