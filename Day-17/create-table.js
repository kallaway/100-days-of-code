var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'khangai',
  password : 'P@ssw0rd123',
  database: 'my_db'
})


var table = "CREATE TABLE details (id int(15) NOT NULL AUTO_INCREMENT," + "name varchar(30) DEFAULT NULL," + "age float(15) DEFAULT NULL," + "PRIMARY KEY (ID)) ENGINE=InnoDB DEFAULT CHARSET=latin1";


connection.connect();

connection.query(table, function(err, result, fields){
    if (err) throw err;
    else {
      console.log('Table created successfully');
      console.log("Result: " + result);
    }
  });

connection.end();


