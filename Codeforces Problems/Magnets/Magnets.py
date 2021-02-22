n=int(input())
s=""
grp=1
while n:
    a=input()
    s+=a
    n-=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        grp+=1
print(grp)