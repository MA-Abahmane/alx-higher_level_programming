#!/usr/bin/node
/* a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer: */

/*
  'process.argv' is an array in Node.js that contains the
  command-line arguments passed to the script. The .slice(2)
  method is used to extract the arguments starting from index 2.
*/
const args = process.argv.slice(2);

const val = parseInt(args[0]);

if (!isNaN(val)) {
  console.log('My number: ' + args[0]);
} else {
  console.log('Not a number');
}
