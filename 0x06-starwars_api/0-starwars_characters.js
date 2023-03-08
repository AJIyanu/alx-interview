#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + episode;

async function makeRequests (urls) {
  const promises = urls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(response.body).name);
        }
      });
    });
  });

  const results = await Promise.all(promises);
  return results;
}

async function getpeople (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(response.body).characters);
      }
    });
  });
}

async function logname (url) {
  const people = await getpeople(url);
  const res = await makeRequests(people);
  res.forEach((names) => {
    console.log(names);
  });
}

logname(url);
