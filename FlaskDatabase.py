import Database
from flask import Flask, jsonify, redirect, url_for, request, render_template
import os
import json


app = Flask(__name__, static_folder='./project/build/', static_url_path='/')
db = Database.DatabaseImpl()
#verifies that the username and password are valid, retrieved from the request form. If successful returns 0.
@app.route("/"):
    def index():
        return app.send_static_file('index.html')
@app.errorhandler(404)
def not_found(e):
        return app.send_static_file('index.html')
@app.route("/verifyuser", methods = ["POST"])
    def verifyuser():
            myrequest = request.get_json(force=True)
            username = myrequest['userid']
            password = myrequest['password']
            if(db.validateUser(username, password) == 0)
                return {'valid' : true}
            else
                return {'valid' : false}
#creates a user with the userid and password given in the request form. If successful returns 0.
@app.route("/createuser", methods = ["POST"])
    def createuser():
        myrequest = request.get_json(force=True)
        username = myrequest['userid']
        password = myrequest['password']
        
        verify = db.createUser(username, password)
        
        return {'errorcode': verify}
#creates a hardware set with the name and capacity given in the request form. If successful returns 0. 
@app.route("/createHWSet", methods = ["POST"])
    def createhwset():
        myrequest = request.get_json(force=True)
        name = myrequest['name']
        capacity = myrequest['capacity']
        verify = db.createHardwareSet(name, capacity)
        
        return {'errorcode': verify}
#requests resources from the hardware sets, taking a certain number from the hardware set named in the request form. If successful returns 0.
@app.route("/requestResources", methods = ["POST"])
    def requestresource():
        myrequest = request.get_json(force=True)
        name = myrequest['name']
        resourcesToTake = myrequest['request']
        verify = db.requestHardware(name, resourcesToTake)
        return {'errorcode': verify}
        
#return resources to hardware sets in the same way.    
@app.route("/returnResources", methods = ["POST"])
    def returnresource():
        myrequest = request.get_json(force=True)
        name = myrequest['name']
        resourcesToReturn = myrequest['return']
        verify = db.returnHardware(name, resourcesToReturn)
        return {'errorcode': verify}
#at this URL, flask will pass a list containing dictionaries with all current hardware sets names, availability, and capacity. This url can therefore be used to have a 
#dynamically updating page with the hardware on it. This list is jsonified when returned.
@app.route("/hardwarelist", methods = ["GET"])
    def hardware():
        return json.dumps(db.hardwareSetList())
    
    
#returns a specific hardware set as jsonified, with an input being its name.    
@app.route("/getHardwareSet", methods = ["POST"])
def gethardwareset():
    myrequest = request.get_json(force=True)
    name = myrequest['name']
    hardwareSet = db.getHardwareSet(name)
    return jsonify(hardwareSet)

    
#this method allows the client to create a project. It takes a name, description, and projectid from the form, and creates the project in the database. If successful returns 0.
@app.route("/createProject", methods = ["POST"])
def createproject():
        myrequest = request.get_json(force=True)
        name = myrequest['name']
        description = myrequest['description']
        projectid = myrequest['projectid']
        
        verify = db.createProject(name, description, projectid)
        return {'errorcode' : verify}
    
#returns a specific project as jsonified, with an input being its name.
@app.route('/getProject', methods = ["POST"])
def getproject():
    myrequest = request.get_json(force=True)
    name = myrequest['name']
    project = db.getProject(name)
    return jsonify(project)

#at this URL, flask will pass a list containing dictionaries with all current projects,
#names, availability, and capacity. This url can therefore be used to have a dynamically updating page with the hardware on it. This list is jsonified when returned.
@app.route("/projectlist", methods = ["GET"])
def getprojectlist():
        return json.dumps(db.projectList())

#this method closes the database. It could be ideally implemented with a button that closes the user session gracefully.
@app.route("/close")
def closeclient():
    db.closeClient()
    return 

if __name__ == "__main__":
    app.run(host='0.0.0.0
           , debug = False, port=os.environ.get('PORT', 80))

