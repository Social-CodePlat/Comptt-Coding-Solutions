s1=input()
my_list=[]
my_list1=[]
for i in range(0,len(s1),2):
    my_list.append(int(s1[i]))
my_list=(sorted(my_list))
for i in my_list:
    my_list1.append(str(i))
x = "+".join(my_list1)
print(x)


