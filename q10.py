# write a python program to find the list of words that are longer than n from a given list of word 


d="The quick brown fox jumps over the lazy dog"
s=3
word_len = "" 
word=[]
i=0
while i<len(d):
        if d[i]==" ":
            if len(word_len)>s:
                word.append( word_len) 
            word_len = "" 
        else:
                word_len =  word_len+d[i] 
        i=i+1
word.append(word_len)
print(word)   



# def long_words(n, str):  
#         word_len = []  
#         txt = str.split(" ")  
#         for x in txt:  
#             if len(x) > n:  
#                 word_len.append(x)  
#         return word_len   
# print(long_words(3, "The quick brown fox jumps over the lazy dog")) 

# string="today'ss a ggreat day, istt it ?"
# print(string[0])
# mapping={"o":1,"t":4,"s":5,"g":6} 
# for i in mapping:
#         for j in string:
#                 if i==j or i!=j:
#                         print(mapping[i])                               




#                 # if mapping[i]



# a="today'ss a ggreat day, ,istt it ?"
# b={"o":1,"t":4,"s":5,"g":6}
# k=""
# for i in a:
#     if i in b:
#         for j in b:
#             if i==j:
#                 k+=str(b[j])
#     else:
#         k+=i
# print(k)

g=["siya","hello","morning","you"][bool("")]
print(g)











