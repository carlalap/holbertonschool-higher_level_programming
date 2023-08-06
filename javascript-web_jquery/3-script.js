#!/usr/bin/node
// task-3 - Add `.red` class
// script that adds the class red to the <header>
// element when the user clicks on the tag DIV#red_header

// Wait for the DOM to be ready
$(document).ready(function () {
  // Attach a click event handler to the #red_header div
  $('#red_header').click(function () {
    // Update the text color of the <header> element to red
    $('header').addClass('red');
  });
});
