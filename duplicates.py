l=[1,2,3,4,5,6,7,7,7,5,5,2,3]
k=[]
for i in set(l):
    if l.count(i)-1:
        k.append(i)

print(k)

