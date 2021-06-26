#GitHub

#Version control

#--------------------------

#DB

#mysql, oracle, mongo,sqllite3
#sqlconnector, cx_oracle, pymongo, sqllite3
import sqlite3

###connect to DB
##connection = sqlite3.connect("vikram.db")
##
####Create tabel
####create_query = """create table Employee ("Name" text, "Age" integer)"""
####query_execution = connection.execute(create_query)
##
###Insert data into the table
####insert_query = """insert into Employee ("Name", "Age") values ("dhoni", 39)"""
####query_execution = connection.execute(insert_query)
##
###Select data from the table
##select_query = """select * from Employee"""
##query_execution = connection.execute(select_query)
##output = query_execution.fetchall()
##print(output)
##
##connection.commit()
##connection.close()

#Using function
##def my_db(db,query):
##    connection = sqlite3.connect("vikram.db")
##    query_execution = connection.execute(query)
##    output = query_execution.fetchall()
##    print(output)
##    connection.commit()
##    connection.close()
##
##db = "vikram.db"
##query = '''insert into Employee ("Name", "Age") values ("Kohli", 33)'''
##my_db(db,query)

#------------------------------------------

#FILES

##file_obj = open("vikram.txt","w")
##file_obj.write("my first line")
##
##file_obj.close()
##
##f = open("vikram.txt","r")
##print(f.read())
##f.close()

###context manager
##with open("vikram.txt","w") as file_object:
##    file_object.writen("my second content")
##
###If we use context manager method file willbe closed compulsorily

###append
##with open("vikram.txt","a") as file_object:
##    file_object.write("my second content")

#read
##with open("vikram.txt","r") as f:
##    content = f.read(5) #read first five characters
