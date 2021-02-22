s1=input()
my_list=[]
for i in range(len(s1)):
    my_list.append(s1[i])
my_list[0]=my_list[0].upper()
x="".join(my_list)
print(x)
