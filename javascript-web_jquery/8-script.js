#!/usr/bin/node
// 8. Star wars movies - script that fetches and lists 
// the title for all movies by using this 
// URL: https://swapi-api.hbtn.io/api/films/?format=json

// Wait for the DOM to be ready
$(document).ready(function () {
  // Fetch movie data from the API
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
    // get the character name
    var movieTitles = data.results.map(function(movie) {
      return movie.title;
    });
  
    // Create list of movies titles
    var movieList = $("<ul></ul>");
    movieTitles.forEach(function(title) {
      var listItem = $("<li>" + title + "</li>");
      movieList.append(listItem);
    });

    // Append the movie list to the #list_movies ul
    $('#list_movies').html(movieList);
  });
});
