var crypto = require('crypto');

var hmac = crypto.createHmac('md5', 'secret');

data = hmac.update('khangaikhuu');

gen_hash = data.digest('hex');

console.log("hash : " + gen_hash);
