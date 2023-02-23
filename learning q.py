a=[1,2,3,4,5,]
b=[6,7,8,9,10]
i=0
s=[]
while i<len(a):
    s.append(a[i])
    s.append(b[i])
    i=i+1
i=0
while i<len(s):
    j=0
    while j<len(s):
        if s[i]<s[j]:
            s[i],s[j]=s[j],s[i]
        j=j+1
    # print()
    i=i+1
print(s)


a=int(input("enter no"))
w=[]
i=0
while a>=i:
    s=(input("enter no."))
    w.append(s)
    i=i+1
s=w
l=[98,45,78,100,90,12,56,99]
max1=0
max2=0
i=0
while i<len(l):
    j=0
    while j<len(l):
        if max1<l[j]:
            max1=l[j]
        if max2<l[j] and l[j]!=max1:
            max2=l[j]
        j=j+1
    i=i+1
print(max1)
print(max2)
            









