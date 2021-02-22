n,m=[int(x) for x in input().split()]
for i in range(1,n+1):
    if i%2==1:
        print("#"*(m))
    if i%4==2:
        print("." * (m-1) + "#")
    if i%4==0:
        print("#" + "." * (m-1))

