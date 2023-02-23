 
s=[[12,34,56],[34,56,78],[67,89,23]]
i=0
d=[]
while i<len(s):
    j=0
    while j<len(s[i]):
        b=str(s[i][j])
        k=0
        sum=0
        while k<len(b):
            sum=sum+int(b[k])
            k=k+1
        d.append(sum)
        j=j+1
    print()
    i=i+1
print(d)



a="garden"
j=0
while j<len(a[0]):
    print(a[0])


d=[[4,3,2],[2,3,4],[4,8,9]]
r=0
for i in d:
    for j in i:
        c=0
        for g in d:
            for n in g:
                if j==n:
                    c=c+1
        if c>=2:
            r=r+j
print(r)


i=0
j=0
while i<len(a):
    if a[i]=="e":
        pass
    else:
        print(a[i])
    i=i+1




i=0
g=[]
while i<len(s):
    j=0
    while j<len(s[i]):
        d=s[i][j]
        g.append(d)
        j=j+1
    i=i+1
i=0
sum=0
while i<len(g):
    j=0
    c=0
    while j<len(g):
        if g[i]==g[j]:
            c=c+1
        j=j+1
    if c>=2:
        sum=sum+g[i]   
    i=i+1
print(sum)
# a=int(input(""))
# b=int(input(""))
# h=a/(1/b)
# g=int(h)
# print(g)

        

        
    
















    
