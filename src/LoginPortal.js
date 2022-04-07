import React, { useState } from 'react';
import LoginForm from './components/LoginForm';

function LoginPortal() {

const adminUser = {
  email: "admin@admin.com",
  password: "admin123"
}

const [user, setUser] = useState({name: "", email: ""});
const [error, setError] = useState("");
const [serverResponse, setServerResponse] = useState("No Response yet");

  async function sendCredentials(details){
      let username = details.username;
      let password = details.password;
      let email = details.email;

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
     console.log(responseJson);

     if(responseJson['valid']){
       console.log("Logged in")
       setUser({
         name: details.name,
         email: details.email
       });
       setServerResponse("User was verified");
     }else{
       console.log("Details do not match")
       setError("Details do not match")
       setServerResponse("User was not verified");
     }
  }  
const Login = details => {
  console.log(details);
   sendCredentials(details);
}

const Logout = () => {
  setUser({name: "", email: ""});
}



  return (
    <div className="LoginPortal">
     {(user.email != "") ? (
       <div className="welcome">
         <h2>Welcome, <span>{user.name}</span></h2>
         <button onClick={Logout}>Logout</button>
         </div>
     ) : ( 
       <LoginForm Login={Login} error={error}/>
     )}
    </div>
  );
}
export default LoginPortal;

