# write a python program to check a list is empty or not.
# list=[]
# if len(list)==0:
#     print("empty")
# else:
#     print('not empty')

# print(-18
# s=11
# print(s>>2)

# p=2**9
# print(p)
# a=2+3j
# b=2+3j
# print(a*b)

# list=[10,11,12,13,14,17,18,19]
# i=0
# g=[]
# while i<len(list):
#     j=1
#     k=[]
#     while j<len(list):
#         if list[i]+list[j]==30:
#             k.append(list[i])
#             k.append(list[j])
#             g.append(k)
#         j=j+1
#     i=i+1
# print(g)

m=["mom","dad","nan","bob","aya"]
i=0
c=0
while i<len(m):
    b=m[i]
    j=1
    sum=""
    while j<=len(b):
        sum=sum+b[-j]
        j=j+1
    if b==sum:
        c=c+1
    i=i+1


print(c)


