a=int(input())
b=[]
for x in range(0,a):
    c=input()
    b.append(c)
d=[]
e=[]
for x in b:
    if x not in d:
        d.append(x)
    else:
        e.append(x)
e.sort()
f=[]
for x in e:
    if x not in f:
        f.append(x)
print (f)
