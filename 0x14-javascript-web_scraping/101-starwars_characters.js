#!/usr/bin/node
// A script that prints all characters of a Star Wars movie
// in the same order of the list “characters” in the /films/ response

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
    return;
  }
  const actors = JSON.parse(data).characters;

  // create an array of promises to fetch data of each character
  const promises = actors.map(actor => {
    // promise to fetch data of each character
    return new Promise((resolve, reject) => {
      // make a request to fetch each character's data
      request(actor, (error, response, data) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(data).name);
        }
      });
    });
  });

  // wait for all promises to resolve before printing
  Promise.all(promises)
    .then(characters => {
      console.log(characters.join('\n'));
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
