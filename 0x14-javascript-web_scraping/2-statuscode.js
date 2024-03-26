#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const url = argv[2];

request(url, function (error, response) {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response && response.statusCode);
});
