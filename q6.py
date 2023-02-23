# Write a python program to get a list sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples
#Sample list [(2,5),(1,2),(4,4),(2,3),(2,1)]
#Expected result [(2,1),(1,2),(2,3),(4,4),(2,5)]

def last(n): 
    return n[-1]
def sort_list_last(tuples):
  return sorted (tuples, key=last)
print(sort_list_last([[2, 5], [1, 2], [4, 4], [2, 3], [2, 1]]))


        


l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

lst = len(l)

for i in range(0, lst):
    for j in range(0, lst-i-1):
        print(j)
        if (l[j][-1] > l[j + 1] [-1]):
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp
print(l)



l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
i=0
while i<len(l):
    j=0
    while j<len(l)-i-1:
        if (l[j][-1] > l[j + 1] [-1]):
            l[j],l[j+1]=l[j+1],l[j]
        j=j+1
    i=i+1
print(l)
            
         

