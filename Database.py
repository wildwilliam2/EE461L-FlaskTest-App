from pymongo import MongoClient
import Encryptor

class DatabaseImpl:
    '''Initializes the database object'''
    
    def __init__(self):
        # Used to access the mongodb Cluster
        client = MongoClient("mongodb+srv://avengineers461L:MwycDXNBxKObOc3I@cluster0.s12ua.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.myClient = client
        # The singular database that will hold the collections used in the application
        self.__db = client.Project461L
        passMe = "LGowXavJ2MZhq50RhqVD"
        # An encryptor for encrypting the transactions between this program and the user information collection
        self.__encryptor = Encryptor.Encryption(151, -1) 
        
        
    '''User Methods: Transactions Encrypted'''
    
    # Input: userid, password
    # Output: code signalling sucess or failure
    # Purpose: Place a new user in the user collection
    def createUser(self, userid, password):
        # Encrypt the arguments
        encryptedPassword = self.__encryptor.encrypt(password)
        encryptedUserID = self.__encryptor.encrypt(userid)
        
        # Check if there is a user with the id given in the database
        if(self.__db.UserCollection.find_one({"userid":encryptedUserID}) != None):
            print("Error: Nonunique user id.")
            return -1
        # Create the new user post/document
        userDoc = {
                "userid" : encryptedUserID,
                "encryptedPassword" : encryptedPassword
        }
        
        # Insert the new user post/document into the database                                
        self.__db.UserCollection.insert_one(userDoc)
        
        #If the post was sucessfully inserted, then return with no errors
        if(self.__db.UserCollection.find_one({"userid":userid}) != None):
               return 0
        else:
            #Otherwise signify there was an error
            print("Error: user was not successfully put in the database.")
            return -1
        
    # Input: userid
    # Output: the query associated with the userid, or none if none exists
    # Purpose: Get user information
    def getUser(self, userid):
    	
        encryptedUserID = self.__encryptor.encrypt(userid)
        # Returns a dictionary associated with the encrypted userid if one exists
        query = self__db.UserCollection.find_one({"userid":encryptedUserID})
        if query != None:
            return query
        else:
            # Return Nothing if no user found
            print("Error: a user with this id was not found in the database.")
            return None
            
    # Input: userid, a password to check
    # Output: Singal telling wheter or not user was valid
    # Purpose: Determines 
    def validateUser(self, userid, passwordToCheck):
        #Encrypt the user id
        encryptedUserID = self.__encryptor.encrypt(userid)
        
        # if their is no user with the encrypted id specified, return failed signal
        if(self.__db.UserCollection.find_one({"userid":encryptedUserID}) == None):
            return -1
        
        # Retrieve the *true* password associated with the userid
        foundUser = self.__db.UserCollection.find_one({"userid":encryptedUserID})
        encryptedPassword = foundUser["encryptedPassword"]
        truePassword = self.__encryptor.decrypt(encryptedPassword)
        
        # Check if the password matches the one in the database
        if(truePassword != passwordToCheck):
            return -1
        else: 
            return 0
            
    # Input: userid
    # Output: Signal telling Success/failure ( initially not necessary)
    # Purpose: Remove a user document/post from UserCollection
    def removeUser(self, userid):
        # Deletes the document if there is one, does nothing otherwise
        self.__db.UserCollection.delete_one({"name" : name})
        return 0       
        
    '''Hardware methods'''
    # Input:   name, capacity
    # Output:  Singal telling whether or not hardware post was successful
    # Purpose: Create a hardwareset entry in the hardware collection
    def createHardwareSet(self, name, capacity):
        # If the hardware set witht this name already exists, return a failure signal
        if(self.__db.HardwareCollection.find_one({"name":name}) != None):
            print("Error: Nonunique hardware set name.")
            return -1
            
        # Create new hardware post/document 
        hardwareDoc = {
                      "capacity" : capacity,
                      "availability" : capacity,
                      "name" : name
                         }
        # Insert ethe new hardware post/document into the Hardware Collection
        self.__db.HardwareCollection.insert_one(hardwareDoc)
        # If the insertion was successul return a sucess signal, otherwise a failure signal
        if(self.__db.HardwardCollection.find_one({"name":name}) != None):
            return 0
        else:
            print("Error: user was not successfully put in the database.")
            return -1
           
    # Input: name
    # Output: Hardware Collection entry associated with 'name' or None if it does not exist
    # Purpose: Retreival of hardwareset data
    def getHardwareSet(self, name):
        query = self__db.HardwareCollection.find_one({"name":name})
        # If there is an entry in the hardware collection with the specified name return it, otherwise return none
        if query != None:
               return query
        else:
               print("Error: a hardware set with this name was not found in the database.")
               return None
    # Input: name - name of the hardwarset, qty - amount being requested 
    # Output: signal telling the sucess or failure of the operation
    # Purpose: Check out the specified quantity from the hardware set specified by name
    def requestHardware(self, name, qty):
        hardware = self.getHardwareSet(name)
        # If there is no hardware set, signal failure
        if hardware == None:
        	return -1
        #  If the user is asking for less than zero, return failure
        if(qty <0):
            print("Invalid. Checkout quantity must be a nonnegative number.")
            return -1
        else:
            # If there is enough availability to service the request, subtract that amount, return success
            if(qty <= hardware["availability"]):
                values = {"$set": {"availability" : availability-qty} }
                self.__db.HardwareCollection.update_one( {"name" : name}, values)
                return 0
            else:
            # Otherwise, there is not, checkout whatever is left by setting avail to 0, return success
                values = {"$set": {"availability" : 0}}
                self.__db.HardwareCollection.update_one( {"name" : name}, values)
                return 0
                
    # Input: name - name of the hardwarset, qty - amount being requested 
    # Output: signal telling the sucess or failure of the operation
    # Purpose: Check in the specified quantity from the hardware set specified by name     
    def returnHardware(self, name, qty):
        hardware = self.getHardwareSet(name)
        if(qty<0):
                print("Invalid. check-in quantity must be a nonnegative number.")
                return -1
        else:
            if(qty <= hardware["capacity"] - hardware["availability"]):
                values = {"$set": {"availability" : availability+qty}}
                self.__db.HardwareCollection.update_one({"name" : name}, values)
                return 0
            else:
                values = {"$set": {"availability" : hardware["capacity"]}}
                self.__db.HardwareCollection.update_one({"name" : name}, values)
                return 0
                
    # Input: name
    # Output: Signal telling Success/failure ( initially not necessary)
    # Purpose: Remove a hardwareset document/post from HardwareCollection
    def removeHardware(self, name):
        # Deletes the document if there is one, does nothing otherwise
        self.__db.HardwareCollection.delete_one({"name" : name})
        return 0
        
            
    '''Project Methods'''
    # Input: name - name of the project, description- a string, projectid -  number to identify the project
    # Output: Singal telling whether the insertion was a success or failure
    # Purpose: Inserts a new project/post into the ProjectCollection
    def createProject(self, name, description, projectid):
        # If there already is a project with this project id, return a failure signal
        if(self.__db.ProjectCollection.find_one({"projectid":projectid}) != None):
                print("Error: Nonunique Project ID.")
                return -1
        # Otherwise, Create a new project document/post
        projectDoc = {
                   "name":name,
                   "description":description,
                   "projectid":projectid
           }
        # Insert the project document/post
        self.__db.ProjectCollection.insert_one(projectDoc)
        # If successfully added, return a sucess signal; otherwise failure signal
        if(self.__db.ProjectCollection.find_one({"projectid":projectid}) != None):
            return 0
        else:
            print("Error: project was not successfully put in the database.")
            return -1
           
    # Input: projectid
    # Output: project document associated with the projectid, None if there is not one
    # Purpose: Getting project documentation/data
    def getProject(self, projectid):
        if(self.__db.ProjectCollection.find_one({"projectid":projectid}) != None):
            query = self.__db.ProjectCollection.find_one({"projectid":projectid})
            return query
        else:
            return None
            
    # Input: projectid - id of the project 
    # Output: Signal telling Success/failure ( initially not necessary)
    # Purpose: Remove a project document/post from ProjectCollection
    def removeProject(self, projectid):
        # Deletes the document if there is one, does nothing otherwise
        self.__db.ProjectCollection.delete_one({"projectid" : projectid})
        return 0
        
        
    '''Other Methods'''	
    # Input: None
    # Output: None
    # Purpose: Close the cluster/connection to mongodb
    def closeClient(self):
        self.myClient.close()
       
       
       
         
        
        
