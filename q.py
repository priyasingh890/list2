# s=[[2,3,4]]
# f=len(s)
# d=len(s[0])
# t=f,d
# print(t)
# li=[1,2,3,5,6,4,5,6,7]
# i=0
# j=1
# h=[]
# while i<len(li) and j<len(li[j]):
#     h.append(li[i])
#     j=j+1
#     i=i+1
# print(h)



# a= int(input("enter no"))
# j=10
# i=0
# h=0
# while i<a:
#     d=j+h
#     print(d)
#     i=i+1
#     h=h+5

# f={1:"2",2:"2",3:"3",4:"4",5:"5"}
# g={}
# c=0
# for i in f:
#     c=c+1
#     if c!=3:
#         g[
# i]=f[i]
# print(g)
# i=1
# a=int(input("enter no"))
# if a%i==0:
#     print(i)
# i=i+1
# a=a%i


a=[1,1,2,3,4,4,5,1]
i=0
l=[]
while i<len(a):
    j=0
    c=0
    m=[]
    while j<len(a):
        if a[i]!=a[j]:
            break
        else:
            c=c+1
        j=j+1
    i=i+1
    if c>1:
        if c not in m:
            m.append(c)
            m.append(a[j])
            l.append(m)
        else:
            l.append(a[i])
    print(l)



    









