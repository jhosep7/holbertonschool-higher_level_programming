#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (response.statusCode === 200) {
    let i = 0;
    for (const episode of JSON.parse(body).results) {
      for (const actor of episode.characters) {
        if (actor.endsWith('18/')) { i++; }
      }
    }
    console.log(i);
  } else if (err) throw err;
});
