# def add():
#     b=4+5
#     print(b)

# def sub():
#     c=9-4
#     print(c)
# def multi():
#     d=6*3
# def divide():
#     s=10/2
#     print(s)
# def calcular(b,c,d,s):
#     if b=="t":
#         add()
#         if c=="k":
#             sub()
#             if d=="e":
#                 multi()
#                 if s=="w":
#                     divide()
# calcular("t","k","e","w")

# # 1.user input
# # user input operator


# # s="priya"
# # i=1
# # sum=""
# # while i<len(s):
# #     sum=""+s[-i]*2
# #     print(sum,end="")
# #     i=i+1

# # d="my name is siya"
# # print("siya"in d)
# # a=15
# # b=17
# # print(a^b)


# str1 = "Welcome \tto my Blog"
# str2 = "Welcome to\n my \tBlog"
# print(str1)
# print(str2)

# # str1 = “”” Welcome to my
# #       blog.
# # This is for
# # Class X”””
# # print(str1

# str="hello"
# print(str[:3])

# str[i]str=’My Blog’
# a=’ ‘
# for i in range(len(str)):
# a+=
# print(a)

# print(“My”+’Blog’ * 2)

# print("My" *3 + "Blog"+"7")

# str1 = "Welcome to my Blog"
# x = str1.split()append
# print(x)




# a=[1,4,6,7,9,2]
# i=0
# b=[]
# c=[]
# count1=0
# count2=0
# sum1=0
# sum2=0
# while i< len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#         sum1=sum1+a[i]
#         count1=count1+1
#     else:
#         c.append(a[i])
#         sum2=sum2+a[i]
#         count2=count2+1
#     i=i+1
# b.append(sum1)
# b.append(count1)
# c.append(sum2)
# c.append(count2)
# # print(b)
# # print(c)

# a=[2,4,7,8,9,2,5]





# a=int(input("hour no."))
# b=int(input("minute no."))
# print(a*30+(b*30/60))

# a=int(input("total feet no"))
# b=int(input("fall down feet."))
# c=int(int(input("reach feet")))
# print((a-b)*c)



	
# y=int(input("enter no"))
# m=int(input("enter no."))
# d=int(input("enter no"))
# if len(str(y))==4:
#     if m<=12 and m>0:
#         if d>0 and d<=31:
#             print(y,"-",m,"-",d)
# else:
#     print("wrong")


# 12. Write a program to print in an input number is power of 3. Without using any maths library (10)
# 
# def Power_Three(n):
#     if (n <= 0):
#         return False
#     if (n % 3 == 0):
#         return Power_Three(n // 3)
#     if (n == 1):
#         return True
#     return False
# num1 = int(input("enter no"))
# if (Power_Three(num1)):
#     print("Yes")
# else:
#     print("No")
# # # # 
# 0. Write a piece of code to reverse the contents of an array, you cannot create a new array the
# contents have to be replaced in the same array (3)

# a=[1,3,7,8,9]
# h=[]
# for i in a:
#     h=[i]+h
# print(h)

# A coaching institute teaches only standard 10th students for 3 subjects - Physics, Chemistry and
# # Mathematics. It has 3 periods every day one for each subject. It has 5 sections. What is the
# minimum number of teachers required to teach in that institute Assume one teacher can teach
# only one subject (1)

# a= int(input("enter subject"))
# b=int(input("enter section"))
# print(a*b)


# f=open("demofile2.txt","w")
# f.write("ths is a dog\n")
# f.write("my favorite colour pink")
# f.close()
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!\n")
# f.close()

# Write a piece of code to count the number of words in a file (3)

# file = open("demofile2.txt", "rt")
# data = file.read()
# words = data.split()
# print(words)

# print('Number of words in text file :', len(words))
print(3**8)