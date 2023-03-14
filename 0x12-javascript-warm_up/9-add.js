#!/usr/bin/node
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

function add (a, b) {
  return a + b;
}

const result = add(a, b);
console.log(result);
