n=int(input())
c=0
arr=[int(x) for x in input().split()]
for i in range(len(arr)):
    for j in range(1,len(arr)):
        if arr[j]>arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            c+=1
            j+=2
            print(arr)
            if max(arr) == arr[0] and min(arr) == arr[len(arr) - 1]:
                break
print(c)
print(arr)