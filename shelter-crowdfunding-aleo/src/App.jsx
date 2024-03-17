import { useState } from "react";
import "./App.css";
import helloworld_program from "../helloworld/build/main.aleo?raw";
import { AleoWorker } from "./workers/AleoWorker.js";
import Project from "./Project.jsx";

const aleoWorker = AleoWorker();
function App() {
  const [count, setCount] = useState(0);
  const [account, setAccount] = useState(null);
  const [executing, setExecuting] = useState(false);
  const [deploying, setDeploying] = useState(false);
  const [goal, setGoal] = useState(1000);
  const [amountRaised, setAmountRaised] = useState(0);

  const generateAccount = async () => {
    const key = await aleoWorker.getPrivateKey();
    setAccount(await key.to_string());
  };

  async function execute() {
    setExecuting(true);
    const result = await aleoWorker.localProgramExecution(
      helloworld_program,
      "main",
      ["5u32", "5u32"],
    );
    setExecuting(false);

    alert(JSON.stringify(result));
  }

  async function deploy() {
    setDeploying(true);
    try {
      const result = await aleoWorker.deployProgram(helloworld_program);
      console.log("Transaction:")
      console.log("https://explorer.hamp.app/transaction?id=" + result)
      alert("Transaction ID: " + result);
    } catch (e) {
      console.log(e)
      alert("Error with deployment, please check console for details");
    }
    setDeploying(false);
  }

  return (
    <>
      <h1>Shelter Crowdfunding</h1>
      <div>
        <h2>Donate</h2>
    <div style={{display:"flex", gap:"20px"}}>
      <div style={{border:"4px solid white",  borderRadius:"20px", width:"25%"}} className="card w-96 bg-base-100 shadow-xl">
          <div className="card-body">
            <h2 className="card-title">Women</h2>
            <p>$50000</p>
            <div className="card-actions justify-end">
            <button className="btn" onClick={()=>document.getElementById('my_modal_1').showModal()}>Donate Now!</button>
            </div>
          </div>
        </div>
        <div style={{border:"4px solid white",  borderRadius:"20px", width:"25%"}} className="card w-96 bg-base-100 shadow-xl">
          <div className="card-body">
            <h2 className="card-title">Children</h2>
            <p>$50000</p>
            <div className="card-actions justify-end">
            <button className="btn" onClick={()=>document.getElementById('my_modal_1').showModal()}>Donate Now!</button>
            </div>
          </div>
        </div>
        <div style={{border:"4px solid white",  borderRadius:"20px", width:"25%"}} className="card w-96 bg-base-100 shadow-xl">
          <div className="card-body">
            <h2 className="card-title">Sanctuary</h2>
            <p>$50000</p>
            <div className="card-actions justify-end">
            <button className="btn" onClick={()=>document.getElementById('my_modal_1').showModal()}>Donate Now!</button>
            </div>
          </div>
        </div>
        <div style={{border:"4px solid white",  borderRadius:"20px", width:"25%"}} className="card w-96 bg-base-100 shadow-xl">
          <div className="card-body">
            <h2 className="card-title">Adoption</h2>
            <p>$50000</p>
            <div className="card-actions justify-end">
            <button className="btn" onClick={()=>document.getElementById('my_modal_1').showModal()}>Donate Now!</button>
            </div>
          </div>
        </div>
    </div>
    <div>
    <dialog id="my_modal_1" className="modal">
  <div className="modal-box">
    <p>
      <Project goal={50000} projectNumber={1} />
    </p>    
    <p className="py-4">Press ESC key or click the button below to close</p>
    <div className="modal-action">
      <form method="dialog">
        {/* if there is a button in form, it will close the modal */}
        <button className="btn">Close</button>
      </form>
    </div>
  </div>
</dialog>
    </div>
      </div>  
      {/* <div className="card">
        <p>
          <Project goal={50000} projectNumber={1} />
        </p>
      </div> */}

      <div className='footer'>
		    <h2> © 2024 BITHack-ShelterApp. All rights reserved.</h2>
      </div>
    </>
  );
}

export default App;
