#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const character = 'X';
    let i;
    for (i = 0; i < this.height; i++) {
      let row = '';
      let j;
      for (j = 0; j < this.width; j++) {
        row += character;
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
