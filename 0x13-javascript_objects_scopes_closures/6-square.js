#!/usr/bin/node
/* a class Square that defines a square and inherits from Rectangle of 4-rectangle.js: */

const oldSquare = require('./5-square');

class Square extends oldSquare {
  constructor (size) {
    super(size, size);
  }

  /* an instance method called charPrint(c) that prints the rectangle using the character c */
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let rectangle = '';
      for (let i = 0; i < this.height; i++) {
        rectangle += c;
      }
      console.log(rectangle);
    }
  }
}

module.exports = Square;
