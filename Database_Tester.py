'''
	File: Databas_Tester.py
	Purpose: Test the functionality of teh methods in Database.py
	Author(s):  Julian, William
	Last Edit: 2/26/2022 
'''

import Database

def test(x):
    if (x == -1):
        print("Failed")
    else:
    	print("Passed")
        
''' One test for each collection type'''
    
def test_one_user():
	print("\nFirst Test of User Collection Methods for Database.py\n")
	db = Database.DatabaseImpl()
	#USERS------------------------
	#Creates an user
	print("Creating user with username: " + "Username" + " and password: " + "Password")
	test(db.createUser("Username", "Password"))
	print("Creating user with username: " + "User" + " and password: " + "Pass")
	test(db.createUser("User", "Pass"))
	#Creates an user, duplicate
	print("Attempting to create a duplicate user with username: Username")
	test(db.createUser("Username", "Username"))
	
	
	#Find user
	print("Getting the user data for Username: ")
	print(db.getUser("Username"))
	print("Attempting to get user data for a user that does not exist")
	#Find user, does not exist
	print(db.getUser("Password"))
	
	#Validate user
	print("Testing that username: Username  and password: Password are matched")
	test(db.validateUser("Username", "Password"))
	#Validate user, wrong password
	print("Testing that username: Username and username: Username are matched -shouldnt")
	test(db.validateUser("Username", "Username"))
	
	print("Testing validation for a user that does not exist")
	#Validate user, does not exist
	test(db.validateUser("Password", "Password"))
	#Deletes created users
	delete_entries = input("Would you like to delete the entries? (y/n) ")
	if delete_entries == "y" or delete_entries == "yes":
		print("Attempting to delete entry Username")
		test(db.removeUser("Username"))
		print("Attempting to delete entry User")
		test(db.removeUser("User"))
	print("Closing The Cluster/client")
	db.closeClient()
	print("\nTest One for Users Passed\n")
	
def test_one_hardware():
	#HARDWARE---------------------
	print("\nFirst Test of Hardware Collection Methods for Database.py\n")
	db = Database.DatabaseImpl()
	
	#Creates hardware
	print("Creating Hardware Set: HWSet")
	test(db.createHardwareSet("HWSet", 100))
	print("Creating Hardware Set: HSet2")
	test(db.createHardwareSet("HWSet2" , 50))
	print("Attempt to Create a copy - should fail")	
	#Creates hardware, duplicate
	test(db.createHardwareSet("HWSet", 300))
	
	#Gets hardware
	print("Printing the entry for HWSet")
	print(db.getHardwareSet("HWSet"))
	#Gets hardware, does not exist
	print("Attempting to print hardware entry that does not exist")
	print(db.getHardwareSet("User"))
	print("Attempting to look for a hardware set in the user database")
	print(db.getUser("HWSet")) #Checks to make sure it is not created in wrong db
	
	#Request hardware
	print("Attempting to request 50 from HWSet")
	test(db.requestHardware("HWSet", 50))
	#Request hardware, too many
	print("Attempting to request more than available for HWset and HWset2")
	test(db.requestHardware("HWSet", 100))
	test(db.requestHardware("HWSet2", 50))
	print("Attempting to request from hardware that does not exist")
	#Request hardware, does not exist
	test(db.requestHardware("Username", 1))
	
	#Return hardware
	print("Attempting to return hardware to hwset")
	test(db.returnHardware("HWSet", 99))
	#Return hardware, too many
	print("Attempting to return too much hardware too hwset2")
	test(db.returnHardware("HWSet2", 100))
	print("Attemppting to reutnr hardware to a set that does not exist")
	#Return hardware, does not exist
	test(db.returnHardware("Username", 1))
	
	
	#Deletes created Hardware Sets
	if input("Would you like to delete the hardware? (y/n) ") == "y":
		print("Deleting HWSet and HSet2")
		test(db.removeHardware("HWSet"))
		test(db.removeHardware("HWSet2"))
	print("Closing the client")
	db.closeClient()
	print("\nTest One for Hardware Passed\n")
	
def test_one_projects():
	#PROJECTS---------------------
	print("\nFirst Test of Projects Collection Methods for Database.py\n")
	db = Database.DatabaseImpl()
	print("Create Users: User and Username")
	#Creates project
	test(db.createUser("Username", "Password"))
	test(db.createUser("User", "Pass"))
	print("Create a project for Username")
	test(db.createProject("Username", "Description", 1))
	print("Try to create duplicate project - should fail")
	#Creates project, duplicate ID
	test(db.createProject("User", "Description", 1))
	print("Createa projoect with newlines in the description")
	#Creates project, new line in description
	test(db.createProject("Username", "Description\n\n\n\n\nDescription", -1))
	print("Creates a project id is a string instead of an int")
	#Creates project, id is a string vs int
	test(db.createProject("User", "Description", "3"))
	
	#Gets project
	print("Attempting to print the data fro project: 1")
	print(db.getProject(1))
	print("Attempting to print the data for project: str(3)")
	#Gets project, id is a string vs int
	print(db.getProject("3"))
	print("Attempting to print the data for non existent project")
	#Gets project, does not exist
	print(db.getProject("Username"))
	
	if input("Would you like to delete the projects/users? (y/n) ") == "y":
		print("Deleting the projects created")
		db.removeProject(1)
		db.removeProject("3")
		db.removeProject(-1)
		print("Deleting the users created")
		db.removeUser("User")
		db.removeUser("Username")
		
	print("Closing the Client")
	db.closeClient()
	print("\nTest One for Projects Passed\n")
	
def main():
	if input("Would you like to run test 1? (y/n) ") == "y":
		test_one_user()
	if input("Would you like to run test 2? (y/n) ") == "y":
		test_one_hardware()
	if input("Would you like to run test 3? (y/n) ") == "y":
		test_one_projects()
if __name__ == "__main__":
	main()	
	
