arr=[int(x) for x in input().split()]
brr=sorted(arr)
middle=brr[1]
print((middle-brr[0])+(brr[2]-middle))