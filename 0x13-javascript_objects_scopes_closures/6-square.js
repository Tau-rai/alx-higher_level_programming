#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    if (c !== undefined) {
      let i;
      for (i = 0; i < this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
