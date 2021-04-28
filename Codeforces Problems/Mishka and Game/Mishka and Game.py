n=int(input())
my_list1=0
my_list2=0
for i in range(n):
	a,b=[int(x) for x in input().split()]
	if a>b:
		my_list1+=1
	if b>a:
		my_list2+=1

sum_a=my_list1
sum_b=my_list2
if sum_a>sum_b:
	print("Mishka")
elif sum_b>sum_a:
	print("Chris")
else:
	print("Friendship is magic!^^")