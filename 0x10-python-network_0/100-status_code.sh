#!/bin/bash
#sends a request & displays only the status code of the response
curl -sL -w "%{http_code}" "$1" -X HEAD
