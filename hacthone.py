# s=[2,31,4,5,6,74]
# c=[]
# for j in s:
#     c=[j]+c
# print(c)

v=[3,6,7,8,9,2,1,6,3,8,3]
c=0
s=1
sum=0
for k in v:
    sum=sum+v[c]
    c=c+1
print("average",sum/c)
print("middle",v[(c//2)])
c=0
m=[]
for j in v:
    k=0
    b=0
    for l in v:
        if v[c]==v[k]:
            b=b+1
        k=k+1
    print(b)
    if b not in m:
        m=m+[b]
        sum5=0
        for z in m:
            if sum5<z:
                sum5=z  
    c=c+1
print("highest dublicate",sum5)

# h=[3,6,7,5,10]
# i=0
# while i<len(h):
#     j=0
#     n=0
#     c=0
#     while j<len(h):
#         c=n+1
#         if c<=3:
#             if c==3:
#                 print(h[j])
#         else:
#             n=n+1
#         j=j+1
#     i=i+1


            





        

# i=0
# while i<5:
#     i=i+1
#     if i==3:
#         continue
#     print(i)
# c=[2,6,9,3,9,0,1,5,6,7]
# d=[6,7,8,9]
# dic=c+d

# c=0
# for i in dic:
#     k=0
#     for j in dic:
#         if dic[c]<dic[k]:
#             dic[c],dic[k]=dic[k],dic[c]
#         k=k+1
#     c=c+1
# print(dic)


# k=[5,6,7,8,6,9,9]
# g=[]
# for s in k:
#     c=0
#     for d in k:
#         if s==d:
#             c=c+1
#     if c>1:
#         if s not in g:
#             g=g+[s]
# print(g)
# s=int(input("enter no."))
# g=[3,6,7,5,10]
# for i in g:
#     for j in g:
#         if i+j==s:
#             print(i,j)

# h=[5,7,8,9,3,2]
# g=[]
# for i in h:
#     z=[]
#     for j in h:
#         z=[i]
#     print(z)

# 7.Find the Union and Intersection of the two sorted arrays 
# a=[5,6,7,8,6,9,9]
# b=[2,3,4,5,6,8]
# for i in (a):
#     b=b+[i]
# d=[]
# for i in b:
#     if i not in d: 
#         d=d+[i]
# c=0
# for i in d:
#     k=0
#     for j in d:
#         if d[c]<=d[k]:
#             d[c],d[k]=d[k],d[c]
#         k=k+1
#     c=c+1
# print(d)




# . Find a number using Binary Search in a sorted array 
# g
# a=int(input("enter no."))
# while a>0:
#     c=(a%2)
    # a=a//2
    # print(c)
p=[10,2,7,8,9,2,3]
i=0
b=[]
k=[]
while i<len(p):
    g=""
    while p[i]>0:
        c=(p[i]%2)
        g=g+(str(c))
        p[i]=p[i]//2
    i=i+1
    b=b+[g]
x=0
l=[]
for  a in b:
    g=a
    u=1
    p=""
    for o in g:
        p=p+(g[-u])
        u=u+1
    l=l+[p]
print(l)

# g=int(input("enter no."))
# dic=[3,6,7,5,10,8]

# k=0
# for i in dic:
#     p=0
#     for a in dic:
#         p=k+1
#         if(dic[k]+dic[p])==g:
#             print(dic[k],dic[p])
#         p=p+1
#     k=k+1


# d=[]
# i=0
# while i<len(dic):
#     j=i+1
#     while j<len(dic):
#         if dic[i]+dic[j]==g:
#             print(dic[i],dic[j])
#         j=j+1
#     i=i+1














        








# p=[10,2,7,8,9,2,3]
# k=0
# for j in p:
#     g=""
#     for l in (0,j):
#         c=(j%2)
#         j=j//2
#         print(c)
#     print()
#     k=k+1
    


# h=[{"name":"rani","age":89},{"name":"priya","age":96}]
# max=0
# k=[]
# q={}
# for i in h:
#     k.append(i["age"])

#     b=(i["age"])
#     if max<=b  :
#         max=b
#         n=[max]

# for e in n:
#     for s in h:
#         print(s)
#         if s["age"]==e:
#             q.update({s["name"]:e})
# print(q)
    
        # if i[j




    # a=v
    # for h in (0,a+1):
    #     c=(a%2)
    #     a=a//2
    # print(c)


# dic=[3,6,7,5,10,8,9]
# i=0
# b=0
# while i<len(dic):
#     c=b
#     j=0
#     while j<len(dic):
#         if c%2==0 :
#             print(dic[j])
#             c=c+1
#         else:
#             c=c+1
#         j=j+1
#     #   )  print(c
#     b=b+c
#     i=i+1 

# rotation number
# dic=[3,6,7,5,10,6,3]
# i=0
# b=0
# while i<len(dic):
#     j=0
#     c=b
#     b=0
#     while j<len(dic):
#         c=c+1
#         if c==3:
#             print(dic[j])
#             c=0
#         j=j+1
#     b=c+b
#     i=i+1

# arr=[4,8,4,3,2,6,7]
# dic={}
# for i in arr:
#     if i not in dic:
#         dic[i]=arr.count(i)
# count=0
# for j in dic.values():
#     if j<=2:
#         count+=1
# if count==len(dic):
#     print("YES")
# else:
#     print("NO")




# dic=[3,6,7,5,10,8,9,2]
# i=0
# b=1
# while i<len(dic):
#     c=b
#     j=0
#     while j<len(dic):
#         if c%3==0:
#             print(dic[j])
#         else:
#             c=c-1
#             c=c+1
#         j=j+1
#     b=b+c
#     i=i+1

# i=0
# c=0
# while i<10:
#     if c==3:
#         c=c+1
#         continue
#     else:
#         c=c+1
#     i=i+1
#     print(c)


# dic=[3,6,7,5,10]
# i=0
# b=1
# while i<len(dic):
#     c=b
#     j=0
#     while j<=len(dic):
#         if c%3==0  and c!=0:
#             print(dic[j])
#             c=c+1
#         else:
#             c=c+1
#             pass
#         j=j+1
#     # print(i)
#     b=b+c
#     i=i+1

# a=str(input("enter a number"))
# print(a[::-2])


f=[1,11,4,3,42,63,84,15,]
# i=0
# while i<len(f):
#     j=1
#     c=0
#     while j<len(f):
#         d=str(f[j])
#         if d[-1]==str(i):
#             c=c+1
#         j=j+1
#     i=i+1
#     print(c)
# d=len(f)//2
# print(f[d],f[d-1])


# a=[3,5,7,11,9,13,1]
# k=3
# c=7
# h=0
# result=[]
# for i in range(0,c):
#     h=h+k-1
#     if h<c:
#         print(a[h])
#     elif h>=c:
#         print(a[h])
#     h=c-h
#     k=k+3
# s="abcabc"
# i=0
# j=0
# d=""
# k=""
# while i<len(s)//2 and j<=3:
#     d=d+s[i]
#     g=k+s[j]
#     i=i+1
#     j=j+1
#     print(d)
#     print(g)
#     # if d+g==s:
    #     print("yes")
#     # i=i+1
#     # j=j+1
# a=int(input("enter no"))
# i=1
# max=0
# while i<=a:
#     d=int(input("enter no"))
#     if max<d:
#         max=d
#     i=i+1
#     j=1
# while j<=max:
#     i=1
#     b=[]
#     while i<=a:
#         b.append(i)
#         i=i+1
#     j=j+1
#     print(b)
# c=int(input("enter no"))
# print(c%100//10)
# # v=c%10
# b=c//10
# l=c%10
# m=b//10
# z=m%10
# n=m//10
# a=n%10
# k=n//10
# s=k%10
# print(s)


# a="abcefc"
# i=0
# d=""
# c=""
# while i<len(a):
#     if len(a)//2>i:
#         d=d+a[i]
#     else:
#         c=c+a[i]
#     i=i+1
# if d==c:
#     print("yes")
# else:
#     print("no")
# f=7
# g=2
# print((f-g))


# x=2
# y=1
# i=0
# while i<100:
#     j=1
#     c=0
#     while j<100:
#         if (x+y)%j==0:
#             c=c+1
#         j=j+1
#     i=i+1
#     print(c)
    # if c==2:
    #     print("alice")
    # else:
    #     print("bob")

# a=int(input())
# b=int(input())
# for i in range(a):
# b=[2,4,7,8,2]
# i=0
# while i<len(b):
#     j=0
#     c=0
#     while j<len(b):
#         if b[i]==b[j]:
#             c=c+1
#         j=j+1
#     i=i+1
#     if c==1:
#         print("yes")
#         break
#     else:
#         print("no")
#         break









        




















