a=[2,6,7]
b=[6,6,7]
i=0
c=0
while i<len(a):
    if a[i]==b[i]:
        c=c+1
    i=i+1
print(c)
a=[3,2,1,4,3]
i=0
c=0
max=0
while i<len(a):
    if max<a[i]:
        max=a[i]
        i=i+1
    else:
        c=c+1
    i=i+1
print(c)
