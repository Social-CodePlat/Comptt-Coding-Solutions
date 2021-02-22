n=int(input())
ans=0
for i in range(n):
    my_list1 = []
    c=input()
    t=[str(x) for x in c]
    new_list=list(map(int,t))
    val1=int(c)
    if val1 % (10 ** (len(c) - 1)) == 0:
        print(1)
        print(c)
    else:
        s = len(new_list) - 1
        for i in range(len(new_list)):
            if new_list[i] != 0:
                my_list1.append(new_list[i] * (10 ** (s)))
            s -= 1
    if len(my_list1)>0:
        print(len(my_list1))
        new_list1 = map(str, my_list1)
        x = " ".join(new_list1)
        print(x)