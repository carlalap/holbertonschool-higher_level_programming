#!/usr/bin/node
// task 2 - Script with class Rectangle that defines 2 argmuments (w, h) of rectangle:
// If w or h is equal to 0 or not a positive integer, create an empty object
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
