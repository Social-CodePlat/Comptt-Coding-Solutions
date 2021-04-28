t=int(input())
for i in range(t):
	n=int(input())
	print(n//2)

'''
def gcd(a,b):
	if b==0:
		return a
	if a%b==0:
		return b
	if b%a==0:
		return a
	if a%b!=0 and a>b:
		return gcd(a%b,b)
	if b%a!=0 and b>a:
		return gcd(a,b%a)
def appendPairs(arr, n):
    my_list=[]
    for i in range(n):
        for j in range(n):
            if arr[i]!=arr[j]:
                my_list.append((arr[i],arr[j]))
    return my_list

t=int(input())
for i in range(t):
	arr=[]
	my_list2=[]
	my_list1=[]
	n=int(input())
	for i in range(1,n+1):
		arr.append(i)
	my_list2=appendPairs(arr,len(arr))
	for i in range(len(my_list2)):
		my_list1.append(gcd(my_list2[i][0],my_list2[i][1]))
	print(max(my_list1))

'''