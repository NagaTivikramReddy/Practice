var = "India is"
##for i in var:
##    if i=='i' or i=="a":
##        print("Success")
##    else:
##        print("Failure")
##    break

##break -- Used to end any loop

##----------------------------------

var = "India is a Country"

for i,j in enumerate(var):
    print("{} is at index {}".format(j,i))

##enumerate -- gives index value pair
##
##Here i is represents index and j represents value at tht index

##---------------------------------

##for i,j in enumerate(var):
##    if i%2==0:
##        print("{} is at index {}".format(j,i))

##------------------------
##for i in range(2,20,4):
##    print(i)
##
##
##for i in enumerate(range(2,20,4)):
##    print(i)

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##--------------------LIST-----------------------------

##l=["Dhoni","raina","Kohli",["numbers",2,3,4]]
##print(l[0][3])
##print(l[3][0][4])

##deep copy
##var = [1,2,3,4]
##new_var = var -- ##now both var and new_var points to same address location
##
##print(var)
##print(new_var)
##
##new_var[0] = 10
##
##print(var)
##print(new_var)

## here both var and new_var are changed because both points to same address location

##Shallow copy
##var = [1,2,3,4]
##new_var = var[:]
##
##print(var)
##print(new_var)
##

##a=var.copy()
##a[2]=5555
##print(var)
##print(a)

##------------------------------------------

## List is mutable i.e. changable
## List uses the mechanism "LIFO"

lis = [1,2,3,4,5]
####insert
##lis.insert(2,1000)
##print(lis)
##
####append
##lis.append(200)
##print(lis)


## -- append is used to add an elememt at last and it can only add one extra index

## the below is not possible
##lis.append(22,44)

##We can do this
##lis.append([11,33])
##print(lis)
## output : [1, 2, 3, 4, 5, [11, 33]]

## -----------------------------

##extend

##lis = [1,2,3,4,5]
##
##lis.extend([33,55,77])
##print(lis)
## Output : [1, 2, 3, 4, 5, 33, 55, 77]

## -- extend is used to add multiple elements to a list

## ----------------------------------------------------------------------

##pop

p = ['dhoni','kohli','raina','M Hussey']
##print(p)
##p.pop(2)
##print(p)

## -- pop() is used to remove element at last if no index is specified and to remove that particular index element if it is specified

## ----------------------------------------------------------------------

## remove
##p.remove('kohli')
##print(p)

## -- remove() is used to remove a data. We need to specify the particular data

## ----------------------------------------------------------------------

## clear
##p.clear()
##print(p)

## -- clear() is used to empty a list

## ----------------------------------------------------------------------

## del
##del p
##print(p)

## -- del is used to delete the list

## -----------------------------------------

##output = []
##
##for i in range(9):
##    if i%2 == 0:
##        output.append(i)
##
##print(output)
#### output : [0, 2, 4, 6, 8]
##
#### -------------------------
##
##output1 = [x for x in range(9) if x%2 == 0] # list comprehension method
##print(output1)
#### output : [0, 2, 4, 6, 8]

## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
## ---------------------------Tuple-----------------------------

var = ('dhoni') # this is treated as string

var = ('dhoni',) # Now this is a tuple

## tuple is immutable

var = "dhoni","kohli" # This is treated as tuple by python
print(type(var))
## output : <class 'tuple'>

##&&&&&&&&&&&&&&&&&& IMP &&&&&&&&&&&&&&&&&&&&&&&&&&&

# Deep copy and Shallow copy



















 
