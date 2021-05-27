t=int(input())
for i in range(t):
	h,m=[int(x) for x in input().split()]
	h_a=1440-(60*h+m)
	print(h_a)