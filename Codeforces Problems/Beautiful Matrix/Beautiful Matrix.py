rows, cols = (5, 5)
arr=[]
ans=0
temparr=[]
for i in range(1,rows+1):
    row=[]
    temparr = [int(x) for x in input().split()]
    row.append([int(x) for x in temparr])
    for k in range(0, len(temparr)):
        if not (temparr[k] ^ 1):
            ans=(abs(i - 3) + abs(k - 2))
    arr.append(row)
print(ans)