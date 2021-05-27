n=int(input())
import math
for i in range(n):
    a=input()
    l=len(a)
    s=0
    if(l==1):
        print(int(a))
    else:
     for i in range(l-1):
        s+=9
     if(int(a)==int(math.pow(10,l-1))):
         print(s)
     else:
      c=0
      s+=int(a[0])-1
      for i in range(l-1):
          if(a[i]<a[i+1]):
              s+=1
              break
          if(a[i]==a[i+1]):
              c+=1
              continue
          if(a[i]>a[i+1]):
              break
      if(c+1==l):
          s+=1
      print(s)