#!/bin/bash
#request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -sL 0:5000/catch_me "You got me!" -H "Origin: HolbertonSchool" -d "user_id=98" -X PUT
