import sys
def check_if(k,f,count):
	k=int(k)
	f=int(f)
	game=True
	while k!=0:
		rem=k%10
		k=k//10
		if rem==f:
			continue
		else:
			game=False
	if game==True:
		count+=1
	return count

t=int(input())
for i in range(t):
	game=True
	count=0
	n=input()
	f=n[0]
	k=int(n)
	if len(n)==1:
		print(n)
		game=False
	else: 
		for j in range(1,(int(n))+1):
			m=str(j)
			count=check_if(j,m[0],count)
	if game==True:
		print(count)