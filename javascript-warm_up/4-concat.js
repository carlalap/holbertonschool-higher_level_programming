#!/usr/bin/node
// task 4 - script that prints two arguments
// passed to it, in the following format: “ is”

// Get the first argument from process.argv
const firstArg = process.argv[2];

// Get the second argument from process.argv
const scndArg = process.argv[3];

// Print the two arguments in the specified format
console.log(firstArg + ' is ' + scndArg);
