#  Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric
# values.
# Original list:
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
j=1
d=[]
while i<len(l) and j<len(l):
    s=l[j]-l[i]
    d.append(s)
    j=j+1
    i=i+1
print(d)

# # 
a=input("enter no.")
n=list(a)
if len(n)%2==0:
    j=0
    d=[]
    while j<len(n):
        if j%2==0:
            s=int(n[j])*2
            d.append(s)
        else:
            d.append(n[j])
        j=j+1
else:
        i=0
        d=[]
        while i<len(n):
            if i%2!=0:
                s=int(n[i])*2
                d.append(s)
            else:
                d.append(n[i])
            i=i+1
print(d)


