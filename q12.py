# Write a python program to print a specified list after removing the 0th ,4th and 5th element 
#Sample list ["red","green","white","black","pink","yellow"]
#output ["green","white","black"]
list =["red","green","white","black","pink","yellow"]
d=[]
i=0
while i<len(list):
    if i==0 or i==4 or i==5:
        pass
    else:
        d.append(list[i])
    i=i+1
print(d)



