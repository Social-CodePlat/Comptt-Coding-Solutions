n=int(input())
arr=[int(x) for x in input().split()]
brr=[int(x) for x in input().split()]
my_list=[]
for i in arr[1:]:
    my_list.append(i)
for i in brr[1:]:
    my_list.append(i)
for i in range(1,n+1):
    if i in my_list:
        if i == n:
            print("I become the guy.")
            break
        else:
            continue
    else:
        print("Oh, my keyboard!")
        break

