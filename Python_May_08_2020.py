#STRING OPERATIONS

##value="Dhoni is my history"
##
##print("Count : ",value.count("i"))
###Output : 3
##
##print("Find : ",value.find("i"))
###Output : 4
##
##print("Index : ",value.index("i"))
###Output : 4
##
##print("rfind : ", value.rindex("i"))
###Output : 13
##
##print("rindex : ",value.rindex("i"))
###Output : 13
##
####print(value.index("l"))
###Output :
####Traceback (most recent call last):
####  File "C:\Users\VIKRAM\OneDrive\Desktop\Python - Netzwekk\Python_May_08_2020.py", line 13, in <module>
####    print(value.index("l"))
####ValueError: substring not found
##
##print(value.find("l"))
###Output : -1
##
###Note : The index() method is similar to find() method for strings.
###The only difference is that find() method returns -1 if the substring is not found, whereas index() throws an exception

statement = "My captain scored against Sri Lanka"
score = 77
name = "MS Dhoni"
##
###Using '+' we can only merge string data types
##statement = "My captain " +name+ " scored "+str(score)+ " against Sri Lanka"
##print(statement)

#%s -- string and %d -- integer
statement = "My captain %s scored %d against Sri Lanka" %(name,score)
print(statement)

###We need to place the variables in the order we want
##statement= "My captain {} scored {} against Sri Lanka".format(name,score)
##print(statement)
##
##statement = f"My captain {name} scored {score} against Sri Lanka"

##print(dir(str))

#statement.


###Looping(Iteration)
##
##s = "India is "
##
##for i in s:
##    print(i)
##
##for i in s:
##    if i=='i' or i == 'a':
##        print("Success")
##    else:
##        print("Failure")
##
##print("--------")
##for i in s:
##    if i=="i":
##        print("Success")
##    elif i=="a":
##        print("Success")
##    else:
##        print("Failure")
















    






















