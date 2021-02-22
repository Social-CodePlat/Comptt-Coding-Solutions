s=input()
arr=[]
if s=="{}":
    print("0")
else:
    for i in s[1:len(s):3]:
        arr.append(i)
    c = len(set(arr))
    print(c)
