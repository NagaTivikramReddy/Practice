
##--------------------- Dictionary-------------------
##
##my_dict = {'name':'Dhoni','team':'Inida','role':'Wk - batsman','alt_role':'Captain'}
##print(my_dict)
##my_dict['role'] = 'Captain'
##print(my_dict)
##
#### Dictionary is mutable
#### Key value pair
##
##a = my_dict['name']
##print(a)
##
####Unordered collection
####Hashing

##my_dict = {'name':'Vikram',7:[1,2,3],('a','b'):'tuple',False:'word'}
##print(my_dict[False])

## We can use all immutable data types are keys
## For example , We cannot use list as a key

temp = 0
##d = {False : 'Dhoni',True:'raina',1:'Kohli',1.0:'rohit',1+2-2:'qwerty',temp:'temp',temp+1:'one'}
##print(d)
##
#### Here False is equvalent to 0 and True is equivalent is 1 and 1.0

##for i in d:
##    print(i)
##
#### here only keys will be printed
##
##for i in d.items():
##    print(i)
##
#### here both keys values will be printed
##
##for i in d.values():
##    print(i)

## here only values will be printed

##d1 = {1:'Kohli',1.0:'rohit',1+2-2:'qwerty',temp:'temp',temp+1:'one',False : 'Dhoni',True:'raina'}
####
##print(d1)
##print(True)
##print(1)
##print(False)
##print(0)

##
##my_dict = {'name':'Vikram','age':{'values':[1,2,3]},('a','b'):'tuple',False:'word'}
##
##print(my_dict['age']['values'][0])

##temp_dict = {}
##for i in range(5):
##    temp_dict[i] = i**2
##
##print(temp_dict)
##
##new_dict = {x:x*x for x in range(5)} # -- Dictionary comprehension
##print(new_dict)

##s = {{'a':10,'b':20}:'vvvv','name':'vikarm'}
##print(s)
## output : TypeError: unhashable type: 'dict'

##s = {'a':10,'b':20,'name':'vikarm'}
##c = s
##c['a'] = 11
##s['b'] = 21
##print(s,c)

##
##var = {'name':'Dhoni'}
##var1 = {'age':40}
##
##var.update(var1)
##print(var)
##
##new = {**var, **var1}
##print(new)

##Presentation
##2 things
##
##1. we can use opeations as key
##2. if the keys are True or False we can use 1 or zero to access values and vice versa

w = {0:'zero',1:'one'}
print(w[0])

e = {1+2+3:10+20,'na'+'me':'vik'+'ram'}
print(e)



