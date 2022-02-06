var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'khangai',
  password: 'P@ssw0rd123',
  database: 'my_db'
})


var read_r = 'UPDATE details SET age = ? WHERE name = ?';

connection.connect();
console.log('Database is connected');

connection.query(read_r,[25, 'khangaikhuu'], function(err, result, fields){
  if (err) throw err;

  else {
    console.log('Updated the age of khangaikhuu: ');
    console.log('Result : ' + JSON.stringify(result[0]));
  }
});

connection.end();
