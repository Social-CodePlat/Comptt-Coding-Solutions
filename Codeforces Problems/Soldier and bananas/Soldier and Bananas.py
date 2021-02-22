arr=[int(x) for x in input().split()]
sum=0
for i in range(1,(arr[2]+1)):
    sum+=arr[0]*i
if sum<=arr[1]:
    print(0)
else:
    print(sum-arr[1])
