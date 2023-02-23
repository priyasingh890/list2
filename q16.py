# Write a python program to generate print a list except for the first 5 element where the value of numbers are  square between 1 to 30.
# def printValues():
# 	l = list()
# 	for i in range(1,31):
# 		l.append(i**2)
# 	print(l[5:])
# printValues()
i=0
c=[]
while i<(31):
    if i>=6:
        c.append(i**2)
    i=i+1
print(c)


