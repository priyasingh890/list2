# 13. Write a Python program to create a list reflecting the modified run-length encoding from
# a given list of integers or a given list of characters.
# Original list:
# 1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String





l=[ 1, 1, 2, 3, 4, 4, 5, 1]
i=0
d=[]
while i<len(l):
    j=0
    c=0
    while j<len(l):
        if l[i]==l[j]:
            c=c+1
        j=j+1
            
    if c>1:
        if [c,l[i]] not in d:
            d.append([c,l[i]])
    else:
        d.append(l[i])
    i=i+1
print(d)










