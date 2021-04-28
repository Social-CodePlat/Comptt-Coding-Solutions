import sys
r,c=[int(x) for x in input().split()]
game=True
arr=[]
for i in range(r):
    arr.append(input().split())
for i in arr:
    for j in i:
        if (j=="C") or (j=="M") or (j=="Y"):
            print("#Color")
            game=False
            sys.exit()
if game==True:
    print("#Black&White")