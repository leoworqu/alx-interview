#!/usr/bin/node

const request = require('request');

function getCharacters (movieId) {
  return new Promise((resolve, reject) => {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characters = JSON.parse(body).characters;
        resolve(characters);
      }
    });
  });
}

function printCharacters (movieId, index) {
  getCharacters(movieId).then(characters => {
    if (index >= characters.length) {
      return;
    }

    request.get(characters[index], (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterName = JSON.parse(body).name;
        console.log(characterName);
        printCharacters(movieId, index + 1);
      } else {
        console.error('Error fetching character:', error);
      }
    });
  }).catch(error => {
    console.error('Error fetching characters:', error);
  });
}

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID as an argument.');
} else {
  printCharacters(movieId, 0);
}
