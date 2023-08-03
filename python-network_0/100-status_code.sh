#!/bin/bash
# Script that sends a request to an URL and displays the status code
curl -sI "$1" -o /dev/null -w "%{http_code}"
