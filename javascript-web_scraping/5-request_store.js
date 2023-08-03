#!/usr/bin/node
// Task-5. Script that gets the contents
// of a webpage and stores it in a file.

// Get the URL and file path from the command line arguments
const URL = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');

// Make the GET request to the URL
request.get(URL, (error, response, body) => {
  if (!error) {
    fs.writeFile(file, body, error => {
      if (error) console.error(error);
    });
  }
});
