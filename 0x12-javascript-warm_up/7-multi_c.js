#!/usr/bin/node

const { argv } = require('process');
const lang = 'C is fun';

if (argv.length <= 2) {
  console.log('Missing number of occurances');
} else {
  if (Number(argv[2]) > 0) {
    let i = 0;
    while (i < Number(argv[2])) {
      console.log(lang);
      i++;
    }
  }
}
