#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL with the provided movie ID
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make the GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error:', 'Invalid movie ID');
  } else {
    console.log(JSON.parse(body).title);
  }
});
