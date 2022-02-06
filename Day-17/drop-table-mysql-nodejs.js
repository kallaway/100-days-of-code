var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'khangai',
  password: 'P@ssw0rd123',
  database: 'my_db'
})


var drop_T =  'DROP table details';

connection.connect();
console.log('Database is connected');

connection.query(drop_T, function(err, result, fields){
  if (err) throw err;

  else {
    console.log('A record is removed: ');
    console.log('Result : ' + JSON.stringify(result[0]));
  }
});

connection.end();
