n=int(input())
for i in range(n):
    count=0
    a,b=[int(x) for x in input().split()]
    if a<b:
    	d=b-a
    else:
    	d=a-b
    if d%10>0:
    	print(int((d/10)+1))
    else:
    	print(int((d+9)/10))

