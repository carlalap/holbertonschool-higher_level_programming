#!/usr/bin/node
// task-4 - Add `.red` class
// script that adds the class red to the <header>
// element when the user clicks on the tag DIV#red_header

// Wait for the DOM to be ready
$(document).ready(function () {
  // Attach a click event handler to the #red_header div
  $('#toggle_header').click(function () {
    // Update the text color of the <header> element to red
    $('header').toggleClass('red green');
  });
});
