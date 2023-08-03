#!/usr/bin/node
// Script that display the status code of a GET request.

if (process.argv.length !== 3) {
  console.log('Usage: node 2-statuscode.js <URL>');
  process.exit(1);
}
// Get the URL to request from the command line arguments
const URL = process.argv[2];
const request = require('request');

// Make the GET request
request.get(URL, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
