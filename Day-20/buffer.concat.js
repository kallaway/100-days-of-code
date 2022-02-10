var buff1 = Buffer.from('Khangaikhuu for nodejs ');
var buff2 = Buffer.from('- 100 days of node');
var output = Buffer.concat([buff1, buff2]);
console.log("Buff3 content: " + output.toString());

