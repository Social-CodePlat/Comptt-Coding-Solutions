n,k=[int(x) for x in input().split()]
tt=k
i=1
c=0
while tt<=240:
    if c<=n:
        tt += 5 * i
        c += 1
        i += 1
    else:
        break
print(c-1)