#!/usr/bin/node
/* a script that prints x times “C is fun” */

/*
  'process.argv' is an array in Node.js that contains the
  command-line arguments passed to the script. The .slice(2)
  method is used to extract the arguments starting from index 2.
*/
const args = process.argv.slice(2);

a = parseInt(args[0]);

function add(a) {
    let result, n = 1;

    if (!isNaN(a)) {
        result = add(a + result);
    } else {
        console.log(1);
    }

    console.log(result);
};

add(a);
