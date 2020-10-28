import React from 'react';
// import Search from './components/Search'
import './style.css';
var ReactDOM = require('react-dom');


class Board1 extends React.Component {
    constructor(){
        super(); 
        this.state = {
            items: [],
            currentItem: {
                text: '',
                key: ''
            }

        }
        this.addItem = this.addItem.bind(this);
        this.handleInput = this.handleInput.bind(this);
    }

    addItem(e){
        e.preventDefault();
        const newItem = this.state.currentItem;
        if(newItem.text !==""){
          const items = [...this.state.items, newItem];
        this.setState({
          items: items,
          currentItem:{
            text:'',
            key:''
          }
        })
        }
      }
      handleInput(e){
        this.setState({
          currentItem:{
            text: e.target.value,
            key: Date.now()
          }
        })
      }




    render () {
    return (
        <div>
        <h1 className="main-title">Todo Board</h1>
        <div className="drag-container"></div>
            <ul className="drag-list">
                {/* <!-- Backlog Column --> */}
                <li className="drag-column backlog-column">
                    <span className="header">
                        <h1>Backlog</h1>
                    </span>
                    {/* <!-- Backlog Content --> */}
                    <div id="backlog-content" className="custom-scroll">
                        <ul className="drag-item-list" id="backlog-list" 
                        ondrop="drop(event)" ondragover="allowDrop(event)" 
                        ondragenter="dragEnter(0)"></ul>
                    </div>
                    {/* <!-- Add button Group--> */}
                    <div className="add-btn-group">
                        <div className="add-btn" >
                            <span className="plus-sign">+</span>
                            <span >Add Item</span>
                            {/* <form onSubmit={this.addItem}>
                            <input type="text" placeholder="Enter task" value= {this.state.currentItem.text} onChange={this.handleInput}></input>
                                <button type="submit">Add</button>
                            </form> */}
                        </div>
                        <div className="add-btn solid" onclick="hideInputBox(0)">
                            <span>Save Item</span>
                        </div>
                    </div>
                    <div className="add-container">
                        <div className="add-item" contenteditable="true"></div>
                    </div>
                </li>
            </ul>
        </div>
    )
}
}

export default Board1;