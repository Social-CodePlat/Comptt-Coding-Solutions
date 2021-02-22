n=int(input())
s=input()
av=s.count("A")
dv=s.count("D")
if av>dv:
    print("Anton")
elif av<dv:
    print("Danik")
else:
    print("Friendship")