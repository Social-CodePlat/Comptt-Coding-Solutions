a, b =[int(x) for x in input().split()]
count = 0
if a == b:
    print(1)
else:
    while a <= b:
        a = 3 * a
        b = 2 * b
        count += 1
    print(count)
