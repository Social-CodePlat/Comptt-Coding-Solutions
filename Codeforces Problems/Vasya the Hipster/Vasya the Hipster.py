a,b=[int(x) for x in input().split()]
print(min(a,b),end=" ")
a1=a-min(a,b)
b1=b-min(a,b)
print(max(a1,b1)//2)