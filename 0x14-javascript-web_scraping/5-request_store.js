#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const fs = require('fs');

const url = argv[2];
const file = argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(file, body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
