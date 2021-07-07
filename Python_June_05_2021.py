#this is DB operation
import sqlite3

def get_data():
    status = False
    while(status == False):
        name1 = input("Enter ur name: ")
        age = int(input("Enter ur age: "))
        
        n1 = int(input("enter the 1st operand: "))
        n2 = int(input("enter the 2nd operand: "))

        print("Please use the following codes for operations")
        print("d - division, m - multiplication , a - additin, s - subtraction")
        operation = input("Enter the operation u want to perform: ")
        if operation == 'd':
            status = True
            res = n1/n2
            
        elif operation == 'm':
            status = True
            res = n1*n2
            
        elif operation == 'a':
            status = True
            res = n1+n2
            
        elif operation == 's':
            status = True
            res = n1-n2
            
        else:
            status = False
            print("Please enter the valid operation")
            print("Please use the following codes for operations")
            print("d - division, m - multiplication , a - additin, s - subtraction")
        
        
        return (name1,age,n1,n2,operation,res)
         
    

def insert_data():
    
    insert_query = """INSERT INTO EMPLOYEE(name, age, num1, num2, operation, result) VALUES (?, ?, ?, ?, ?, ?);"""
        
    query_execution = connection.execute(insert_query,data)
    print()
    print("Inserted Data")

def print_data():
    select_query = """select * from EMPLOYEE"""
    select_results = connection.execute(select_query)
    output = select_results.fetchall()
    print("Below is the all Data in the table 'Employee' ")
    for record in output:
        print(record)

print("Welcome.........")  

temp = 0
while(temp == 0):
    try:
        connection = sqlite3.connect("example1.db")
        print("Connection opened")
        #Get data
        data = get_data()

        #Insert data into the table
        insert_data()

        
    except (TypeError,ZeroDivisionError,ValueError) as e:
        print()
        print("encountered error.", e)
        print()
        
    except:
        print("Unknown error occured")
        temp = 1
        
    
    else:
        print()
        print("Awesome... No errors. Committing the operation")
        print()
        
        #save the changes made
        connection.commit()

        #Print all data from Employee data
        print_data()
    
        print()
      
        print("Enter n for exiting or any other key to try again..")
        again = input("Do u want insert another record ..(y/n)?")
        if again == 'n':
            print("Thank You byee...")
            temp = 1
        else:
            temp = 0

    finally:
        #close the connection
        
        connection.close()
        print("Connection closed")
    
