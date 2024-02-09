# spy_game
a = [1,2,4,0,0,7,5]
def spy_game(a):
    s = ""
    for i in a:
        if i == 0 or i==7:
            s+=str(i)
    if s.find("007") >=0:
        return True
    else:
        return False
print(spy_game(a))