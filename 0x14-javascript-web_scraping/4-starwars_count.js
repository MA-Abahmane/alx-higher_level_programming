#!/usr/bin/node
/**
 * script that prints the number of movies where the character “Wedge Antilles” is present.
**/

// import the request module specialized in making HTTP requests
const request = require('request');
const URL = process.argv[2];

// GET request to the given URL and take in the response
request(URL, function (error, response, body) {
  // if no error; proceed
  if (!error) {
    // Get the list of films
    const films = JSON.parse(body).results;

    // Print the count of caracters found
    console.log(films.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        // if a character with id == 18 is found, increment count by one;
        ? count + 1
        : count;
    }, 0));
  }
});
