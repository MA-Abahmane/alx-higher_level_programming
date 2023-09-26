#!/usr/bin/node
/** A script that display the status code of a GET request. */

// import the request module specialized in making HTTP requests
const request = require('request');
const URL = process.argv[2];

// GET request to a given URL and take in the response
request.get(URL).on('response', function (response) {
    // from the response get the status code and print
    console.log(`code: ${response.statusCode}`);
});
