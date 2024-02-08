def get_max(a ,b , c):
    thislist = [a , b ,c]
    thislist.sort()
    print(thislist[-1])

a = int(input("Write the first element: "))
b = int(input("Write the second element: "))
c = int(input("Write the third element: "))
get_max(a , b, c)