#Task = List of files in list of folders that users provide
#step 1 = Read inpuy from the user
#step 2 = for loop on every folder = list of files in each folder
#step 3 = identtify the modules
#step 4 = print the files
#step 5 = error handling


# import os
# folders = input("Enter a list of folder names with spaces in between: ").split()
# for folder in folders:
# 	files =os.listdir(folder)
# 	print("listing files in " + folder)
    
# for file in files:
#         print(file)
        


#exceptional handling means instead of terminating the program, 
# we can handle the error and provide a user-friendly message



import os
folders = input("Enter a list of folder names with spaces in between: ").split()
for folder in folders:
	try:
		files =os.listdir(folder)
		print("listing files in " + folder)
		for file in files:
			print(file)
	except FileNotFoundError:
		break
		print("Sorry, " + folder + " does not exist")
	except PermissionError:
		break
		print("Sorry, you do not have permissions to access " + folder)