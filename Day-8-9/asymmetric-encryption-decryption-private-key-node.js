var crypto = require('crypto');
var fs = require('fs');

privK = {
  key: fs.readFileSync('priv.key').toString(),
  passphrase: 'khangaikhuu'
}

var buf = Buffer.from('This is secret code', 'utf8');

secretData = crypto.privateEncrypt(privK, buf);

console.log(secretData.toString('utf8'));

pubK = fs.readFileSync('pub.key').toString();

origData = crypto.publicDecrypt(privK, secretData);

console.log(origData.toString());
