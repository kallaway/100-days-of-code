var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'khangai',
  password: 'P@ssw0rd123',
  database: 'my_db'
})


var read_r = 'SELECT * FROM details';

connection.connect();
console.log('Database is connected');

connection.query(read_r, function(err, result, fields){
  if (err) throw err;

  else {
    console.log('Details are: ');
    console.log('Result : ' + JSON.stringify(result[0]));
  }
});

connection.end();
