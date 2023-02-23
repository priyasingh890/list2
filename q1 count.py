list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
a=[]
while i<len(list):
    j=0
    b=[]
    c=0
    while j<len(list):
        if list[i]==list[j]:
            c=c+1
        j=j+1
    if [list[i],c] not in a:
            a.append([list[i],c])
    i=i+1
print(a)
a="my name is priya"
i=0
k=""
h=[]
while i<len(a):
    if a[i]==" ":
        h.append(k)
        k=""
    else:
        k=k+a[i]
    i=i+1
h.append(k)
print(h)
#  0,10,0,0,10
#  200
        
n=int(input("enter no"))
i=1
min=n
max=n
while i<=10:
    n=int(input("enter no"))
    if n>max:
        max=n
    if n<min:
        min=n
    i=i+1
print("max",max)
print("min",min)
# # if i>=a:
#     print(i,"greater then")
# elif i<=a:
#     print(i,"less then")


# g=[1,2,3,4,5,6,7,8]
# d={}
# i=0
# j=1
# while i<len(g) and j<len(g):
#     d.update({g[i]:g[j]})
#     i=i+2
#     j=j+2
#     print(d)

# i=0
# j=1
# h=[]
# while i<len(g) and j<len(g):
#     d=g[j]
#     v=g[i]
#     h.append(d)
#     h.append(v)
#     i=i+2
#     j=j+2
# print(h)
# # 












