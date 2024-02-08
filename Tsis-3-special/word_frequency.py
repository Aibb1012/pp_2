# word_frequency
s = input('Enter any word:')
def word_frequency(s):
    n = s.split()
    d={}
    for x in n:
        if x not in d.keys(): 
            d[x]=0  #creating a word as a key with value = 0
        d[x] = d[x]+1
    return d
print(word_frequency(s))

