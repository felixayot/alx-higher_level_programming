#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (err, response, body) {
  if (!err) {
    const todos = JSON.parse(body);
    const doneTasks = {};
    todos.forEach((t) => {
      if (t.completed && doneTasks[t.userId] === undefined) {
        doneTasks[t.userId] = 1;
      } else if (t.completed) {
        doneTasks[t.userId] += 1;
      }
    });
    console.log(doneTasks);
  }
});
