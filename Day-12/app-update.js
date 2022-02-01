var {MongoClient} = require('mongodb');

var new_db = "mongodb://localhost:27017"
MongoClient.connect(new_db, function(error, db) {
  if (error) {
    throw error;
  }
  var dbo = db.db("demo_db");
  var myobj = {$set: {name: "Khangaikhuu Uvgunkhuu", address: "Highway 37"}};
  var query = {name: "Khangaikhuu Uvgunkhuu"};
  dbo.collection("customers").updateOne(query, myobj, function (err, collection){
        if (err) throw err;
        console.log("Record updated successfully");
    console.log(collection);
      });
    } );



