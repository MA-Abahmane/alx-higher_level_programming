#!/usr/bin/node
/* a script that prints two arguments passed to it, in the following format: “ is ” */

/*
  'process.argv' is an array in Node.js that contains the
  command-line arguments passed to the script. The .slice(2)
  method is used to extract the arguments starting from index 2.
*/
const args = process.argv.slice(2);

console.log(args[0] + ' is ' + args[1]);
