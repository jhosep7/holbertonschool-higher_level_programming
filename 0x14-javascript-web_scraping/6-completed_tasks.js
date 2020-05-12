#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (response.statusCode === 200) {
    const done = {};
    for (const i of JSON.parse(body)) {
      if (i.completed === true) {
        if (i.userId in done) {
          done[i.userId] += 1;
        } else {
          done[i.userId] = 1;
        }
      }
    }
    console.log(done);
  } else if (err) throw err;
});
