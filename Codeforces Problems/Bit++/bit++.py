x=0
n=int(input())
for i in range(n):
    stat=input()
    if '++' in stat:
        x+=1
    if '--' in stat:
        x-=1
print(x)

