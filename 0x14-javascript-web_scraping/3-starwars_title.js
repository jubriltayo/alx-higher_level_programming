#!/usr/bin/node
// A script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(data);
    console.log(movie.title);
  }
});
