# 14. Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
#



# l= [[0], [1, 3], [5,7,8,9,4], [9, 11], [13, 15, 17]]
# # 
# i=0
# max=len(l[i])
# min=len(l[i])
# while i<len(l):
#     j=0
#     while j<len(l):
#         if (max)<len(l[j]):
#             max=len(l[j])
#             m=l[j]
#         elif min >len(l[j]) and len(l[j])!=min:
#             min=len(l[j])
#             k=l[j]
#         j=j+1
#     i=i+1
# print((max,m))

# d=[1]
# for i in d:
#     print(i)
#     d.append(i+1)
# print(d)

# f=int(input("enter no"))
# b=f//10
# n=b%10
# if n%5==0:
#     print("yes")
# else:
#     print("no")
fname=str(input("enter fisrt name"))
lname=str(input("enter last name"))
print(lname+fname)