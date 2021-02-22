import gc
my_list=[]
c=0
for i in range(5):
    my_list.append(int(input()))
for i in range(1,my_list[4]+1):
    if i % my_list[0] != 0 and i % my_list[1] != 0 and i % my_list[2] != 0 and i % my_list[3] != 0:
    	c+=1
print(my_list[4]-c)
gc.collect()