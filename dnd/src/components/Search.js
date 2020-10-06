import React from 'react';

var Search= React.createClass({
    handleClick: function (event) {
        console.log(this.prop);
    },
    render: function () {
        return (
            <div className="date-range">
                <input type="submit" value="Search" onClick={this.handleClick} />
            </div>
        );
    }
});

var Results = React.createClass({
    render: function () {
        return (
            <div id="results" className="search-results">
                Some Results
            </div>
        );
    }
});

export default Search;