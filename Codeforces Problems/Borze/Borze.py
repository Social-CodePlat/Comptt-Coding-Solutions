a=input()
i=0
while i<=len(a)-1:
	if a[i]==".":
		print(0,end="")
		i+=1
	elif a[i]=="-" and a[i+1]==".":
		print(1,end="")
		i+=2
	elif a[i]=="-" and a[i+1] =="-":
		print(2,end="")
		i+=2