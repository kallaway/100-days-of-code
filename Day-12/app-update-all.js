var {MongoClient} = require('mongodb');

var new_db = "mongodb://localhost:27017"
MongoClient.connect(new_db, function(error, db) {
  if (error) {
    throw error;
  }
  var dbo = db.db("demo_db");
  var myobj = {$set: {name: "Minnie"}};
  var query = {address: /^S/};
  dbo.collection("customers").updateMany(query, myobj, function (err, collection){
        if (err) throw err;
        console.log("Record updated successfully");
    console.log(collection);
    db.close();
      });
    } );



