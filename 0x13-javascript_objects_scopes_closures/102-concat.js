#!/usr/bin/node
/* a script that concats 2 files. */

/*
  'process.argv' is an array in Node.js that contains the
  command-line arguments passed to the script. The .slice(2)
  method is used to extract the arguments starting from index 2.
*/
const fs = require('fs');
const args = process.argv.slice(2);

/** load file names:
 * The first argument is the file path of the first source file
 * The second argument is the file path of the second source file
 * The third argument is the file path of the destination
 */
const F1 = args[0];
const F2 = args[1];
const F3 = args[2];

/** read data from both first and second file */
const F1Data = fs.readFileSync(F1, 'utf8');
const F2Data = fs.readFileSync(F2, 'utf8');

/** fuse the data from both files */
const fusionData = F1Data + F2Data;

/** write data to the third file */
fs.writeFileSync(F3, fusionData, 'utf8');
