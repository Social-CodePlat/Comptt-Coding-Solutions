a,b=[int(x) for x in input().split()]
for i in range(b):
    if (a % 10) != 0:
        a -= 1
    else:
        a = a // 10
print(a)