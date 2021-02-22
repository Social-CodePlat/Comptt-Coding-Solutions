n,k=[int(x) for x in input().split()]
while n*(n+1)//2*5>240-k:
    n-=1
print(n)