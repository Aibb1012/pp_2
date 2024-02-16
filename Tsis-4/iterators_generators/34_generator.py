# 34_generator
def generatee(n):
    index = 0
    while index<n:
        yield index
        index+=1
def div_34(k):
    for i in k:
        if i==0:
            continue
        if i%4==0:
            if i%3==0:
                yield i

b=int(input())
n = generatee(b)
k = div_34(n)
for i in k:
    print( i)
            