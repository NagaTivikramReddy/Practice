## Data Types - Strings, Numbers, Tuples, List, Dictionary
##
## Mutable - List, Dictionary (When modification is possible by its index)
##
## Immutable - Strings, Numbers and tuples (when modification is not possible by its index)

##print("Vikram")
##name="Vikram"
##print(type(name))
##
##
####commenting in python idle - alt + 3
####uncommenting in python idle - alt + 4
##
##print ("nknn")
##print(name[3])
####name[2]='l' -- TypeError: 'str' object does not support item assignment
##print(name)
##
##line = "I love CSK"
##print(line[0:])
##print(line[0:6])
##print(line[-1:2]) -- Blank
##print(line[-2])
##print(line[-5:])
##
####slicing always goes in forward direction

String ='ASTRING'
  
# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2) 
s3 = slice(-1, -12, -2)
  
print("String slicing") 
print(String[s1]) 
print(String[s2]) 
print(String[s3])




##
##print(len(line))
##print(dir(line))
##
####len() and dir() are two functions which can be applied on all data types
##print(line.islower())
##
####Multiline character
##country='''Inida is country
##I love India'''

##country='''Inida is country \
##I love India'''
####Here \ acts as a escape new line character
####\n -- new line
####\t -- tab space
##print(country)
##
##country=r'''Inida is country \
##I love India'''
####Here r means raw data
##
##print(country)

##n=r"""C\new\table\ """
##print(n)
##m=r'''\fg\ '''
##print(m)
##We cannot give \" at last. we can place a space after \ to print a string ending with \
