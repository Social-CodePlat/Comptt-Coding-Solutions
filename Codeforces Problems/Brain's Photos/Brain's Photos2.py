r,c=[int(x) for x  in input().split()]
game=True
for i in range(r):
	arr=[str(x) for x in input().split()]
	if ("C" in arr) or ("M" in arr) or ("Y" in arr):
		print("#Color")
		game=False
		break
if game==True:
	print("#Black&White")
