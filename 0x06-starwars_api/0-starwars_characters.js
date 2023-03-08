#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + episode;
console.log(url);

request(url, function (error, response, body) {
  //console.log(error);
  console.log(response.body);
  //console.log(body);
});
