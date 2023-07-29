#!/usr/bin/node
// task 4 - Script with class Rectangle that defines 2 argmuments (w, h) of rectangle:
// If w or h is equal to 0 or not a positive integer, create an empty object
// Create method called print(), rotate() and double() that prints the rectangle using the character X
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

  double () {
    // multiples the width and the height of the rectangle by 2
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    // exchanges the width and the height of the rectangle
    [this.width, this.height] = [this.height, this.width];
  }
};
