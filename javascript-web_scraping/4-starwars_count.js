#!/usr/bin/node
// Task-4. Script that prints the number of movies where
// the character “Wedge Antilles” is present.
const request = require('request');

// Get the movie ID from the command line arguments
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error:', 'Failed to fetch data from the API');
  } else {
    const filmsData = JSON.parse(body);
    const characterId = 18;

    // Filter films where “Wedge Antilles” is present
    const filmsWedge = filmsData.results.filter(movie =>
      movie.characters.some(character =>
        character.endsWith(`/${characterId}/`)
      )
    );

    console.log(filmsWedge.length);
  }
});
