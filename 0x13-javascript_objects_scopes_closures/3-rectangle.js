#!/usr/bin/node
/* Write an empty class Rectangle that defines a rectangle: */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rectangle = '';
      for (let j = 0; j < this.width; j++) {
        rectangle += 'X';
      }
      console.log(rectangle);
    }
  }
}

module.exports = Rectangle;
