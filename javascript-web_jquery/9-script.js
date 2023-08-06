#!/usr/bin/node
// 9. Say Hello! - script that fetches from https://stefanbohacek.com/hellosalut/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello.

// Wait for the DOM to be ready
$(document).ready(function () {
  // Fetch movie data from the API
  $.getJSON('https://stefanbohacek.com/hellosalut/?lang=fr', function(data) {
    $('#hello').text(data.hello);
  });
});