n=int(input())
count=0
my_list=[1,2,3,4,5]
if n is my_list:
    print("1")
else:
    while n!=0:
        if n>=5:
            n-=5
            count+=1
        elif n==4:
            n-=4
            count+=1
        elif n==3:
            n -= 3
            count += 1
        elif n==2:
            n -= 2
            count += 1
        elif n==1:
            n -= 1
            count += 1

    print(count)