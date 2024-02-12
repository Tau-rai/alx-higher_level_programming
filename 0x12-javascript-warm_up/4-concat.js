#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 4) {
  console.log(argv[2] + ' is ' + argv[3]);
}
