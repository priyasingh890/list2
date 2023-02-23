t=int(input("enter no"))
f=int(input("enter unit "))
z=int(input("enter no rat."))

i=0
d=[]
while i<t:
    g=int(input("enter no"))
    d.append(g)
    i=i+1
print(d)
j=0
w=0
b=[]
while j<len(d):
    w=w+d[j]
    if w<=f*z or w==f*z :
        b.append(d[j])
        print(b)
    else:
        w=w-d[j]
    j=j+1
    # i=i+1


def add():
    d=5+6
    print(d)
add()
def hub():
    g=7-2
    print(g)
add()







