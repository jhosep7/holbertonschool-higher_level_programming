#!/bin/bash
#takes URL as argument, sends GET request to URL & shows resp body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1" -X GET
