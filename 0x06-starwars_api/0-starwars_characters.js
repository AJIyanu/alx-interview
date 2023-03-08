#!/usr/bin/node

const { rejects } = require('assert');
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + episode;
console.log(url);

async function makerequest (people_url) {
  return new promise ((resolve, rejects) => {
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
