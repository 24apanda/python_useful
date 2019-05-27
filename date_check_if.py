# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Month and date
month=eval(input("Enter the month between 1 to 3 :"))
day=eval(input("Enter date between 1 to 3 :" ))
if month ==1:    
     print("jan",end='')
elif month==2:
    print("feb",end='')
elif month==3:
    print("march",end='')
else:
    print("no data",end='')

if day==1:
    print(",","1st",end='')
elif day==2:
    print(",","2nd",end='')
elif day==3:
    print(",","3rd",end='')
else:
    print("\n","month",month,",","day",day,"not valid as per record")


    
    

    