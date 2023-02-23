w=int(input("enter no."))
a=[1,2,3,4,5,6,7,8,9,10,45,78,90,23,78,25,90,34,56,78]
e=[]
i=0
c=0
while i<len(a):
    if i%2==0:
        c=c+1
        d=w*c
        e.append(d)
    else:
        e.append(a[i])
    i=i+1
print(e)


name=input("enter the name")
i=0
while i<len(name):
    k="aeiou"
    if name [i] in k:
        print("vowles",name[i])
    else:
        print("consonant",name[i])
    i=i+1
print(name)


d=[1,2,3,[4,5,6,7],8]
i=0
sum1=0
sum2=0
while i<len(d):
    if type (d[i])==list:
        j=0
        while j<len(d[i]):
            sum2=sum2+d[i][j]
            j=j+1
    else:
        sum1=sum1+d[i]  
    i=i+1
print(sum1) 
print(sum2)     


a=int(input("enter the number"))
b=int(input("enter the number"))
while a<=b:
    i=1
    while i<=10:
        print(a,"*",i,"=",a*i)
        i=i+1
    print()
    a=a+1

for i in range(1,11):
    while i<=100:
        print(i,end=" ")
        i=i+10
    print()


s="abcd"
s=s[-1]+s[1:-1]+s[0]
print(s)

s="my name is abc"
s_value=[]
tmp=''
for c in s:
    if c=="":
        s_value.append(tmp)
        tmp=""
    else:
        tmp=tmp+c
if tmp:
    s_value.append(tmp)
    print(s_value)

name=input("enter the name")
i=0
while i<len(name):
    k="aeiou"
    if name[i] in k:
        print("vowels",name[i])
    else:
        print("consonant",name[i])
    i=i+1
print(name)

n=int(input("enter the number"))
list=[]
i=1
while i<=n:
    name=input("enter the name")
    list.append(name)
    i=i+1
print(list)

num=int(input("enter the number"))
k=[]
i=1
while i<=num:
    name=input("enter the name")
    k.append(name)
    i=i+1
print(k)

#
