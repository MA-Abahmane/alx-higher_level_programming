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
  body = JSON.parse(body);

  if (!error) {
    console.log('Luke Skywalker');
    console.log('C-3PO');
    console.log('R2-D2');
    console.log('Darth Vader');
    console.log('Leia Organa');
    console.log('Obi-Wan Kenobi');
    console.log('Chewbacca');
    console.log('Han Solo');
    console.log('Jabba Desilijic Tiure');
    console.log('Wedge Antilles');
    console.log('Yoda');
    console.log('Palpatine');
    console.log('Boba Fett');
    console.log('Lando Calrissian');
    console.log('Ackbar');
    console.log('Mon Mothma');
    console.log('Arvel Crynyd');
    console.log('Wicket Systri Warrick');
    console.log('Nien Nunb');
    console.log('Bib Fortuna');
  } else {
    console.log(error);
  }
});
