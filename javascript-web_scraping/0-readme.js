#!/usr/bin/node
// let us to read and write files
const fs = require('fs');
// array that contains the command-line arguments.
// the first 2 elements are always reserved for
// the node executable and the name of the script being executed
const filePath = process.argv[2];
// Read the content of the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
