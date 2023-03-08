#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
let url = 'https://swapi-api.alx-tools.com/api/films/' + episode;
console.log(url);

request()
