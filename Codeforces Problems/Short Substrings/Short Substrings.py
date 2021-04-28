n=int(input())
for i in range(n):
	s=input()
	my_list=[]
	for i in range(0,len(s),2):
		my_list.append(s[i]+s[i+1])
	x=""
	for i in range(len(my_list)-1):
		x+=my_list[i][0]
	print(x+my_list[len(my_list)-1])
