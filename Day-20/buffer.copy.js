var buff = Buffer.from('Khangaikhuu');
var newBuff = Buffer.alloc(20);
buff.copy(newBuff);
console.log("Content of newbuff : " + newBuff.toString());
