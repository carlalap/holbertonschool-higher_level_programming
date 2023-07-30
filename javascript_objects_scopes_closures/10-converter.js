#!/usr/bin/node
// Task 10 - Function that converts a number from base 10
// to another base passed as argument:

// Prototype function
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
