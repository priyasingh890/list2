#write a python program to find the second smallest number in a list.
l=[4,5,6,7,7,8,2,6,9,10,11]
i=0
max=0
while i<len(l):
    if max<l[i]:
        max=l[i]
    i=i+1
i=0
max2=0
while i<len(l):
    if max2<l[i] and l[i]!=max:
        max2=l[i]
    i=i+1
print(max2)

