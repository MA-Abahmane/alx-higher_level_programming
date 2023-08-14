#!/usr/bin/node
/* a script that prints the addition of 2 integers */

/*
  'process.argv' is an array in Node.js that contains the
  command-line arguments passed to the script. The .slice(2)
  method is used to extract the arguments starting from index 2.
*/
const args = process.argv.slice(2);

const a = parseInt(args[0]);
const b = parseInt(args[1]);

function add (a, b) {
  console.log(a + b);
}

add(a, b);
