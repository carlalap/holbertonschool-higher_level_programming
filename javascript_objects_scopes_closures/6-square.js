#!/usr/bin/node
// task 6 - Script class Square and inherits from Square of 5-square.js:
// with an instance method called charPrint(c) that prints the
// rectangle using the character c If c is undefined, use the character X
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    // Prints the rectangle using the char "c"
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
