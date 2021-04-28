n=int(input())
rec=0
crm=0
crmunn=0
arr= [int(x) for x in input().split()]
for i in range(len(arr)):
	if arr[i]==-1:
		if rec>=1:
			rec-=1
			crmunn+=0
		else:
			crmunn+=1
	elif arr[i]>=0:
		rec+=arr[i]
print(crmunn)
