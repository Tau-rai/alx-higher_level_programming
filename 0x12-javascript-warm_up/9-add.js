#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  console.log(a + b);
}

if (argv.length <= 4) {
  const a = Number(argv[2]);
  const b = Number(argv[3]);
  add(a, b);
}
