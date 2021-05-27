str1=input()
arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cur='a'
moves=0
for i in range(len(str1)):
	n = arr.index(cur)
	n1 = arr.index(str1[i])
	moves += min(abs(n-n1),26-abs(n-n1))
	cur=str1[i]
print(moves)