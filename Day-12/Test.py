#files operations
#read operations
#write operations

# in this case you will use inbuilt functions
#open()
#If you inetnd of reading a file you need this r stands for read and w stands for write

#Tasks is to write a python files to update a server configuration
#step 1 read the file store
# step 2 store in a variable
#step 3 write mode
#step 4 updating just what is needed Maximum connections using if condition since its just a line

# solution
def updata_server_config(file_path, key, value):
	with open(file_path, 'r') as file:
		lines = file.readlines()

	with open(file_path, 'w') as file:
		for line in lines:
			if key in line:
				file.write(key + "=" + value + "\n")
			else:
				file.write(line)
	

updata_server_config("server.conf", "MAX_CONNECTIONS", "400")

