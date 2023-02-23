# 35. Write a Python program to check if first digit/character of each element in a given list
# is same or not.
# Original list:




list=[1234, 122, 1984, 19372, 100]
# d=str(list[0])
i=0
c=0
while i<len(list):
    s=str(list[i])
    d=str(list[0])
    if d[0]==s[0]:
        c=c+1
    i=i+1
if c==len(list):
    print("true")
    
else:
    print("false")


        


