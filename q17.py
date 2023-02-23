
#27. Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
#Examples:
l= [1, 2, 3]
l=[1,2]
#Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
for i in l:
    for j in l:
        for k in l:
            if i!=j and i!=k and k!=j and k!=i and j!=i and j!=k:
                print(i,j,k)
# i=1
# while i<len(l):
#     j=1
#     while j<len(l):
#         k=1
#         while k<len(l):
#             if i!=j and i!=k and k!=j and k!=i and j!=i and j!=k:
#                 print(i,j,k,end="")
#             k=k+1
#         j=j+1
#     i=i+1
# f=[ 3,5,6,8,9,2,6,1,6,8]   
# i=1
# n=[]
# while i<len(f):
#     if i%5==0:
#         n.append(20)
#     else:
#         n.append(f[i])
#     i=i+1
# print(n)

# _s=6
# b=5
# 3=10
# print+(+b+"3")

