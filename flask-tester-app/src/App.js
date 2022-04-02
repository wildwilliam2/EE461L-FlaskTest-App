/*
  File: App.js
  Purpose: This application is meant to test the flask applications functionality
  Author: William Wooten
  Json protocol config: David
*/


import './App.css';
import React from 'react';
import {useState, useEffect, useRef} from 'react';
let localhost = "http://127.0.0.1:5000/";
/* for testing entries for login credentials, and deletions of credentials*/
function AddUsers()
{
  // Holds the entered username
  const usernamefield = useRef();
  const passwordfield = useRef();
  const [serverResponse, setServerResponse] = useState("Nothing entered yet");

  // Sends the credentials to the flask backend
  async function sendCredentials()
  {
    let username = usernamefield.current.value;
    let password = passwordfield.current.value;
    let credentials = username + "-" + password;
    // print to the console
    console.log("The entered username: " + username);
    console.log("The eneterd password: " + password);
    // Use fetch protocol to send the data to the backend
    let dict = {
      method : "POST",
      body : JSON.stringify({
        userid: username,
        password: password
      })
    };
    let res = await fetch("/createuser" , dict);
    let responseJson = await res.json();
    
    if(responseJson['errorcode'] == 0)
    {
      setServerResponse("Added User!");
    }
    else{
      setServerResponse("Did not add new user.");
    }
  }
  return(
  <>
    <h2>Add new users</h2>
    <div>
        <h3>Enter a username and password</h3>
        <div>
          <input ref = {usernamefield} type = "text" placeholder = "Enter a username" size = "21"></input>
        </div>
        <div>
          <input ref = {passwordfield} type = "text" placeholder = "Enter a password" size = "21"></input>
        </div>
        <div>
          <button onClick = {() => sendCredentials()}>Enter</button>
         <label>{serverResponse}</label>
        </div>
    </div>
    <div>
    </div>
  </>);
}

/*For testing the removal of users from the database*/
function RemoveUsers()
{
  const [serverResponse, setServerResponse] = useState("Nothing Entered Yet");
  const usernamefield = useRef();
  async function sendCredentials()
  {
    let username = usernamefield.current.value;
    console.log("The entered username for removal: " + username);
        // Use fetch protocol to send the data to the backend
    let dict = {
      method : "POST",
      body : JSON.stringify({
        userid: username
      })
    };
    let res = await fetch("/removeuser" , dict);
    let responseJson = await res.json();
    
    if(responseJson['errorcode'] == 0)
    {
      setServerResponse("User removed!");
    }
    else{
      setServerResponse("There was a problem in removing.");
    }
  }
  return(
    <>
      <h2>Remove an existing user</h2>
      <h3>Enter the username  of the user to remove</h3>
      <div>
        <input ref = {usernamefield} type = "text" placeholder = "Enter the username"></input>
      </div>
      <button onClick = {sendCredentials}>Enter</button>
      <label>{serverResponse}</label>
    </>
  );
}
/* Ensures that user information is correct */
function ValidateUsers()
{
  const [serverResponse, setServerResponse] = useState("No Response yet");
  const usernamefield = useRef();
  const passwordfield = useRef();
  async function sendCredentials()
  {
    let username = usernamefield.current.value;
    let password = passwordfield.current.value;
    console.log("The entered username: " + username);
    console.log("The eneterd password: " + password);

    // Fetch protocol
    let dict = {
      method : "POST",
      body : JSON.stringify({
        userid: username,
        password: password
      })
    };
    let res = await fetch("/verifyuser" , dict);
    let responseJson = await res.json();
    if(responseJson['valid'])
    {
      setServerResponse("User was verified!");
    }
    else{
      setServerResponse("User was not verified!");
    }
  }

  return(
    <>
      <h2> Validate a username and password combination</h2>
      <div>
          <h3>Enter a username and password pair to validate</h3>
          <input ref = {usernamefield} type = "text" placeholder = "Enter a username" size = "21"></input>
        </div>
        <div>
          <input ref = {passwordfield} type = "text" placeholder = "Enter a password" size = "21"></input>
        </div>
        <div>
          <button onClick = {() => sendCredentials()}>Enter</button>
         <label>{serverResponse}</label>
      </div>
      
    </>
  );
}

