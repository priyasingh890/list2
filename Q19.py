# write program to python get to different between two list
a= [10, 15, 20, 25, 30, 35, 40]
B = [25, 40, 35]
i=0
c=[]
while i<len(a):
    if a[i] not in B:
        c.append(a[i])
    i=i+1
print(c)


a=[4,6,7]
b=[6,9,2]
c=[8,9,5]
i=0
f=0
k=0
s=0
while i<len(a):
    s=s+a[i]+b[i+1]+c[i+2]
    k=k+a[f+2]+b[f+1]+c[f]
    print(s)
    print(k)
    f=f+1
    i=i+1
