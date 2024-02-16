# n_to_0
def generatee(n):
    while n>=0:
        yield n
        n-=1
k = int(input())
s = generatee(k)
for i in s:
    print(i)
    