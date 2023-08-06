#!/usr/bin/node
// 7. Star wars character - script that fetches 
// the character name from this URL: 
// https://swapi-api.hbtn.io/api/people/5/?format=json

// Wait for the DOM to be ready
$(document).ready(function () {
  // Attach a click event handler to the #add_item div
  $.get('https://swapi-api.hbtn.io/api/people/5', function(data) {
    // get the character name
    var characterName = data.name;
  
    // Display the character name in the #character div
    $('#character').text(characterName);
  });
});
