#!/usr/bin/node
const data = require('./100-data').list;

const newList = data.map((x, i) => x * i);
console.log(data);
console.log(newList);
