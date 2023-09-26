#!/usr/bin/node
/** A script that prints the title of a Star Wars movie where
  * the episode number matches a given integer.
**/

// import the request module specialized in making HTTP requests
const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// GET request to the given URL and take in the response
request(URL, function (error, response, body)
{
    // if an error occurred; return it
    if (error)
    {
        console.log(error);
        return;
    }
    // if no error encountered; return the value of title after parsing JSON string
    console.log(JSON.parse(body));
});
