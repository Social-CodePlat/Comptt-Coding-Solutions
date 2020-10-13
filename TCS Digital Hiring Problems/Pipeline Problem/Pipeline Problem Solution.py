m,n,k=input().split()
list1=[]
list2=[]
x,y,z=input().split()
list1.append(x)
list1.append(y)
list1.append(z)
p,q,r=input().split()
list2.append(p)
list2.append(q)
list2.append(r)
for i in range(0, len(list1)):
    list1[i] = int(list1[i])
for i in range(0, len(list2)):
    list2[i] = int(list2[i])
t=sum(list2)-sum(list1)
if t < 0:
    s =t - int(k)

else:
    s =t + int(k)
print(s)