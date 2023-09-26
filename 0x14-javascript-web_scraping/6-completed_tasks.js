#!/usr/bin/node
/** A script that computes the number of tasks completed by user id. */

// the request module specialized in making HTTP requests
const request = require('request');

// Get the page url
const URL = process.argv[2];

// Create a GET request to fetch the contents of the page
request(URL, function (error, response, body) {
  // if no errors and the request was OK; start process
  if (!error) {
    let i;
    const completedList = {};

    // parce the response
    body = JSON.parse(body);

    for (i = 0; i < body.length; i++) {
      // get the id and completed list of each user
      const ID = body[i].userId;
      const tasksDone = body[i].completed;

      // count his completes
      if (tasksDone) {
        if (!completedList[ID]) {
          completedList[ID] = 1;
        } else {
          completedList[ID] += 1;
        }
      }
    }

    // print results
    console.log(completedList);
  } else {
    // print error
    console.log(error);
  }
});
