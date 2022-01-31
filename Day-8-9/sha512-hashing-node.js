var crypto = require('crypto');

var hash = crypto.createHash('sha512');

data = hash.update('khangaikhuu', 'utf-8');

gen_hash = data.digest('hex');

console.log("hash : " + gen_hash);
