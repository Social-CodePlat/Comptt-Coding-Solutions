n=input()
v=int(n)
ml=[int(x) for x in n]
val=len(set(ml))
i=0
def count_d(x):
    v=str(x)
    ml=[int(x) for x in v]
    val=len(set(ml))
    return val
while (i!=len(n)):
    v+=1
    i=count_d(v)
print(v)
