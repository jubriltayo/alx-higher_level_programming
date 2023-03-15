#!/usr/bin/node
const SquareMain = require('./5-square');

module.exports = class Square extends SquareMain {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += 'C';
        }
        console.log(line);
      }
    }
  }
};
