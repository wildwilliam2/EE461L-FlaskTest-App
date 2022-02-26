import Database

def test(x):
    if (x == -1):
        print("Failed!")
    

db = Database.DatabaseImpl()
#USERS------------------------
#Creates an user
test(db.createUser("Username", "Password"))
test(db.createUser("User", "Pass"))
#Creates an user, duplicate
test(db.createUser("Username", "Username"))
#Find user
print(db.findUser("Username"))
#Find user, does not exist
print(db.findUser("Password"))
#Validate user
test(db.validateUser("Username", "Password"))
#Validate user, wrong password
test(db.validateUser("Username", "Username"))
#Validate user, does not exist
test(db.validateUser("Password", "Password"))
#Deletes created users
#test(db.deleteUser("Username"))
#test(db.deleteUser("User"))
#HARDWARE---------------------
#Creates hardware
test(db.createHardwareSet(100, "HWSet"))
test(db.createHardwareSet(50, "HWSet2"))
#Creates hardware, duplicate
test(db.createHardwareSet(300, "HWSet"))
#Gets hardware
print(db.getHardwareSet("HWSet"))
#Gets hardware, does not exist
print(db.getHardwareSet("User"))
print(db.findUser("HWSet")) #Checks to make sure it is not created in wrong db
#Request hardware
test(db.requestHardware("HWSet", 50))
#Request hardware, too many
test(db.requestHardware("HWSet", 100))
test(db.requestHardware("HWSet2", 50))
#Request hardware, does not exist
test(db.requestHardware("Username", 1))
#Return hardware
test(db.returnHardware("HWSet", 100))
#Return hardware, too many
test(db.returnHardware("HWSet2", 100))
#Return hardware, does not exist
test(db.returnHardware("Username", 1))
#Deletes created Hardware Sets
#test(db.deleteHardwareSet("HWSet"))
#test(db.deleteHardwareSet("HWSet2"))

#PROJECTS---------------------
#Creates project
db.createUser("Username", "Password")
db.createUser("User", "Pass")
test(db.createProject("Username", "Description", 1))
#Creates project, duplicate ID
test(db.createProject("User", "Description", 1))
#Creates project, new line in description
test(db.createProject("Username", "Description\n\n\n\n\nDescription", -1))
#Creates project, id is a string vs int
test(db.createProject("User", "Description", "3"))
#Gets project
print(db.getProject(1))
#Gets project, id is a string vs int
print(db.getProject("3"))
#Gets project, does not exist
print(db.getProject("Username"))