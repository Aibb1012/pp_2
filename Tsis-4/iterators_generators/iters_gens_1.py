# iters_gens_1
def generatee(n):
    index = 0
    while index<n:
        yield index
        index+=1

def make_square(k):
    for i in k:
        yield i**2

b=int(input())
n = generatee(b)
k = make_square(n)
for i in k:
    print(i)
