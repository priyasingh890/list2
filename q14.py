# Write a python program to print  the numbers of specified list after removing even numbers from it.
num = [7,8, 120, 25, 44, 20, 27]
r=[]
i=0
while i<len(num):
    if num[i]%2!=0:
        r.append(num[i])
    i=i+1
print(r)


