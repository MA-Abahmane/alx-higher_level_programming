#!/usr/bin/node
/* a script that prints a message depending of the number of arguments passed: */

/*
  'process.argv' is an array in Node.js that contains the
  command-line arguments passed to the script. The .slice(2)
  method is used to extract the arguments starting from index 2.
*/
const args = process.argv.slice(2);
const argsLen = args.length;

if (argsLen <= 0) {
  console.log('No argument');
} else if (argsLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
