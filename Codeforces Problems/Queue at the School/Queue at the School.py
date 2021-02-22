a,b=[int(x) for x in input().split()]
s1=list(input())
i=0
while i<b:
    j=0
    while j<len(s1):
        try:
            if s1[j]<s1[j+1]:
                s1[j],s1[j + 1]=s1[j + 1],s1[j]
                j=j+2
            else:
                j+=1
        except:
            break
    i+=1
x="".join(s1)
print(x)
