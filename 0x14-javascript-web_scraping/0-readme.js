#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

const file = argv[2];
fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
