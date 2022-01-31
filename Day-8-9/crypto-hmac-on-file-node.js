var crypto = require('crypto');
var fs = require('fs');

var algorithm = 'md5';
var secret = 'secret';

var hash = crypto.createHmac(algorithm, secret); 

var filename = 'data-hmac.txt';

var file_data = fs.ReadStream(filename);

file_data.on('data', function(data){
  hash.update(data);
});

file_data.on('end', function() {
  var gen_hash = hash.digest('hex');
  console.log('Hash generated using ' + algorithm + '\nHashed output is : ' + gen_hash + ' \nFile name is : ' + filename);

  fs.writeFileSync(filename, gen_hash);
});

