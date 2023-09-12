#!/usr/bin/node
const newData = require('./100-data.js').list;
console.log(newData);
console.log(newData.map((x, i) => x * i));