/* Adds hardware sets to the database*/
function AddHW()
{
  const [serverResponse, setServerResponse] = useState("No Response yet");
  const namefield = useRef();
  const qfield = useRef();
  
  async function sendCredentials()
  {
    let name = namefield.current.value;
    let q = qfield.current.value;
    console.log("Entered name: " + name);
    console.log("Enter q: " + q);
       // Fetch protocol
       let dict = {
        method : "POST",
        body : JSON.stringify({
          name: name,
          capacity:  q
        })
      };
      let res = await fetch("/createHWSet" , dict);
      let responseJson = await res.json();
      if(responseJson['errorcode'] == 0)
      {
        setServerResponse("Hardware set added!");
      }
      else{
        setServerResponse("Set not added!");
      }
  }

  return(
    <>
      <h2>Add a hardware set</h2>
      <div>
          <h3>Enter a name and quantity</h3>
          <input ref = {namefield} type = "text" placeholder = "Enter a set name" size = "21"></input>
        </div>
        <div>
          <input ref = {qfield} type = "text" placeholder = "Enter an amount" size = "21"></input>
        </div>
        <div>
          <button onClick = {() => sendCredentials()}>Enter</button>
         <label>{serverResponse}</label>
      </div>
      
    </>
  );
}

/* Removes a hardware set form the database*/
function RemoveHW()
{
  const [serverResponse, setServerResponse] = useState("No Response yet");
  const namefield = useRef();
  
  async function sendCredentials()
  {
    let name = namefield.current.value;
    console.log("Entered name: " + name);
       // Fetch protocol
       let dict = {
        method : "POST",
        body : JSON.stringify({
          name: name
        })
      };
      let res = await fetch("/removeHWSet" , dict);
      let responseJson = await res.json();
      if(responseJson['errorcode'] == 0)
      {
        setServerResponse("Hardware set removed!");
      }
      else{
        setServerResponse("There was an error!");
      }
  }

  return(
    <>
      <h2>Remove a hardware set</h2>
      <div>
          <h3>Enter a name</h3>
          <input ref = {namefield} type = "text" placeholder = "Enter a set name" size = "21"></input>
        </div>
        <div>
          <button onClick = {() => sendCredentials()}>Enter</button>
         <label>{serverResponse}</label>
      </div>
      
    </>
  );
}
/*Request Resources from a hardware set*/
function RequestResources()
{
  const [serverResponse, setServerResponse] = useState("No Response yet");
  const namefield = useRef();
  const qfield = useRef();
  
  async function sendCredentials()
  {
    let amount = qfield.current.value;
    let name = namefield.current.value;
    console.log("Name of the hardware set: " + name);
    console.log("Amount requested: " + amount);

    // Fetch protocol
    let dict = {
      method : "POST",
      body : JSON.stringify({
        name: name,
        request: amount
      })
    };
    let res = await fetch("/requestResources" , dict);
    let responseJson = await res.json();

    if(responseJson["errorcode"] == 0)
    {
      setServerResponse("Request filled, or filled to best ability! (Or no errors)");
    }
    else{
      setServerResponse("Unable to fill request, or there was an error");
    }

  }

  return(
    <>
      <h2>Request Resources from a hardware set</h2>
      <div>
          <h3>Enter a name and quantity</h3>
          <input ref = {namefield} type = "text" placeholder = "Enter a set name" size = "21"></input>
        </div>
        <div>
          <input ref = {qfield} type = "text" placeholder = "Enter an amount" size = "21"></input>
        </div>
        <div>
          <button onClick = {() => sendCredentials()}>Enter</button>
         <label>{serverResponse}</label>
      </div>
      
    </>
  );
}
/* Returns resources to a hardware set*/
function ReturnResources()
{
  const [serverResponse, setServerResponse] = useState("No Response yet");
  const namefield = useRef();
  const qfield = useRef();
  
  async function sendCredentials()
  {
    let amount = qfield.current.value;
    let name = namefield.current.value;
    console.log("Name of the hardware set: " + name);
    console.log("Amount requested: " + amount);

    // Fetch protocol
    let dict = {
      method : "POST",
      body : JSON.stringify({
        name: name,
        return: amount
      })
    };
    let res = await fetch("/returnResources" , dict);
    let responseJson = await res.json();

    if(responseJson["errorcode"] == 0)
    {
      setServerResponse("Return filled, or filled to best ability! (Or no errors)");
    }
    else{
      setServerResponse("Unable to fill return, or there was an error");
    }

  }

  return(
    <>
      <h2>Return Resources to a hardware set</h2>
      <div>
          <h3>Enter a name and quantity</h3>
          <input ref = {namefield} type = "text" placeholder = "Enter a set name" size = "21"></input>
        </div>
        <div>
          <input ref = {qfield} type = "text" placeholder = "Enter an amount" size = "21"></input>
        </div>
        <div>
          <button onClick = {() => sendCredentials()}>Enter</button>
         <label>{serverResponse}</label>
      </div>
      
    </>
  );
}
/* When Prompted Displays the names of all of the sets in the database */
function SetNames()
{
  const [serverResponse, setServerResponse] = useState("No Sets Displayed Yet");
  
  async function getSets()
  {

  }
  return(
    <>
      <h2>Display all known Hardware Set Names</h2>
      <div>
        <button>Print</button>
        <label>{serverResponse}</label>
      </div>

    </>
  );
}


