#!/usr/bin/node
/** a script that gets the contents of a webpage and stores it in a file. */

// import the fs module specialized in file manipulation and
// the request module specialized in making HTTP requests
const Fs = require('fs');
const request = require('request');

// Get the page url
const URL = process.argv[2];
const Fname = process.argv[3];

// Create a GET request to fetch the contents of the page and
// save to a file with given name [pipe is used to connect the
//   readable stream to the writable]
request(URL).pipe(Fs.createWriteStream(Fname));
