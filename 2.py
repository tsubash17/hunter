a=int(input())
b=[]
for x in range(0,a):
    c=input()
    b.append(c)
d=[]
for x in b:
    if x not in d:
        d.append(x)
d.sort(reverse=True)
print ("".join(d))
