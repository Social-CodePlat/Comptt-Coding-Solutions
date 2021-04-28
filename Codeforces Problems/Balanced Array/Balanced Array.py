t=int(input())
for i in range(t):
	even=2
	odd=1
	n=int(input())
	my_list=[0]*n
	if n%4==0:
		print("YES")
		for i in range(0,n//2):
			my_list[i]=even
			even+=2
		for i in range(n//2,n):
			my_list[i]=odd
			odd+=2
		my_list[-1]+=n//2
		x=" ".join(str(i) for i in my_list)
		print(x)
	else:
		print("NO")
