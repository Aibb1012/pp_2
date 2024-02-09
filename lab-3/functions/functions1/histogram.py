# histogram
a = [4 , 9 , 7]
def histogram(a):
    for i in a:
        for j in range(i):
            print("*" , end="")
        print()
histogram(a)