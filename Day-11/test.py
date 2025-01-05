# #why uses dictionary in python
# #we need not to store just the name of an item in a list , turple or string
# #but also to store the properties of the item which can be done using dictionary
# #eg name of ec2 instance , id of ec2 instance , type of ec2 instance etc
# #if you need information about a resource the response will be in a json format which you need to 
# #convert to a dictionary
# #it starts with {} brackets 
# # The properties will be in keys and values

# #with the example below you can print each property as indicated on line 24

# student_details = {
#     "name": "John",
#     "age": 30,
# 	"gender": "male",
# 	"address": "123 Main Street",
# 	"phone": "000000000000",
# 	"state": "New York",
# 	"country": "USA",
# 	"zip": "12345",
# 	"class": "Biology",
#     "city": "New York"
# }
# print(student_details["age"])

# #To store multile properties of an item you can use a list
# # use will use list of dictionaries
# #eg
# ec2_instances = [
#     {
#         "name": "ec2-1",
#         "id": "i-1234567890abcdef0",
#         "type": "t2.micro",
#         "state": "running",
#         "public_ip": "000000000000",
#         "private_ip": "172.31.45.67"
#     },
#     {
#         "name": "ec2-2",
#         "id": "i-1234567890abcdef1",
#         "type": "t2.micro",
#         "state": "running",
#         "public_ip": "000000000000",
#         "private_ip": "172.31.45.68"
#     }
# ]	 

# print(ec2_instances[1]["type"])
    

#Tasks is to get a pull request from a github using python
# we need a modules to talk to the Api of github

#step 1
# import requests module
# import requests
#step 2
# get the pull request github url
##step 3
# convert the response to a dictionary
#print the result 

# solution
# go the google and copy the url of the pull request
# install requests



# solution this will print at result with a status code to indicate if its worked
import requests
response =requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
print(response.status_code)


# solution this will print at result with a json

# import requests
# response =requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# print(response.json())

#Now I just want to print the names
import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
students = response.json()
for item in range(len(students)):
    print(students[item]["user"]["login"])
    

#sets
#It goest with data type of list but it is unique eg s3 bucket names 
#() turple
#{}set but uniqueor or dictionary
#[] list
#set is a collection of unique items
#eg
students = {"John", "Jane", "Jill", "Jack", "John"}