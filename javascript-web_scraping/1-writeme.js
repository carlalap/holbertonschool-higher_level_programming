#!/usr/bin/node
// let us to read and write files
// with the fs (file system) module
const fs = require('fs');
// Get the file path and string to write from the command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];
// write the string to the file
fs.writeFile(filePath, stringToWrite, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
