n=int(input())
s1=input()
s2=input()
moves=0
for i in range(len(s1)):
	moves+=min(abs(int(s1[i])-int(s2[i])),10-abs(int(s1[i])-int(s2[i])))
print(moves)