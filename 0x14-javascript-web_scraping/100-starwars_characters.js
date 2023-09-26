#!/usr/bin/node
/** a script that prints all characters of a Star Wars movie: */

// import the fs module specialized in file manipulation and
// the request module specialized in making HTTP requests
const request = require('request');

// Get the page url
const URL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Create a GET request to fetch the contents of the page
request(URL, function (error, response, body) {
  // if no errors and the request was OK; start process
  if (!error) {
    let i;
    const charactersList = JSON.parse(body);

    for (i = 0; i < charactersList.length; i++) {
      request(charactersList[i], function (error, response, Body) {
        console.log(JSON.parse(Body).name);
      });
    }
  } else {
    console.log(error);
  }

});
