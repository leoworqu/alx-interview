#!/usr/bin/node

const axios = require('axios');

async function getCharacters(movieId) {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
    const response = await axios.get(url);
    const characters = response.data.characters;
    return characters;
}

async function printCharacters(movieId) {
    try {
        const characters = await getCharacters(movieId);
        for (let i = 0; i < characters.length; i++) {
            const characterResponse = await axios.get(characters[i]);
            console.log(characterResponse.data.name);
        }
    } catch (error) {
        console.error("Error fetching characters:", error);
    }
}

const movieId = process.argv[2];
if (!movieId) {
    console.error("Please provide a movie ID as an argument.");
} else {
    printCharacters(movieId);
}
