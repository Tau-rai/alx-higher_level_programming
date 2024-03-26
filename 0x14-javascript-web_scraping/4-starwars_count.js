#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const url = argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const characterId = 18;
    let filmCount = 0;

    for (const film of data.results) {
      if (film.characters.some(characterUrl =>
        characterUrl.endsWith(`/${characterId}/`))) {
        filmCount++;
      }
    }
    console.log(filmCount);
  }
});
