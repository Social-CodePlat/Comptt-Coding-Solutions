a,b=[int(x) for x in (input().split())]
arr=[int(x) for x in input().split()]
count=0
for i in range(a):
    if arr[i]<=b:
        count+=1
    else:
        count+=2
print(count)