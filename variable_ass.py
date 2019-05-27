# -*- coding: utf-8 -*
###number
x=int(input("provide first val ? "))
y=int(input("provide second val ?"))
print("their sum is" ,x,'+',y,'=',x+y)
print(type(x+y))

##string
q='asdf'
w='zasa'
print(q+w)#string concat

####eval can't work on string datatype

a=eval(input("string1 :"))
print(a)
z=eval(input("string2 :"))
print(a,end='') ##end=''  --use for concat
print(z,end='')
print(a,z)
print(type(a))
