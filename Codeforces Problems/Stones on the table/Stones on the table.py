n=int(input())
s1=list(input())
count=0
i=0
while i<n:
    try:
        if s1[i]==s1[i+1]:
            s1.remove(s1[i+1])
            count+=1
        else:
            i+=1
    except:
        break
print(count)




