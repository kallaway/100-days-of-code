import React from 'react';
import './style.css';
var React = require('react');
var ReactDOM = require('react-dom');


class Board extends React.Component {

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
            </ul>
        </div>
    )
}
}

export default Board;