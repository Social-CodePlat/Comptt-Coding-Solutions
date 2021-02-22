s1=input()
count1=0
count2=0
for i in s1:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
if count1>count2:
    print(s1.lower())
elif count1<count2:
    print(s1.upper())
else:
    print(s1.lower())