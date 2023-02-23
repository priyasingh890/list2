# 33. Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
l=[23, 67, 98, 34]
i=0
h=[]
while i<len(l):
    s=str(l[i])
    j=0
    v=0
    while j<len(s):
        v=v+int(s[j])
        j=j+1
    h.append(v)
    i=i+1
print(h)



