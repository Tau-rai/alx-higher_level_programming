#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const movieId = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  printCharacters(characterUrls, 0);
});

function printCharacters (characterUrls, i) {
  if (i >= characterUrls.length) {
    return;
  }

  request(characterUrls[i], function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    }

    const character = JSON.parse(body);
    console.log(character.name);

    // Recursively print the next character
    printCharacters(characterUrls, i + 1);
  });
}
