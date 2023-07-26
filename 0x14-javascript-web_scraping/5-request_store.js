#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, data, { encoding: 'utf-8' }, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
