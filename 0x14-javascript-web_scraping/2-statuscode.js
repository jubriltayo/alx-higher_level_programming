#!/usr/bin/node
// A script that display the status code of a GET request

const request = require('request');
const url = process.argv[2];

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
