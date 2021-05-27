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
t=int(input())

for i in range(t):
	n=int(input())
	if 100%n!=0:
		mid=gcd(n,100)
		print(100//mid)
	else:
		print(100//n)