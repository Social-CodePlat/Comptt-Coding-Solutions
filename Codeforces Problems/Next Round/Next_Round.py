n,k=[int(x) for x in input().split()]
my_list=[]
count=0
my_list =[int(d) for d in input().split()]
for i in range(n):
    if my_list[i]>0:
        if my_list[i]>=my_list[k-1]:
            count+=1
print(count)