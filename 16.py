a=int(input())
s=int(input())
b=[]
for x in range(0,a):
    d=int(input())
    b.append(d)
b.sort()
c=b.index(s)
print(b[c-1],b[c+1],b[c-2])
