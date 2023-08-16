#!/usr/bin/node
/* a script that imports an array and computes a new array */

let list = require('./100-data.js').list;
console.log(list);

/** each value equal to the value of the initial list, multipled by the index in the list */
const myList = list.map((x, idx) => x * idx);
console.log(myList);
