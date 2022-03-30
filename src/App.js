import React from "react";
import {Routes, Route, Link} from "react-router-dom";
import './App.css'
import Hardware from "./hardware";
import Project from "./project";
import LoginPortal from "./LoginPortal";

export default function App() {
     return (
              <div className = "App">
                  <Routes>
                     <Route path = "/" element = {<Home />} />
                     <Route path = "LoginPortal" element = {<LoginPortal/>} />
                     <Route path = "Hardware" element ={<Hardware />} />
                     <Route path = "Project" element = {<Project/>} />
                  </Routes>
               </div>

          );
}

function Home() {
   return (
      <>
      <main>   
         <h2>Home</h2>
      </main>
      <nav>
         <li>
            <Link to = "/hardware"> Hardware </Link>
         </li>
         <li>
            <Link to = "/project"> Projects </Link>
         </li>
         <li>
            <Link to ="/login"> LoginPortal </Link>
         </li>
      </nav>
      </>
   );
}





