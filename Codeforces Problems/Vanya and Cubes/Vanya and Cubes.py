n=int(input())
count=0
i=1
while n>=((i*(i+1))/2):
	count+=1
	n=n-((i*(i+1))/2)
	i+=1
print(count)
