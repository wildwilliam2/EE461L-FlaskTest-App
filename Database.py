from pymongo import MongoClient
import Encryptor

class DatabaseImpl:
    
    def __init__(self):
        client = MongoClient("mongodb+srv://avengineers461L:MwycDXNBxKObOc3I@cluster0.s12ua.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        
        self.__db = client.Project461L
        passMe = "LGowXavJ2MZhq50RhqVD"
        
        self.__encryptor = Encryptor.Encryption(151, -1) 
        
    #user methods, including encryption    
    
    def createUser(self, userid, password):
        encryptedPassword = self.__encryptor.encrypt(password)
        encryptedUserID = self.__encryptor.encrypt(userid)
        if(self.__db.UserCollection.find_one({"userid":encryptedUserID}) != None):
            print("Error: Nonunique user id.")
            return -1
        userDoc = {
                "userid" : encryptedUserID,
                "encryptedPassword" : encryptedPassword
        }
                                            
        self.__db.UserCollection.insert_one(userDoc)
        if(self.__db.UserCollection.find_one({"userid":userid}) != None):
               return 0
        else:
            print("Error: user was not successfully put in the database.")
            return -1
           
    def findUser(self, userid):
        encryptedUserID = self.__encryptor.encrypt(userid)
        query = self__db.UserCollection.find_one({"userid":encryptedUserID})
        if query != None:
            return query
        else:
            print("Error: a user with this id was not found in the database.")
  
    def validateUser(self, userid, passwordToCheck):
        encryptedUserID = self.__encryptor.encrypt(userid)
           
        if(self.__db.UserCollection.find_one({"userid":encryptedUserID}) == None):
            return -1
        truePassword = self.__encryptor.decrypt(encryptedPassword)
        foundUser = self.__db.UserCollection.find_one({"userid":encryptedUserID})
        encryptedPassword = foundUser["encryptedPassword"]
            
        encodedToCheck = passwordToCheck.encode('ascii')
        if(truePassword != encodedToCheck):
            return -1
        else: 
            return 0
           
     #hardware methods      
    def createHardwareSet(self, capacity, name):
        if(self.__db.HardwareCollection.find_one({"name":name}) != None):
            print("Error: Nonunique hardware set name.")
            return -1
           
        hardwareDoc = {
                      "capacity" : capacity,
                      "availability" : capacity,
                      "name" : name
                         }
           
        self.__db.HardwareCollection.insert_one(hardwareDoc)
        if(self.__db.HardwardCollection.find_one({"name":name}) != None):
            return 0
        else:
            print("Error: user was not successfully put in the database.")
            return -1
           
           
    def getHardwareSet(self, name):
        query = self__db.HardwareCollection.find_one({"name":name})
        if query != None:
               return query
        else:
               print("Error: a hardware set with this name was not found in the database.")
    
    def requestHardware(self, name, qty):
        hardware = self.getHardwareSet(name)
        if(qty <0):
            print("Invalid. Checkout quantity must be a nonnegative number.")
            return -1
        else:
            if(qty <= hardware["availability"]):
                values = {"$set": {"availability" : availability-qty} }
                self.__db.HardwareCollection.update_one( {"name" : name}, values)
                return 0
            else:
                values = {"$set": {"availability" : 0}}
                self.__db.HardwareCollection.update_one( {"name" : name}, values)
                return 0
           
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
     
        #project methods
    def createProject(self, name, description, projectid):
        if(self.__db.ProjectCollection.find_one({"projectid":projectid}) != None):
                print("Error: Nonunique Project ID.")
                return -1
        projectDoc = {
                   "name":name,
                   "description":description,
                   "projectid":projectid
           }
        self.__db.ProjectCollection.insert_one(projectDoc)
        if(self.__db.HardwardCollection.find_one({"projectid":projectid}) != None):
            return 0
        else:
            print("Error: project was not successfully put in the database.")
            return -1
              
    def getProject(self, projectid):
        if(self.__db.ProjectCollection.find_one({"projectid":projectid}) != None):
            query = self.__db.ProjectCollection.find_one({"projectid":projectid})
            return query
         
        
        