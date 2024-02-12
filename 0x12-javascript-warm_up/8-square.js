#!/usr/bin/node

const { argv } = require('process');
const character = 'X';
const size = parseInt(argv[2]);

if (argv.length <= 2) {
  console.log('Missing size');
} else {
  if (isNaN(size)) {
    console.log('Missing size');
  } else {
    let i;
    for (i = 0; i < size; i++) {
      let row = '';
      let j;
      for (j = 0; j < size; j++) {
        row += character;
      }
      console.log(row);
    }
  }
}
