var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'khangai',
  password: 'P@ssw0rd123',
  database: 'my_db'
})


var insert_r = 'INSERT INTO details (name, age) value(?,?)';

connection.connect();
console.log('Database is connected');

connection.query(insert_r, ['Khangaikhuu', 39], function(err, result, fields){
  if (err) throw err;

  else {
    console.log('Details added successfully');
    console.log('Result : ' + result);
  }
});

connection.end();
