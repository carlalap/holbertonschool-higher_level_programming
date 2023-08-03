#!/usr/bin/node
// Task-5. Script that gets the contents
// of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.log('Usage: node 5-request_store.js <URL> <file-path>');
  process.exit(1);
}

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make the GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error:', 'Failed to fetch data from the URL');
  } else {
    // Write the response to the file
    fs.writeFile(filePath, body, err => {
      if (err) {
        console.error('Error writing to the file:', err);
      } else {
        console.log('Successfully stored the response in the file:', filePath);
      }
    });
  }
});
