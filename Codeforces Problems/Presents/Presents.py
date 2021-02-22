n=int(input())
arr=[int(x) for x in input().split()]
my_dict={}
i=1
while i<=n:
    my_dict[i] = arr[i - 1]
    i = i + 1
for i in range(1,n+1):
    print(list(my_dict.keys())[list(my_dict.values()).index(i)],end=" ")