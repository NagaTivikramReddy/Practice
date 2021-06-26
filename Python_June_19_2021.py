##Regular expression

##application:
##    1. cliet side validation
##
##
##
import re

#match() ##to check if the first word in "your word"

import re

##var = "Welcome to python programmin"
##output = re.match("Welcome",var)
##print(output)
##print(output.group()) #Welcome
##print(output.span())  #(0,7)
##
##var = "Welcome to python programmin"
##output = re.search("python",var)
##print(output)
##print(output.group()) 
##print(output.span())

##var = "Welcome to python programmin py"
##output = re.search("py",var,re.I)
##print(output)
##print(output.group()) 
##print(output.span())

##var = "<HTML><BODY><HEAD> <HTML><BODY><HEAD> <HTML><BODY><HEAD>"
##output = re.search("<.*>",var) #greedy mathod
##print(output.group()) #<HTML><BODY><HEAD>
##
##
##var = "<HTML><BODY><HEAD>"
##output = re.search("<.*?>",var) #non greedy method
##print(output.group()) #<HTML>


##var = "sachin is greatest than lara"
##output = re.search(".*is.*",var)
##print(output.group())
##
##var = "sachin is greatest than lara"
##output = re.search("(.*)is(.*)",var)
##print(output.group())
##print(output.group(1))
##print(output.group(2))


var = ".jbjbfsbj* is used .*  to match all"
output = re.search(r"(^.$*)",var)
print(output.group())

##var = "sachin is greatest than lara"
##output = re.search("(.*) is (.*) (.*)",var)
##print(output.group())
##print(output.group(1))
##print(output.group(2))
##print(output.group(3))
##
##var = "sachin is greatest than lara"
##output = re.search("(.*) is (.*?) (.*)",var)
##print(output.group())
##print(output.group(1))
##print(output.group(2))
##print(output.group(3))


##var = "INDIA scored 423 against SriLanka in 49.4 overs in 2013 with 8 runs per over"
##output = re.findall('\d{1,3}',var)
##print(output)
##
####findall() returns a list
##
####here \d means match numbers
####{1,3} means match 1 digit 2 digit and 3 digit
##
##
##var = "INDIA scored 423 against SriLanka in 49.4 overs in 2013 with 8 runs per over"
##output = re.findall('\D{1,3}',var)
##print(output)
##
####here \D means match other than numbers


##var = "44444444444444444444444888888888888888888"
##output = re.findall('\d',var)
##print(output)


var = "INDIA scored 423 $ ^ *against SriLanka in 49.4 overs in 2013 with 8 runs per over"
##output = re.findall('\w{1,2}',var)
##print(output)
##
####/w mathes all other than special characters
##
##output = re.findall('\w*',var)
##print(output)
##
##output = re.findall('\w+',var)
##print(output)

##/W meand only special charaters

##output = re.findall('\W{1,2}',var)
##print(output)
##
##
##output = re.findall('\W*',var)
##print(output)
##
##output = re.findall('\W+',var)
##print(output)

var = "Asia and China are same"
##output = re.findall('[A-Ca-z]+',var)
##print(output)
##
##output = re.findall('[A-Ca-z]*',var)
##print(output)

##output = re.sub('A','a',var)
##print(output)
##
##output = re.split('a',var)
##print(output)























