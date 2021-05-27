import sys
t=int(input())
for i in range(t):
	a,b=[int(x) for x in input().split()]
	c=a*b
	arr1=[]
	game=True
	for i in range(1,101):
		arr1.append(a*i)
	for j in range(len(arr1)):
		if game==True:

			for k in range(len(arr1)):
				if game==True:

					mid= arr1[j]+arr1[k]
					if mid%c==0 and arr1[j]!=a and arr1[k]!=a and arr1[j]!=arr1[k] and arr1[j]%c!=0 and arr1[k]%c!=0:
						print("YES")
						print(arr1[j],arr1[k],mid)
						game=False

	if game==True:
		print("NO")
