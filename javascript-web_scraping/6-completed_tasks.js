#!/usr/bin/node
// Task-6. Script that computes the
// number of tasks completed by user id.
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// make the GET request to the API
request.get(apiUrl, { json: true }, (error, response, data) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error:', 'Failed to fetch data from the API');
  } else {
    // Filter the data to get only completed tasks
    const completedTasks = data.filter(task => task.completed);

    // Count the number of complete tasks for each user ID
    const totalCompletedTaskperId = completedTasks.reduce((count, task) => {
      count[task.userId] = (count[task.userId] || 0) + 1;
      return count;
    }, {});

    console.log(totalCompletedTaskperId);
  }
});
