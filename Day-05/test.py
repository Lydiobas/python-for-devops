#command line arguments
#This is a command line argument used to pass inputs to the program like
#using a calculator to add two numbers to add
#e'g To list all the s3 buckets in an account use aws s3 ls
#where aws s3 ls is the input
#we want the user to enter their inputs on the cli argument

# import sys
# def add(boys, girls):
#     Total = boys + girls
#     return Total

# def sub(boys, girls):
#     Total = boys - girls
#     return Total

# def mul(boys, girls):
#     Total = boys * girls
#     return Total

# boys = float(sys.argv[1])
# operation = sys.argv[2]
# girls = float(sys.argv[3])

# if operation == "add":
# 	output = add(boys, girls)
# 	print(output)
     
# if operation == "sub":
# 	output = sub(boys, girls)
# 	print(output)

# if operation == "mul":
# 	output = mul(boys, girls)
# 	print(output)
 


# Incase of passing sensitive informations we use enviroment variables
#Things that users can not store in the cli
import os
#use export command to set enviroment variables
os.environ["password"] = "123456"
os.environ["apitoken"] = "123456"
os.environ["username"] = "admin"

password = str(os.environ["password"])
apitoken = str(os.environ["apitoken"])
usernames = str(os.environ["username"])

print(password)
print(apitoken)
print(usernames)