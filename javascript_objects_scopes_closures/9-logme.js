#!/usr/bin/node
// Task 9 - Function that prints the number of arguments
// already printed and the new argument value.

// Prototype function
let numberArgs = 0;

exports.logMe = function (item) {
  console.log(`${numberArgs}: ${item}`);
  numberArgs++;
};
