n=int(input())
list1=[]
list2=[]
c=0
for i in range(n):
    a,b=[int(x) for x in input().split()]
    list1.append(a)
    list2.append(b)
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            c+=1
print(c)
