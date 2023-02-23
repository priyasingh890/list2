# 12. You will be given a number and you need to return it as a string in Expanded Form. For example:
# Should return '10 + 2'
# Should return '40 + 2'
# Should return '70000 + 300 + 





num=input("enter the no:")
s=[]
i=len(str(num))-1
for n in str(num):
    if n!="0":
        s.append(n+"0"*i)
    i-=1
    b="+".join(s)
print(b)
