#!/usr/bin/node
/* a script that prints x times “C is fun” */

/*
  'process.argv' is an array in Node.js that contains the
  command-line arguments passed to the script. The .slice(2)
  method is used to extract the arguments starting from index 2.
*/
const args = process.argv.slice(2);
const a = parseInt(args[0]);

function factorial (n) {
  if (isNaN(n)) {
    return (1);
  } else if (n <= 1) {
    return (1);
  } else {
    const result = n * factorial(n - 1);
    return (result);
  }
}

console.log(factorial(a));
