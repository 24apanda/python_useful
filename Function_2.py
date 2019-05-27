# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:21:14 2017

@author: apanda88
"""
#########Argument@############
"""
def greet(name, msg = "Good morning!"):
   
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

  # print("Hello",name + ', ' + msg)"""
"""
greet("Kate")
greet("Bruce","How do you do?")"""

############Arbitrary Arguments########33
"""def greet(*name):
    
    for i in name:
        print("hello",i)
        
greet('ashu','mama','alu')"""

#############Ananymous function########

#####Lambda####3

double=lambda x:x+2
print(double(5))

###filter

my_list=[1,2,3,4,5,6]

new_list=list(filter(lambda x:(x%2==0),my_list))
new_list1=list(filter(lambda x:(x-3 <2),my_list))

print(new_list)
print(new_list1)

############  Map #####

my_list=[1,2,3,4,5,6]

new_list22=list(map(lambda x:(x%2==0),my_list))
new_list2=list(map(lambda x:(x**2),my_list))
#new=list(reduce(lambda x,y:x+y,new_list2))
#new_list23=list((lambda x:(x**2),my_list))

print(new_list22)
print(new_list2)
#print(new_list23)

##########

terms = 10

# Uncomment to take number of terms from user
#terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms+1)))
print(result)

# display the result

print("The total terms is:",terms)
for i in range(terms+1):
   print("2 raised to power",i,"is",result[i])

   ##############
sentence = 'It is raining cats and dogs'
words = sentence.split()
print (words)
 
lengths = map(lambda word: len(word), words)
print (lengths)


