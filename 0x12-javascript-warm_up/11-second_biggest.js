#!/usr/bin/node
const args = process.argv.slice(2); //starts from index 2

if (args.length <= 1) {
  console.log('0');
} else {
  const numbers = args.map(x => parseInt(x)); // typecast args into int
  const max = Math.max(...numbers); // spread numbers
  const secondNumbers = numbers.filter(x => x < max); // filter nums less than max
  const secondMax = Math.max(...secondNumbers);
  console.log(secondMax);
}
