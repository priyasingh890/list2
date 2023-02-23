# 20. Write a function that takes one argument “n” and delete that many elements from the list.
# delete_nth ([1,1,1,1],2) # return [1,1]
# delete_nth ([20,37,20,21],1) # return [20,37,21
c=([20,37,20,21],2)
i=0
d=[]
while i<len(c[0])-(c[1]):
    d.append(c[0][i])
    i=i+1
print(d)
f=int(input("enter no."))
i=0
g=[]
marsheet=[]
scoret=[]
while i<f:
    name=input("enter no.")
    score=float(input("enter no"))
    marsheet=[[score,name]]
    scoret+=[score]

    i=i+1
scoret.sort()
print(scoret[0])
# for n,s in sorted(marsheet):
#     pass

#     # d=[name,score]
    # g.append(d)
    # g.sort()
    # i=i+1
    # s= sorted(list(set([x[1] for x in d ])))
    # print(s)


