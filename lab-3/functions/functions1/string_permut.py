# string_permut
from itertools import permutations
s = "gap"
def permutation(string):
   res = [''.join(p) for p in permutations(string)]
   print(res, sep = ' ')

permutation(s)