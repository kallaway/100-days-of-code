var qs = require('querystring');

var value_json = qs.stringify({ id: 1, name: ['abc', 'khangaikhuu'], tutorial: '30days of node', creator : 'khangaikhuu' });
console.log(value_json); 

var value_json_2 = qs.stringify({ id: 2, name: ['def', 'khangaikhuu2'], tutorial: '30days of node', creator : 'khangaikhuu' },';');
console.log("Changing the default 'sep' from '&' to ';'. An example is shown below:");
console.log(value_json_2); 

var value_json_3 = qs.stringify( {id: 3, name: ['hij', 'khangaikhuu'], tutorial: '30days of node', creator : 'khangaikhuu' },';',':');
console.log("Changing the default 'eq' from '=' to ':'. An example is shown below:")
console.log(value_json_3);
