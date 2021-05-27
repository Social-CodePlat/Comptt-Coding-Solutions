t=int(input())
def countlet(strn,let,count):
	for i in strn:
		if i==let:
			count+=1
	return count
for i in range(t):
	n=int(input())
	game=True
	strn=""
	for j in range(n):
		strn+=input()
	s=set(strn)
	for l in s:
		if strn.count(l)% n!=0:
			game=False
			break
	print("YES" if game else "NO")
