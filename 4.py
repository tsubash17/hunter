a=int(input())
b=[]
for x in range (0,a):
    c=input()
    b.append(c)
for x in b:
    count = b.count(x)
    if count==1:
        print (x)
