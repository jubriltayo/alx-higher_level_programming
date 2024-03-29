#!/usr/bin/node
// A script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');
const url = process.argv[2];
const completedTasks = {};

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(data);

    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });
    console.log(completedTasks);
  }
});
