var {MongoClient} = require('mongodb');

var new_db = "mongodb://localhost:27017"
MongoClient.connect(new_db, function(error, db) {
  if (error) {
    throw error;
  }
  var dbo = db.db("demo_db");
  var myobj = {name: "Khangaikhuu Uvgunkhuu", address: "Highway 37"};
  dbo.collection("customers").insertOne(myobj, function (err, res){
        if (err) throw err;
        console.log("1 document inserted");
        db.close();
      });
    } );



