h=int(input())
s=int(input())
p=int(input())
nextp=s
while h!=1:
    nextp=(nextp*p)//100
    h=h-1
print(nextp)