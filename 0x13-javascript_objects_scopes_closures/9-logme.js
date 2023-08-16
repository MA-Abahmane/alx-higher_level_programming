#!/usr/bin/node
/* a function that prints the number of arguments already printed / argument values */
let count = 0;

exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
