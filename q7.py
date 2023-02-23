#write a python program to remove duplicates from a list.
# list=[4,7,5,4,8,4,3,1,3,4,5,7]
# i=0
# k=[]
# while i<len(list):
#     if list[i] not in k:
#         k.append(list[i])
#     i=i+1
# print(k)

# string="hello word"
# string.strip("h")
# print(string)

# d.strip(
# print(d)

# a=[-1,-2,-8,-3,-4,-5,-6]
# a=[1,2,3,4,5',6,7,8]
# max=a[0]
# i=0
# while i<len(a):
#     if a[i]<max:
#         max=a[i]
#     i=i+1
# print(max)

# b=12345
# c=str(b)
# b=""
# for i in c:
#     b=i+b
#     print(b)


T=int(input("enter the"))
for i in range (T):
    v=int(input("enter the number"))
    u=int(input("enter the number"))
    t=int(input("enter the number"))
    sum=v+u+t
    divide=sum//3
    if divide!=1:
        print("yes")
    else:
        print("no")
