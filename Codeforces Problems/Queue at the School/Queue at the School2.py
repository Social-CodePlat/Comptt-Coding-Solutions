a,b=[int(x) for x in input().split()]
s1=input()
while b:
    s1=s1.replace("BG","GB")
    b-=1
print(s1)