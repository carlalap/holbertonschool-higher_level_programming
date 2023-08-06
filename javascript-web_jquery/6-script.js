#!/usr/bin/node
// 6. Change the text - script that updates the text of the
// <header> element to New Header!!! 
// when the user clicks on DIV#update_header

// Wait for the DOM to be ready
$(document).ready(function () {
  // Attach a click event handler to the #add_item div
  $('#update_header').click(function () {
    // updates the text of the <header>
    $('header').text('New Header!!!');
  });
});
