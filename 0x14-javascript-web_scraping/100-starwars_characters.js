#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const actors = JSON.parse(data).characters;
    actors.forEach((actor) => {
      request(actor, (err, res, data2) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(data2).name);
        }
      });
    });
  }
});
