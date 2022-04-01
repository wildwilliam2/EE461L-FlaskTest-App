import Database
from flask import Flask, jsonify, redirect, url_for, request, render_template
import os


app = Flask(__name__)
db = Database.DatabaseImpl()
#verifies that the username and password are valid, retrieved from the request form. If successful returns 0.
@app.route("/verifyuser", methods = ["POST"])
def verifyuser():
    username = request.form['userid']
    password = request.form['password']
    if(db.validateUser(username, password) == 0):
        return true
    else:
        return false
#creates a user with the userid and password given in the request form. If successful returns 0.
@app.route("/createuser", methods = ["POST"])
def createuser():
    username = request.form['userid']
    password = request.form['password']

    verify = db.createUser(username, password)

    return verify
#creates a hardware set with the name and capacity given in the request form. If successful returns 0. 
@app.route("/createHWSet", methods = ["POST"])
def createhwset():
    name = request.form['name']
    capacity = request.form['capacity']
    verify = db.createHardwareSet(name, capacity)
    
    return verify

#requests resources from the hardware sets, taking a certain number from the hardware set named in the request form. If successful returns 0.
@app.route("/requestResources", methods = ["POST"])
def requestresource():
    name = request.form['name']
    resourcesToTake = request.form['request']
    verify = db.requestHardware(name, resourcesToTake)
    return verify

#at this URL, flask will pass a list containing dictionaries with all current hardware sets names, availability, and capacity. This url can therefore be used to have a 
#dynamically updating page with the hardware on it. This list is jsonified when returned.
@app.route("/hardware", methods = ["GET"])
def hardware():
    return jsonify(result = db.hardwareSetList())

    
#this method allows the client to create a project. It takes a name, description, and projectid from the form, and creates the project in the database. If successful returns 0.
@app.route("/createProject", methods = ["POST"])
def createProject():        
        name = request.form['name']
        description = request.form['description']
        projectid = request.form['projectid']
        
        verify = db.createProject(name, description, projectid)
        return verify

#at this URL, flask will pass a list containing dictionaries with all current projects,
#names, availability, and capacity. This url can therefore be used to have a dynamically updating page with the hardware on it. This list is jsonified when returned.
@app.route("/projects", methods = ["GET"])
def getProjects():
    return jsonify(result = db.projectList())

#this method closes the database. It could be ideally implemented with a button that closes the user session gracefully.
@app.route("/close")
def close():
    db.closeClient()
    return 0

if __name__ == "__main__":
    app.run()

