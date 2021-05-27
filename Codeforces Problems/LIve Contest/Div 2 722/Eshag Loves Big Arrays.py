t=int(input())
for i in range(t):
	n=int(input())
	arr=[int(x) for x in input().split()]
	lenarr=len(arr)
	game=True
	count=0
	while game:
		arr1=list(set(arr))
		arr1_len=len(arr1)
		midans=sum(arr1)//arr1_len
		j=0
		game=False
		for j in (arr):
			if j>midans:
				arr.remove(j)
				game=True
	midans1=len(arr)
	print(lenarr-midans1)
			


