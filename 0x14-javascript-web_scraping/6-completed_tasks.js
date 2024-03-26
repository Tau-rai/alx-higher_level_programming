#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const url = argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  const tasksCompletedByUser = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (tasksCompletedByUser[todo.userId]) {
        tasksCompletedByUser[todo.userId]++;
      } else {
        tasksCompletedByUser[todo.userId] = 1;
      }
    }
  }

  console.log(tasksCompletedByUser);
});
