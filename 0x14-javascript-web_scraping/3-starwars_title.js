#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req(url, function (err, response, body) {
  console.log(err || JSON.parse(body).title);
});
