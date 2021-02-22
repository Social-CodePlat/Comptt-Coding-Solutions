t=int(input())
for i in range(t):
    n=int(input())
    my_list=[]
    my_list=sorted([int(x) for x in input().split()])
    j=0
    while (len(my_list) > 1 and ((j + 1) < len(my_list))):
        if my_list[j + 1] - my_list[j] <= 1:
            del (my_list[j])
        else:
            j += 1
    if len(my_list) == 1:
        print("YES")
    else:
        print("NO")



