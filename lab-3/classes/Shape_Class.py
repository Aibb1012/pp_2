class My_Shape:
   def __init__(self) -> None:
      pass
    
    # def __str__(self):
    #     return (f'given shape = ')

   def area(self):
      return 0
# shape = My_Shape()

class Square(My_Shape):
   def __init__(self, length = 0):
      My_Shape.__init__(self)
      self.length = length

   def area(self):
      return self.length * self.length


x = int(input())
s = Square(x)
print(s.area())

print(Square().area())

