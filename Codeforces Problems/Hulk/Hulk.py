n=int(input())
s=""
for i in range(1,n+1):
    if i==n:
        if i%2==0:
            s+="I love it "
        else:
            s+="I hate it "
    elif i%2!=0:
        s+="I hate that "
    else:
        s+="I love that "
print(s)