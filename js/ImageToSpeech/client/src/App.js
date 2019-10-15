import React from 'react';
import axios from "axios";
import './App.css';

function App() {
  // Text to speech

  const synth = window.speechSynthesis;

  function speak(text) {
    const utterThis = new SpeechSynthesisUtterance(text);
    synth.speak(utterThis);
  }

  function pause() {
    hide("pauseBtn");
    show("resumeBtn");
    synth.pause();
  }

  function resume() {
    hide("resumeBtn");
    show("pauseBtn");
    synth.resume();
  }

  // DOM functions

  function show(id) {
    document.getElementById(id).setAttribute("class", "visible");
  }

  function hide(id) {
    document.getElementById(id).setAttribute("class", "hidden");
  }

  // Event handlers

  let image;

  function handleFileSelect(e) {
    show("submitBtn");
    hide("selectImageSpan");
    image = e.target.files[0];
  }

  function handleClick(e) {
    hide("uploadInput");
    hide("submitBtn");
    show("uploadingSpan");

    const data = new FormData();
    data.append('image', image);
    
    const config = {
      headers: {
        'content-type': 'multipart/form-data'
      }
    };

    axios.post("http://localhost:5000/upload", data, config).then(res => {
      const textSpan = document.getElementById("textSpan");
      hide("uploadingSpan");
      show("outputSpan");
      show("uploadInput");
      speak(res.data);
      textSpan.innerHTML = res.data;

      const clearOutput = setInterval(() => {
        if (synth.speaking) {
          show("outputSpan");
          hide("selectImageSpan");
        } else if (!synth.speaking && !synth.paused) {
          hide("outputSpan");
          show("selectImageSpan");
          clearInterval(clearOutput);
        }
      }, 2000);
    });
  }

  //

  return (
    <div className="App">
      <header className="App-header">
        <p>
          <span id="selectImageSpan">
            Select an image
          </span>
          <br /><br />
          <input type="file" id="uploadInput" name="image" onChange={handleFileSelect} />
          <button id="submitBtn" onClick={handleClick} class="hidden">
            SUBMIT
          </button>
          <span id="uploadingSpan" class="hidden">
            Uploading the image...
          </span>
          <br /><br />
          <span id="outputSpan" class="hidden">
            <button id="pauseBtn" onClick={pause}>
              PAUSE
            </button>
            <button id="resumeBtn" onClick={resume} class="hidden">
              RESUME
            </button>
            <br /><br />
            <span id="textSpan"></span>
          </span>
        </p>
      </header>
    </div>
  );
}

export default App;
