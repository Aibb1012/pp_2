# even numbers_gen
def generatee(n):
    index = 0
    while index<n:
        yield index
        index+=1
def is_even(k):
    for i in k:
        if i%2==0 and i!=0:
            yield i

b=int(input())
n = generatee(b)
k = is_even(n)
for i in k:
    print(f"{i:_}", end=", ")