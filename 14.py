from itertools import permutations
a=input()
b=list(permutations(a))
for x in b:
    print ("".join(x))
