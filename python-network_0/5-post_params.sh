#!/bin/bash
# Script that sends a POST request to the URL and displays the body
curl -sX POST "$1" -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD'
