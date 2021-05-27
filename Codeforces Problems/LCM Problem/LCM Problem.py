t=int(input())
for i in range(t):
  a,b=[int(x) for x in input().split()]
  if a*2<=b:
    print(a,a*2)
  else:
    print(-1,-1)