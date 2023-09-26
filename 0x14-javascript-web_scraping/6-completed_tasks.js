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
  if (!error && response.statusCode === 200) {
    const todoList = JSON.parse(body);
    const list = {};

    // search for id with completed tasks and ids completed tasks
    // loop trough the todo list looking for completed tasks
    todoList.forEach((todo) => {
      // if task is completed add 1 to user completes
      if (todo.completed) {
        if (list[todo.userId] === undefined) {
          list[todo.userId] = 1;
        } else {
          list[todo.userId] += 1;
        }
      }
    });

    // set all values in a dictionary style
    const values = `{${Object.entries(list).map(([key, value]) => ` '${key}': ${value}`).join(',\n ')} }`;

    // print object as is if list length is less than 3
    console.log(Object.keys(list).length > 2 ? values : list);
  } else {
    // print error
    console.log(error);
  }
});
