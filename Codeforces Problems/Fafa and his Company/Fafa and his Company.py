n=int(input())
count=1
for i in range(2,n):
	if n%i==0:
		count+=1
print(count)
