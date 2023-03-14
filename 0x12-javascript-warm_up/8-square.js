#!/usr/bin/node
const args = Number(process.argv[2]);

if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < args; row++) {
    let line = '';
    for (let column = 0; column < args; column++) {
      line += 'X';
    }
    console.log(line);
  }
}
