#!/usr/bin/node
// task-2 - Click and turn red

// Wait for the DOM to be ready
$(document).ready(function () {
  // Attach a click event handler to the #red_header div
  $('#red_header').click(function () {
    // Update the text color of the <header> element to red
    $('header').css('color', '#FF0000');
  });
});
