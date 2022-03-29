import React from "react";
import {Link} from "react-router-dom";
import ConstructionIcon from '@mui/icons-material/Construction';

function Project() {
   return (
      <div>
         <h1> Projects </h1>
         <p> This is the project page </p>
         <ConstructionIcon sx={{ fontSize: 50 }}/>
         <p className="underConstruction" >
         This page is under construction...
         </p>
         <nav>
            <li>
               <Link to ="/"> Home </Link>
            </li>
            <li>
               <Link to = "/hardware"> Hardware </Link>
            </li>
         </nav>
      </div>
   );
}

export default Project;
