import gc
my_list=[]
arr=[]
list2=[]
for i in range(5):
    my_list.append(int(input()))
for i in range(1,my_list[4]+1):
    arr.append(i)
for i in arr:
    if i % my_list[0] == 0 or i % my_list[1] == 0 or i % my_list[2] == 0 or i % my_list[3] == 0:
        list2.append(i)
print(len(list2))
gc.collect()