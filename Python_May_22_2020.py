#FUNCTIONS

##def my_func():
##    print("My name is Vikarm")
##
##my_func()
##
##def my_func(name):
##    print("My name is ",name)
##
##my_func('Trivikram')
##
##def my_func(name,age):
##    print("My name is {} and age is {}".format(name,age))
##
##my_func('Vikram',30) #position of parameters passed is very important
##
###dfault agruments
##def my_fun(name="Don",age=20):
##    print(name,age)
##
##my_fun()
##
###-------------------
##
##def my_fun(name="Don",age):
##    print(name,age)
##
##my_fun(20)
##
### here we should not give argumets as above, always we need to give defualt agruments at last
#-------------------------
####Functions with key word argumets
##
##def my_func(name,age):
##    print("My name is {} and age is {}".format(name,age))
##my_func(age=20,name='kkik')

#-------------------------

###args and kwargs
##
##def func(*names):
##    print(names)
##func('dhoni','sachin','kohli')
###output
###tuple
##('dhoni', 'sachin', 'kohli')
##
##def fun(**names):
##    print(names)
##
##fun(name='dhoni',age=39)
###output
###dictionary
##{'name': 'dhoni', 'age': 39}

#------------------------------

##def total_score(a,b,c):
##    total = a+b+c
##    return
##
##print(total_score(20,22,69))
###output
##None # because you just returned with no agrument


##def total_score(a,b,c):
##    total = a+b+c
##    return total
##temp = total_score(20,22,69)
##print(temp)
###output
##111

#-----------------------------
###return multiple values
##
##def total_score(a,b,c,name):
##    total = a+b+c
##    return total,name
##
##first,second = total_score(10,20,30,'India')
##print(first)
##print(second)
###output
##60
##India
##
##alll = total_score(10,20,30,'India')
##print(alll[0])
##print(alll[1])
###Output
##60
##India

#----------------------------
#Scoping
##
##a = 10
##def func():
##    a=100
##    def sub_func():
##        a=1000
##        print(a)
##    sub_func()
##
##func()
##LEG
##var = 100
##
##def f():
##    global var
##    var =  var*2
##    print(var)
##f() #200
##print(var) #200

##counter=0
##def t():
##    global counter
##    print('Hi')
##    counter = counter+1
##    
##    try:
##        t()
##    except(RecursionError):
##        print('count : ',counter)
##
##t()


##counter=0
##def t():
##    global counter
##    print('Hi')
##    counter = counter+1
##    while counter<100:
##        t()
##
##t()





    
dic = {}














