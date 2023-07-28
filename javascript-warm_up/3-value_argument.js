#!/usr/bin/node
// task 3 - script that prints the first argument passed to it:
const firstArg = process.argv[2];

// Print the message based on the presence of the first argument
if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
