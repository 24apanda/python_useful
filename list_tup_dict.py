# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 20:31:40 2016

@author: apanda88
"""
"""
Dictionary practice

fmenu={'tomato':20,'potato':10,'no':0}
order=input("place order between tomato ,potato or no(no option) ")
if order=='tomato':
    print("for tomato price will be","$","%d" %fmenu.get('tomato'))
elif order.lower()=='potato':
    print("for potato price will be","$","%d" %fmenu.get('potato'))
else:
    print("for potato price will be","$","%d" %fmenu.get('no'))
    
"""
"""
list=[1,3,5,6,9,10]
for i in list:  
    print(i)"""
"""   
tup_list=[(1,'as'),(3,'ab'),(5,'cd')]
for (i,j) in tup_list:
    print(i,j) """
    
"""fmenu={'tomato':20,'potato':10,'no':0}
for k,v in fmenu.items():
    print (k,v)"""
"""    
mix=['a',(5,6),3.14]
val=[(5,6),3.14]
for i in val:
    if(i in mix):
        print("val found :",i)
    else:
        print("no result")"""
        

"""
#####
Tuple is imutable and faster than list because of its static nature
cann't per form append(),remove(),insert(),extend() 

len()
type conversion tuple -> list ,tuple ->tuple 

Tuple can be used as dict keys .
"""
"""
tup=(1,'as',3.13,'same car',3.13)
var=tup[0:3] #slicing the tuple
print(tup.index(3.13),'' ,var) #print index value
cnt=tup.count(3.13)
print(cnt)#count the no. of occurances"""
"""
##enumerate()
Return an enumerate object. 
It contains the index and value of all the items of set as a pair.
lis1=[1,3,4]
#lis1[1]=2
#lis2=lis1.index(3)
#lis3=lis1.insert(lis2,2)
#lis4=lis1.remove(3)
#lis1[lis2]=2
'''for i in range(0,lis1.__len__()):
    if(lis1[i]==3):
        lis1[i]=2
'''
for i,v in enumerate(lis1):
    if(v==3):
        lis1[i]=2
    #print(i)
        
print(lis1)"""


"""########List##########
lis1=[1,'as',3.13,'same car',3.13,'gita','babita',45,90]
lis2=lis1[0:5]
print(lis2)
rmv=lis2.remove(3.13) #remove first argument or first value
print(lis2)
lis_tup=tuple(lis2) #list to tuple conversion
print(lis_tup)
lis2.append(9999)##append
print(lis2)
lis2.count(1)###count occurance
print(lis2.count(1))

print(lis2.append('eggs'),"\n",lis2)
lis2.insert(4,'hello')
print(lis2)
#lis2.sort() always work on same datatype
"""

#######Dictionary##########
"""pop()-Remove key value from dict
clear()-purge all items from dict"""
"""

months={1:'jan',2:'feb',3:'mar'}
months[2]
print(months[2])
months[4]='apr'
#months[3]='apr' will replace the value
print(months)
print(months.keys())
print(months.values())

months2listkey=list(months.keys())
months2listval=list(months.values())
print(months2listkey,'\n',months2listval)
lis1=[1,'as',3.13,'same car',3.13,'gita','babita',45,90]
tup=(1,'as',3.13,'same car',3.13)
months[5]=lis1
months[6]=tup
print(months)

print(len(months))
months.pop(1)
print(months)"""

"""
#########comprehensesion###########
fmenu={'tomato':20,'potato':10,'no':0}
tup=(12,122,124)
fmenu[4]=tup
fmenu1={value:key for key,value in fmenu.items()}
print(fmenu1)
#Note -list can't  be used in dic comp because of hash key violation
"""

"""

lis1=[1,2,3,4,5,6,1,2,3,7,9]
while lis1.__contains__(2 or 3 or 1):
    for i,v in enumerate(lis1):
        if(v==2 or v==1 or v==3):
            lis1.remove(v)

print(lis1)"""
"""
# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)"""

"""
my_tuple = (4, 2, 3, [6, 5])

# we cannot change an element
# If you uncomment line 8
# you will get an error:
# TypeError: 'tuple' object does not support item assignment

#my_tuple[1] = 9

# but item of mutable element can be changed
# Output: (4, 2, 3, [9, 5])
my_tuple[3][1] = 9
print(my_tuple)

# tuples can be reassigned
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple)"""



