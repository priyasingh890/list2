# Write a python program function that takes two lists and return True if they have at least one common members.
def common(a,b):
    for i in a:
        for j in b:
            if i==j:
                   return True
            else:
                return False
print(common([2,4,6,7,8],[9,10,11,12]))


def common_data(list1, list2):  
         result = False  
         for x in list1:  
             for y in list2:  
                 if x == y:  
                     result = True  
                     return result  
print(common_data([1,2,3,4,5], [5,6,7,8,9,5]))  



