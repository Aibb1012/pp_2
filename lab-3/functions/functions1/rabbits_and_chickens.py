# rabbits_and_chickens
def solve(numheads, numlegs):
    chickns = (numlegs - (4 * numheads)) / -2
    rabbits = numheads - chickns
    return int(chickns), int(rabbits)
print(solve(35 , 94))
