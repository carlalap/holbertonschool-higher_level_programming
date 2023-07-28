#!/usr/bin/node
// task 5 - script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer
// Get the first argument from process.argv
const num = process.argv[2];

// Convert the first argument to an integer using parseInt()
// const num = parseInt(firstArg);

// Checks if the conversion was succesful
if (!isNaN(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
