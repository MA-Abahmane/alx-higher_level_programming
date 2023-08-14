#!/usr/bin/node
/* a script that searches the second biggest integer in the list of arguments. */

/*
  'process.argv' is an array in Node.js that contains the
  command-line arguments passed to the script. The .slice(2)
  method is used to extract the arguments starting from index 2.
*/
const args = process.argv.slice(2);
const argsLen = args.length;

if (argsLen > 1) {
  args.sort((a, b) => a - b);
  console.log(args[argsLen - 2]);
} else {
  console.log(0);
}
