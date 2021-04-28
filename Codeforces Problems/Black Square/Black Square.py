arr = [int(x) for x in input().split()]
n = input()
count=0
for i in n:
    if i == '1':
        count += arr[0]
    elif i == '2':
        count += arr[1]
    elif i == '3':
        count += arr[2]
    elif i == '4':
        count += arr[3]
print(count)