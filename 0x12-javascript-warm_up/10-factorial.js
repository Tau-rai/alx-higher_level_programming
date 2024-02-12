#!/usr/bin/node

const { argv } = require('process');

function factorial (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

if (argv.length >= 2) {
  const num = Number(argv[2]);
  if (isNaN(num)) {
    console.log(1);
  } else {
    console.log(factorial(num));
  }
}
