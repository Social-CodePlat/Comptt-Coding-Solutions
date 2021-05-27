n=int(input())
arr=[int(x) for x in input().split()]
s=0
d=0
for i in range(len(arr)):
	if len(arr)>=1:
		a=max(arr[0],arr[len(arr)-1])
		s+=a
		arr.remove(a)
	else:
		break
	if len(arr)>=1:
		b=max(arr[0],arr[len(arr)-1])
		d+=b
		arr.remove(b)
	else:
		break
print(s,d)