/*Creates a project*/
function CreateProject()
{
  const [serverResponse, setServerResponse] = useState("No Response Yet");
  const namefield = useRef();
  const descriptionfield = useRef();
  const idfield = useRef();

  async function sendCredentials()
  {
    let name = namefield.current.value; 
    let des = descriptionfield.current.value;
    let id  = idfield.current.value;
    console.log("The name entered: "+  name);
    console.log("The description entered: " + des);
    console.log("The project id entered: " + id);

    let dict = {
      method : "POST",
      body : JSON.stringify({
        name: name,
        description: des,
        projectid: id
      })
    };
    let res = await fetch("/createProject" , dict);
    let responseJson = await res.json();

    if(responseJson["errorcode"] == 0)
    {
      setServerResponse("Project Created Successfully!");
    }
    else{
      setServerResponse("Project not created!");
    }
  }
  
  return(
    <>
      <h2>Create a new Project</h2>
      <div>
          <h3>Enter a name and quantity</h3>
          <input ref = {namefield} type = "text" placeholder = "Enter a name" size = "21"></input>
        </div>
        <div>
          <input ref = {descriptionfield} type = "text" placeholder = "Enter a description" size = "21"></input>
        </div>
        <div>
          <input ref = {idfield} type = "text" placeholder = "Enter a projectid" size = "21"></input>
        </div>
        <div>
          <button onClick = {() => sendCredentials()}>Enter</button>
         <label>{serverResponse}</label>
      </div>
      
    </>
  );
}
/* Removes a project from the database with the given project id*/
function RemoveProject()
{
  const [serverResponse, setServerResponse] = useState("No Response Yet");
  const namefield = useRef();
  async function sendCredentials()
  {
    let id = namefield.current.value;
    console.log("The name of the project to be removed: " + id);
    let dict = {
      method : "POST",
      body : JSON.stringify({
        id : id
      })
    };
    let res = await fetch("/removeProject" , dict);
    let responseJson = await res.json();

    if(responseJson["errorcode"] == 0)
    {
      setServerResponse("Project Removed Successfully!");
    }
    else{
      setServerResponse("Project not removed!");
    }
  }
  return(
    <>
      <h2>Remove a Project</h2>
      <div>
          <h3>Enter the project id of the project to be removed</h3>
          <input ref = {namefield} type = "text" placeholder = "Enter a project id" size = "21"></input>
        </div>
        <div>
          <button onClick = {() => sendCredentials()}>Enter</button>
         <label>{serverResponse}</label>
      </div>
      
    </>
  );
}


/* Gets the data associated with a given project*/
function GetProject()
{
  const [serverResponse, setServerResponse] = useState("No Response Yet");
  const namefield = useRef();
  async function sendCredentials()
  {
    let id = namefield.current.value;
    console.log("The id of the projec to get is : " + id);
    let dict = {
      method : "POST",
      body : JSON.stringify({
        id : id
      })
    };
    let res = await fetch("/getProject" , dict);
    let responseJson = await res.json();

    let name = responseJson['name'];
    let projectid = responseJson["projectid"];
    let des = responseJson["description"];
    setServerResponse("The name: " + name + " The project id: " + projectid + " THe description: " + des);
  }
  return(
    <>
      <h2>Get the data of the project</h2>
      <div>
          <h3>Enter the project id</h3>
          <input ref = {namefield} type = "text" placeholder = "Enter a project id" size = "21"></input>
        </div>
        <div>
          <button onClick = {() => sendCredentials()}>Enter</button>
         <label>{serverResponse}</label>
      </div>
    </>
  );
}
function App() {
  return (
    <>
      <h1>This app is for testing the functions in the Flask application: app.py</h1>
      <AddUsers/>
      <RemoveUsers/>
      <ValidateUsers/>
      <AddHW/>
      <RequestResources/>
      <ReturnResources/>
      <RemoveHW/>
      <CreateProject/>
      <RemoveProject/>
    </>
  );
}

export default App;
