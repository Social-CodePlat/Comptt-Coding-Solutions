"""
it is very genuine to go for ascii code approach using the inbuilt ord() fun in python
but that won't work here,, cause the sum value of two strings can be same even when the
strings aren't. ex- aeg & bdg same 301
"""
s1=input().lower()
s2=input().lower()
if s1==s2:
    print(0)
elif s1<s2:
    print("-1")
else:
    print("1")