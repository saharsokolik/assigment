# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:23:09 2023

@author: sahar
"""
##Question1:
    
# def my_func(x1,x2,x3):
#     lst = [x1,x2,x3]
#     for i in lst: 
#         if not isinstance(i, float):
#             print("Error: parameters should be float")
#             return (None)
#     if x1+x2+x3==0:
#         print ("Not a number - denominator equals zero")
#         return (None)
#     formula = ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
#     return(float(formula))
    
# w=my_func(5.0,2.0,3.0)
# print(w)
# print(type(w))



##Question 2.a:

    
def revword(word:str):
    word=word[::-1].lower()
    return word
  

##Question 2.b:
def Countword(file):
    count = 0
    fhand = open (file)
    my_list=[]
    for i in fhand:
        i=i.rstrip()
        m=i.split(' ')
        for x in m:
            my_list.append(x)
    word=my_list[0]
    for seek in my_list[1:]:
            if word == revword(seek):
                count+=1
            else:
                continue
    return count+1

Countword("C:/phyton - exc/text.txt") 

#print(count+1) ##include the word varibaile
##RESULT IS 6

