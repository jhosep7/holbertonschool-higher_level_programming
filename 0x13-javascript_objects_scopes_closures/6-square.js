#!/usr/bin/node

const Sq = require('./5-square');
module.exports = class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let cont = 0; cont < this.width; cont++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
