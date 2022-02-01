var {MongoClient} = require('mongodb');

var new_db = "mongodb://localhost:27017"
MongoClient.connect(new_db, function(error, db) {
  if (error) {
    throw error;
  }
  var dbo = db.db("demo_db");
  var query = {name: "Khangaikhuu Uvgunkhuu"};

  dbo.collection("customers").deleteOne(query, function (err, collection){
        if (err) throw err;
        console.log("Record Deleted successfully");
        console.log(collection);
        db.close();
      });
    } );



