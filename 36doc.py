# Write a Python program to join adjacent members of a given list.
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']

l= ['1', '2', '3', '4', '5', '6', '7', '8',"6"]
i=0
j=1
d=[]
while i<len(l) and j<len(l):
    s=l[i]+l[j]
    d.append(s)
    i=i+2
    j=j+2
print(d)




