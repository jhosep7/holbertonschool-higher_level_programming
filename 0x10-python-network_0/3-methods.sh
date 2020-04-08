#!/bin/bash
#takes a URL and displays all HTTP methods the server will accept.
curl -sI "$1" -X OPTIONS | grep "Allow" | cut -f2- -d " "
