#!/usr/bin/node
/** a script that gets the contents of a webpage and stores it in a file. */

// import the fs module specialized in file manipulation and
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

    body = JSON.parse(body);

    for (i = 0; i < body.length; i++) {
        // get the id and completed list of each user
        const userId = body[i].userId;
        const completed = body[i].completed;

        // count his completes
        if (completed)
        {
            if (!completedList[userId]) {
                completedList[userId] = 1;
            } else {
                completedList[userId] += 1;
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
