# find_common_elements

a = [1, 12 , 7 , 4 , 8 , 17]
b = [12 , 6 , 63 , 12 , 4 ,5]
d =[]
#if you want input
# a=[]
# b=[]
# n = int(input("The size of first list: "))
# m = int(input("The size of second list: "))
# for i in range(n):
#     x = int(input())
#     a.append(x)
# for i in range(m):
#     z = int(input())
#     b.append(z)
def find_common_elements(a , b):
    for i in a:
        if i in b:
            d.append(i)
find_common_elements(a , b)
print(d)
                