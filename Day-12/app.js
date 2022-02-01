var {MongoClient} = require('mongodb');

var new_db = "mongodb://localhost:27017/demo_db"



async function main() {

  const client = new MongoClient(new_db);

  try {
    await client.connect();

    console.log('Database connection to demo_db is successfully established');
    await listDatabases(client)
  } catch(e) {
    console.error(e);
  } finally {
    await client.close();
  }
}

async function listDatabases(client) {
  databasesList = await client.db().admin().listDatabases();

  console.log("Databases:");

  databasesList.databases.forEach(db => console.log(' - ' + db.name));
}
main().catch(console.error);
