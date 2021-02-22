my_list=[]
for i in range(int(input())):
    a,b=[int(x) for x in input().split()]
    my_list.append((-a)%b)
for i in my_list:
    print(i)