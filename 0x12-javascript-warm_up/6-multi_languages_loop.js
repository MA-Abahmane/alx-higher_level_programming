#!/usr/bin/node
/* a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop */

const L1 = 'C is fun';
const L2 = 'Python is cool';
const L3 = 'JavaScript is amazing';

const arr = [L1, L2, L3];

for (const i in arr) {
  console.log(arr[i]);
}
