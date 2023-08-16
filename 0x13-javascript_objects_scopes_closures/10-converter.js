#!/usr/bin/node
/* a function that converts a number from base 10 to another base passed as argument: */

exports.converter = function (base) {
  /** In the conv function, it converts the
   *  decimal number n to a string representation
   *  in the specified base using the toString()
   *  method.
   */
  return function conv (n) {
    return n.toString(base);
  };
};
