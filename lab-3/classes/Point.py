# Point
import math

class Point():
   def __init__(self, x, y):
      self.x = x
      self.y = y
   # def __str__(self):
   #    return f"the points is ({self.x} , {self.y})"
   def show_coord(self):
      return self.x, self.y

   def move(self, z, w):
      self.x += z
      self.y += w
   
   def distance(self, p2):
        newx = math.sqrt((p2.x - self.x) * (p2.x - self.x))
        newy = math.sqrt((p2.y - self.y) * (p2.y - self.y))
        return newx, newy
    
p1 = Point(7, 4)
p2 = Point(3, 5)

print(p1.show_coord())

print(p1.show_coord())
print(p1.distance(p2))
p1.move(1, 1)
    