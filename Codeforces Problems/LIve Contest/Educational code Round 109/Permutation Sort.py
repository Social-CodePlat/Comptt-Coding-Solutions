t=int(input())
for i in range(t):
    count=0
    n=int(input())
    arr=[int(x) for x in input().split()]
    game=False
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            if i==len(arr)-2:
                count+=1
            game=True
            continue
        else:
            if game==True:
                count+=1
            game=False
    if count<=3:
        print(count)
    else:
        print(3)
