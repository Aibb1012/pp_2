a = [1 , 2 , 3 , 4 , 5 , 7 , 11 , 9 , 21]
def only_prime(a):
    primes = []
    for i in a:
        flag = True
        for j in range(2 , i):
            if i%j==0:
                flag = False
        if i<2:
            continue
        if flag == True:
            primes.append(i)
    return primes
print(only_prime(a))