# reversed_sentence
s = input()
def reversed_sentence(s):
    a = list(s.split())
    a.reverse()
    for i in a:
        print(i , end = ' ')
reversed_sentence(s)

