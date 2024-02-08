mylist = []
n = int(input("Number of elements: "))
for i in range(n):
    mylist.append(int(input()))
# for i in mylist:
#     print(i)
a = []
k = True

def filter_prime(mylist):
    for i in mylist:
        c=0
        for j in range (1 , i):
            if i%j==0:
                c=c+1
        if c==1:
            a.append(i)
filter_prime(mylist)
        
print("Prime Numbers are" , a)