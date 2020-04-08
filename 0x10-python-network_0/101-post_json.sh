#!/bin/bash
#sends a JSON POST request to a URL passed as the first argument
curl -sd @"$2" -H "Content-Type: application/json" "$1" -X POS
T
