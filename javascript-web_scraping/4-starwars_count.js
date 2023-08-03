#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const apiUrl = process.argv[2];

// Make the GET request to the Star Wars API to get the list
// of the films
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error:', 'Failed to fetch data from the API');
  } else {
    const filmsData = JSON.parse(body);
    const characterId = 18; // Character ID

    // Filter films where “Wedge Antilles” is present
    const filmsWedge = filmsData.results.filter(film =>
      film.characters.includes(`${apiUrl}people/${characterId}/`)
    );

    console.log(filmsWedge.length);
  }
});
