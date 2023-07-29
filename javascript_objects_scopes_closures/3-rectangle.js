#!/usr/bin/node
// task 3 - Script with class Rectangle that defines 2 argmuments (w, h) of rectangle:
// If w or h is equal to 0 or not a positive integer, create an empty object
// Create method called print() that prints the rectangle using the character X
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
