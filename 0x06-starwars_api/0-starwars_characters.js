#!/usr/bin/node

const { resolve } = require('path');
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + episode;
console.log(url);

async function makerequest (people_url) {
  return new Promise((resolve, reject) => {
    request(people_url, function(error, response) {
      console.log(error);
      const result = JSON.parse(response.body);
      console.log(result.name);
    });
  });
}

request(url, function (error, response, body) {
  console.log(error);
  const result = JSON.parse(response.body);
  console.log(result.characters);
  const xter = result.characters;
  makerequest(xter[1]);
});

async function logname(url) {
  const peopleurl = await request(url);
  console.log(typeof (peopleurl));
}

logname(url);
