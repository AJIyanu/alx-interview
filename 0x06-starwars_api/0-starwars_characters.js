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

async function getpeople(url) {
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
  console.log(people);
  const res = await makeRequests(people);
  console.log(res);
}

logname(url);
