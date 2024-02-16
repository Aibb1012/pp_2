# squares_ab_gen
def square(a , b):
    for i in range(a ,b):
        yield i**2

sq = square(a = int(input()) , b = int(input()))
for i in sq:
    print(i)