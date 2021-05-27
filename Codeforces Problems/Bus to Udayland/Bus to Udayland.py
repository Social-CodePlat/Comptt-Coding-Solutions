n=int(input())
arr=[]
game=True
for i in range(n):
	arr.append((input()))
for j in range(n):
	if "OO" in arr[j]:
		print("YES")
		ind=arr[j].index("OO")
		if ind==0 and arr[j][ind+1]=="O":
			arr[j]="++|"+arr[j][3]+arr[j][4]
		if ind==3 and arr[j][ind+1]=="O":
			arr[j]=arr[j][0]+arr[j][1]+"|"+"++"
		game=False
		break
if game==True:
	print('NO')
else:
	for k in range(n):
		print(arr[k])