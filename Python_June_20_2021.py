## +	One or more occurrences
## *	Zero or more occurrences

## ^   starts with
## $   ends with



# Mongo DB
##It is a open source ,Document - oriented database
##Used for high volume
##
##Data is stored in the form of collections and socuments
##Example: Student details
##    {object_d : "njajhjbb779hiabd98", "name":"Vijram","age":"55}
##    {"name": "Dhoni"}
##    {"name":"Virat"}
##all the documents should be in the form of dictionry
##     all the documents when u store will get an unique Objecy Id whicch is created automatically
##    
##Two ways to work with MongoDB
##     1.through CLI(Command Line interpreter)
##     2. GUI
##Tools - Compass(default), robomongo
##
###Running procedure:
##     open vmd and run something like 'mongod'
##     CLI
##     it can run over multiple servers

#------------------------------

####JSO
##
##import json
##
### python object(dictionary) to be dumped
##dict1 ={
##	"emp1": {
##		"name": "Lisa",
##		"designation": "programmer",
##		"age": "34",
##		"salary": "54000"
##	},
##	"emp2": {
##		"name": "Elis",
##		"designation": "Trainee",
##		"age": "24",
##		"salary": "40000"
##	},
##}
##
### the json file where the output must be stored
##out_file = open("myfile.json", "w")
##
##json.dump(dict1, out_file, indent = 1)
##
##out_file.close()

##import json
##   
### Opening JSON file
##f = open('myfile.json',)
##   
### returns JSON object as 
### a dictionary
##data = json.load(f)
##   
### Iterating through the json
### list
##for i in data['emp_details']:
##    print(i)
##   
### Closing file
##f.close()


import json
var = '{"name":"Vikram","age":100}'
print(type(var))
out = json.loads(var) #converts str to dict
print(type(out))
inp = json.dumps(out) #converts dict to str
print(type(inp))














     
