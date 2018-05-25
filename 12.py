a=int(input())
b=int(input())
c=[]
for x in range(0,a):
    d=input()
    c.append(d)
c.sort(reverse=True)
print (c[b-1])
