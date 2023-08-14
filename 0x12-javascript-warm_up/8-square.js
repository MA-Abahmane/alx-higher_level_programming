#!/usr/bin/node
/* a script that prints a square */

/*
  'process.argv' is an array in Node.js that contains the
  command-line arguments passed to the script. The .slice(2)
  method is used to extract the arguments starting from index 2.
*/
const args = process.argv.slice(2);

const x = parseInt(args[0]);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    let square = '';
    for (let j = 0; j < x; j++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
