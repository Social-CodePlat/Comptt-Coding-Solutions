n=int(input())
arr=[float(x) for x in input().split()]
perc=((sum(arr)/(100*len(arr)))*100)
print("{:.11f}".format(perc))
