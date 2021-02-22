n=list(input())
for i in n:
    if n.count("4")+n.count("7")==4 or n.count("4")+n.count("7")==7:
        print("YES")
        break
    else:
        print("NO")
        break