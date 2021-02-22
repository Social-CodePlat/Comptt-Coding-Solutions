s1=input()
s2=input()
s3=input()
s4=s1+s2
if len(s4)==len(s3):
    for i in s4:
        if s4.count(i) == s3.count(i):
            if s4.rindex(i) == len(s3)-1:
                print("YES")
                break
            else:
                continue
        else:
            print("NO")
            break
else:
    print("NO")