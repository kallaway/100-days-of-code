var {MongoClient} = require('mongodb');

var new_db = "mongodb://localhost:27017"
MongoClient.connect(new_db, function(error, db) {
  if (error) {
    throw error;
  }
  var dbo = db.db("demo_db");
  dbo.collection("customers").findOne({}, function (err, collection){
        if (err) throw err;
        console.log("Record Read successfully");
        console.log(collection);
        db.close();
      });
    } );



