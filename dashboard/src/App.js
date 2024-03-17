import './App.css';
import { useQuery } from "convex/react";
import { useState, useEffect, useRef } from 'react';
import { api } from "./convex/_generated/api";

function App() {
  const messages = useQuery(api.messages.get);
  const [editedStatus, setEditedStatus] = useState("");
  const inputValues = useRef({}); // Use useRef to store input field values

  // const handleStatusChange = (id, event) => {
  //   setEditedStatus(prevStatus => ({
  //     ...prevStatus,
  //     [id]: event.target.value
  //   }));
  // };

  const handleStatusChange = (id, event) => {
    setEditedStatus(prevStatus => ({
      ...prevStatus,
      [id]: event.target.value
    }));
  };

  const handleFocus = (id) => {
    // Store the current value of the input field when it receives focus
    inputValues.current[id] = editedStatus[id];
  };

  return (
    <div>
      <div className='title'>
        <h1 >SOS Messages</h1>
      </div>
      <div className='center-container'>
        <div className="App">
          {messages !== null && Array.isArray(messages) && messages.length > 0 ? ( // Check if messages is not null and is an array with length > 0
            messages.map(({ _id, message, status }) => (
              <div key={_id} className="message-container">
                <div className="message">{message}</div>
                <input
                  type="text"
                  value={editedStatus[_id] !== undefined ? editedStatus[_id] : status}
                  onFocus={() => handleFocus(_id)} // Call handleFocus when the input field receives focus
                  onChange={(e) => handleStatusChange(_id, e)}
                />
              </div>
            ))
          ) : (
            <p>Loading...</p>
          )}
        </div>
    </div>
    </div>
  );
}

export default App;
