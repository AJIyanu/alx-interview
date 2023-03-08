#!/usr/bin/node

const { resolve } = require('path');
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + episode;
console.log(url);

async function logname (url) {
  const peopleurl = await request(url, async function (error, response) {
    console.log(error);
    const xter = JSON.parse(response.body).characters;
    console.log(xter);
    for (let i = 0; i < xter.length; i++) {
      await request(xter[i], function (error, response) {
        //console.log(error);
        console.log(JSON.parse(response.body).name);
      });
    }
  });
}

logname(url);
