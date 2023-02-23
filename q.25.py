# 25. Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]
l = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
i=0
b=[]
while i<len(l):
    j=0
    c=0
    while j<len(l):
        if l[i]==l[j]:
            c=c+1
        j=j+1
    if c>3:
        if l[i] not in b:
            b.append(l[i])
    i=i+1
print(b)

28. The task is to perform the operation of removing all the occurrences of a given item/element present in
a list.
Input :
1 1 2 3 4 5 1 2
1
Output :
2 3 4 5 2


l=[1,1,2,3,4,5,1,2]
i=0
d=[]
v=0
while i<len(l):
    j=0
    c=0
    while j<len(l):
        if l[i]==l[j]:
            c=c+1
        j=j+1
            
    if c>1:
        if [c,l[i]] not in d:
            pass
    else:
        d.append(l[i])
        v=v+1
    i=i+1
print(v)
ar= [10, 20, 20, 10, 10, 30, 50, 10, 20,20,2,2,3]
i=0
k=[]
while i<len(ar):
    j=0
    c=0
    while j<len(ar):
        if ar[i]==ar[j]:
            c=c+1
        j=j+1
    if c not in k:
        k.append(c) 
    i=i+1
a=0
f=0
b=0
while a<len(k):
    if k[a]%2!=0:
        f=f+1
    else:
         b=b+1
    a=a+1
#     i=i+1
# print(f+b)
# a=[()]
# res=[False]*2
# if a:
#     res[0]=True
# if a[0]:
#     res[1]=True
d=[1,2]
b=[3,4]
s=d+b

d=len(s)//2
b=s[d]+s[d-1]
c=b/d
print(c)
