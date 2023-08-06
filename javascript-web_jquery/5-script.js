#!/usr/bin/node
// task-5 - List of elements
// script that adds a <li> element to a list when 
// the user clicks on the tag DIV#add_item

// Wait for the DOM to be ready
$(document).ready(function () {
  // Attach a click event handler to the #add_item div
  $('#add_item').click(function () {
    // adding new element
    $('.my_list').append('<li>Item</li>');
  });
});
