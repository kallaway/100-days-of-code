import React from 'react';
import Search from './components/Search'
import './style.css';
var ReactDOM = require('react-dom');

const addBtns = [];
const saveItemBtns = [];
const addItemContainers = [];

class Board1 extends React.Component {
    constructor(){
        super(); 
        this.state = {

        }
    }

    // addItem = () => {
    //     // const [showResults, setShowResults] = React.useState(false)
    //     return (
    //       <div>
    //         <input type="submit" value="Search" />
    //         {/* { showResults ? <results /> : null } */}
    //       </div>
    //     )
        
    //   }



//  results = React.createClass({
//     render: function () {
//         return (
//             <div id="results" className="search-results">
//                 Some Results
//             </div>
//         );
//     }
// });



    render () {
    const {Search} = this.state
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