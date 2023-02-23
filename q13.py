# Write a python program to generate a 3*4*6 3D array whose each element is.
# array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
# print(array)

# b=[]
# for i in range(3):
#     b.append([])
# for j in range(4):
#     b[i].append(['*'])
# for k in range(6):
#     b.append([])
#     b[i][j].append('*')
# print(b)





# Python 3 code to implement above approach
 
# Function to find minimum operations
# # used to make permutation of 1 to N
# def minoperation(arr, N):
#     st = set([])
#     rem = []
 
#     # Storing one instance of every element
#     # from 1 to N
#     for i in range(1, N + 1):
#         st.add(i)
#         print(st)
 
#     for i in range(N):
#         if (arr[i] in st):
#             st.remove(arr[i])
 
#         else:
#             rem.append(arr[i])
#             print(rem)
 
#     # Sorting in descending order
#     rem.sort()
#     rem.reverse()
 
#     pt = 0
#     flag = False
 
#     for x in rem:
#         it = len(st)
#         it -= 1
#         p = list(st)[it]
#         if (p > (x - 1) / 2):
#             flag = True
#             break
 
#         st.remove(it)
 
#     if (flag):
#         # Not possible to make permutation.
#         print("-1")
 
#     else:
#         # Minimum number of operation required.
#         print(len(rem))
 
# # Driver code
# if __name__ == "__main__":
 
#     N = 3
#     arr = [1, 5, 4]
#     minoperation(arr, N)
a=[3,2,1]
a.sort()
print(a)