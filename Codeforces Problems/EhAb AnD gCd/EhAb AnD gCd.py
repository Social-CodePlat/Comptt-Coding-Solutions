def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

t=int(input())
for i in range(t):
	n=int(input())
	game=True
	while game:
		a=n-1
		b=1
		a_mid=hcfnaive(a,b)
		b_mid=compute_lcm(a,b)
		if a_mid+b_mid==n:
			print(a,b)
			break
		else:
			a-=1
			b+=1