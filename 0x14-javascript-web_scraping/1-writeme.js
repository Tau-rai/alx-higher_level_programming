#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

const file = argv[2];
const dataString = argv[3];
fs.writeFile(file, dataString, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
