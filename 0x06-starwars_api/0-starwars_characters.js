#!/usr/bin/node

const { resolve } = require('path');
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + episode;
console.log(url);

async function logname (url) {
  const peopleurl = await request(url, function (error, response) {
    console.log(error);
    return JSON.parse(response.body).characters;
  });
  console.log(typeof (peopleurl));
  console.log(peopleurl);
}

logname(url);
