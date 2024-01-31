# Python Arrays_examp
cars = ["Ford", "Volvo", "BMW"] #Create an array containing car names
#Get the value of the first array item:
x = cars[0]
cars[0] = "Toyota" #Modify the value of the first array item
x = len(cars) #Return the number of elements in the cars array
for x in cars:
  print(x)

cars.append("Honda")
cars.pop(1) #Delete the second element of the cars array
cars.remove("Volvo") 
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")