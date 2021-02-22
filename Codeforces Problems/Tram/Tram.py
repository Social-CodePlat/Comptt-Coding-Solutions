n= int(input())
my_list=[]
a=b=c=0
for i in range(n):
    a,c=[int(x) for x in input().split()]
    my_list.append(c+b-a)
    b=b+c-a
print(max(my_list))