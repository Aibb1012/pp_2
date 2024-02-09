n = int(input())
def Is_Square(n):
    for i in range(n):
        k = True
        if n == i*i:
            k = False
            break
    if k == True:
        print("No")
    else:
        print("Yes")
    



x = Is_Square(n)