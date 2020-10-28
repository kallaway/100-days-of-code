import React from 'react';
import './style.css';
import React, { Component } from 'react';
import ScriptTag from 'react-script-tag';


class Board extends React.Component {
    // constructor(props){
    //     super(props); 
    //     this.state = {
    //         updatedOnLoad: false,
    //         backlogListArray: [],
    //         progressListArray: [],
    //         completeListArray: [],
    //         onHoldListArray: [],
    //         listArrays: [],
    //         dragging: false
    //     }
    //   }


    render () {
    return (
        <div>
        <h1 class="main-title">Todo Board</h1>
        <div class="drag-container"></div>
            <ul class="drag-list">
                {/* <!-- Backlog Column --> */}
                <li class="drag-column backlog-column">
                    <span class="header">
                        <h1>Backlog</h1>
                    </span>
                    {/* <!-- Backlog Content --> */}
                    <div id="backlog-content" class="custom-scroll">
                        <ul class="drag-item-list" id="backlog-list" 
                        ondrop="drop(event)" ondragover="allowDrop(event)" 
                        ondragenter="dragEnter(0)"></ul>
                    </div>
                    {/* <!-- Add button Group--> */}
                    <div class="add-btn-group">
                        <div class="add-btn" onclick="showInputBox(0)">
                            <span class="plus-sign">+</span>
                            <span>Add Item</span>
                        </div>
                        <div class="add-btn solid" onclick="hideInputBox(0)">
                            <span>Save Item</span>
                        </div>
                    </div>
                    <div class="add-container">
                        <div class="add-item" contenteditable="true"></div>
                    </div>
                </li>
                 {/* <!-- Progress Column --> */}
                 <li class="drag-column progress-column">
                    <span class="header">
                        <h1>Progress</h1>
                    </span>
                    {/* <!-- Progress Content --> */}
                    <div id="progress-content" class="custom-scroll">
                        <ul class="drag-item-list" id="progress-list" 
                        ondrop="drop(event)" ondragover="allowDrop(event)" 
                        ondragenter="dragEnter(1)"></ul>
                    </div>
                    {/* <!-- Add button Group--> */}
                    <div class="add-btn-group">
                        <div class="add-btn" onclick="showInputBox(1)">
                            <span class="plus-sign">+</span>
                            <span>Add Item</span>
                        </div>
                        <div class="add-btn solid" onclick="hideInputBox(1)">
                            <span>Save Item</span>
                        </div>
                    </div>
                    <div class="add-container">
                        <div class="add-item" contenteditable="true"></div>
                    </div>
                </li>
                 {/* <!-- Complete Column --> */}
                 <li class="drag-column complete-column">
                    <span class="header">
                        <h1>Complete</h1>
                    </span>
                    {/* <!-- Complete Content --> */}
                    <div id="complete-content" class="custom-scroll">
                        <ul class="drag-item-list" id="complete-list" 
                        ondrop="drop(event)" ondragover="allowDrop(event)" 
                        ondragenter="dragEnter(2)"></ul>
                    </div>
                    {/* <!-- Add button Group--> */}
                    <div class="add-btn-group">
                        <div class="add-btn" onclick="showInputBox(2)">
                            <span class="plus-sign">+</span>
                            <span>Add Item</span>
                        </div>
                        <div class="add-btn solid" onclick="hideInputBox(2)">
                            <span>Save Item</span>
                        </div>
                    </div>
                    <div class="add-container">
                        <div class="add-item" contenteditable="true"></div>
                    </div>
                </li>
                 {/* <!-- On-hold Column --> */}
                 <li class="drag-column on-hold-column">
                    <span class="header">
                        <h1>On-hold</h1>
                    </span>
                    {/* <!-- On-hold Content --> */}
                    <div id="on-hold-content" class="custom-scroll">
                        <ul class="drag-item-list" id="on-hold-list" 
                        ondrop="drop(event)" ondragover="allowDrop(event)" 
                        ondragenter="dragEnter(3)"></ul>
                    </div>
                    {/* <!-- Add button Group--> */}
                    <div class="add-btn-group">
                        <div class="add-btn" onclick="showInputBox(3)">
                            <span class="plus-sign">+</span>
                            <span>Add Item</span>
                        </div>
                        <div class="add-btn solid" onclick="hideInputBox(3)">
                            <span>Save Item</span>
                        </div>
                    </div>
                    <div class="add-container">
                        <div class="add-item" contenteditable="true"></div>
                    </div>
                </li>
            </ul>
        </div>
    )
}
}

export default Board;