#!/usr/bin/node

const { resolve } = require('path');
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + episode;
console.log(url);

async function makeRequests(urls) {
  const promises = urls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });
  });

  const results = await Promise.all(promises);
  return results;
}

async function logname (url) {
  await request(url, async function (error, response) {
    console.log(error);
    const xter = JSON.parse(response.body).characters;
    console.log(xter);
    makeRequests(xter);
  });
}

logname(url);
