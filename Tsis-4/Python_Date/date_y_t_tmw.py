
import datetime
x = datetime.datetime.now() - datetime.timedelta(1)
y = datetime.datetime.now()
z = datetime.datetime.now() + datetime.timedelta(1)
print("Yesterday -" , x)
print("Now -" , y)
print("Tomorrow -",z)