t=int(input())
for i in range(t):
	l,b=[int(x) for x in input().split()]
	min_m=min(l,b)
	max_m=max(l,b)
	if max_m <= 2*min_m:
		ans_m=2*min(l,b)
		print(ans_m**2)
	else:
		ans_m=max(l,b)
		print(ans_m**2)
