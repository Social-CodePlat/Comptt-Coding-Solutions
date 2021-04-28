t=int(input())
for i in range(t):
	n,k=[int(x) for x in input().split()]
	a=[int(x) for x in input().split()]
	b=[int(x) for x in input().split()]
	a_srt=sorted(a)
	b_srt=sorted(b, reverse =True)
	for i in range(k):
		if a_srt[i]<b_srt[i]:
			a_srt[i]=b_srt[i]
	print(sum(a_srt))
