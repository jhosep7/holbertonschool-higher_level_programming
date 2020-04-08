#!/bin/bash
#sends a POST request to the passed URL, and displays the resp body
curl -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1" -X POST
