import React from "react";
import {Link} from "react-router-dom";
import "./hardware_formatting.css"

class Hardware extends React.Component{
   constructor(props){
      super(props);
      this.state = {
         hardwareAvailable: true, //state to maintain if can check out more hardware or not
         hardwareAmount: 50}; 
   }

   /* Update states after adding specified amount of hardware
    * Updates hardwareAmount by adding props to hardwareAmount
    * Current max is set to be 50
    * TODO - implement a global constant so 50 isn't hardcoded
    */
   add(amountToAdd){ //seems like "props" is reserved and can't be used as param name
      //recognizes first hardwareAmount in setState, but doesn't know what 
      //it is when performing an operation on it unless specified with "this"
      //don't wrap parameter in {} when using it to perform numerical operations
      this.setState({hardwareAmount: this.state.hardwareAmount + amountToAdd});
      if (this.state.hardwareAmount > 0){ //check if have more than 0 avaiable hardware
         this.setState({hardwareAvailable: true}); //if not, than change state to reflect
      }
   }

   /* Update state after removing specified amount of hardware
    * Updates hardwareAmount by subtracting props from hardwareAmount
    * Then checks if hardwareAmount is less than 0
    * If so, sets hardwareAvailable to false
    */
   remove(amountToRemove) {
      console.log("In remove function");
      this.setState({hardwareAmount: this.state.hardwareAmount - amountToRemove});
      console.log("hardwareAmount after removal: ",this.state.hardwareAmount);
      if (this.state.hardwareAmount === 0){ //check if have more than 0 avaiable hardware
         this.setState({hardwareAvailable: false}); //if not, than change state to reflect
      }
   }

   render(){
      const hardwareAvailable = this.state.hardwareAvailable;
      const hardwareAmount = this.state.hardwareAmount;
      const amount = 10;
      let addButton;
      let removeButton;

      //disable add button if max is reached
      if (hardwareAvailable && (hardwareAmount === 50) ){ 
         addButton = <button disabled onClick = {() => this.add(amount)}> Add {amount} </button>;
         removeButton = <button onClick = {() => this.remove(amount)}> Remove {amount} </button>;
//         console.log("first if statement");
         //enable both buttons if between max and min
      } else if (hardwareAvailable && (hardwareAmount < 50)){ 
         addButton = <button onClick = {() => this.add(amount)}> Add {amount} </button>;
         removeButton = <button onClick= {() => this.remove(amount)}> Remove {amount} </button>;
//         console.log("second if statement");
         // disable remove button if min is reached (0)
      } else if (!hardwareAvailable){
         addButton = <button onClick = {() => this.add(amount)}> Add {amount} </button>;
         removeButton = <button disabled onClick = {() => this.remove(amount)}>
                           Remove {amount} 
                        </button>;
//         console.log("third if statement");
      }

      return (
         //apparently this qualifies as a "parent element" that allow for multiple lines of JSX
         <div>       
          <h2>Hardware</h2>
          <p> this is the hardware page. Amount is currently {amount}</p>
          {addButton}
          {removeButton}
          <p className = "displayHardwareTotal"> 
            Current amount of available hardware is {hardwareAmount}
          </p>
          <nav>
             <Link to = "/"> Home </Link>
          </nav >
         </div>
      );
   }
}

export default Hardware;
