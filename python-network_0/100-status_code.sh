#!/bin/bash
# Script that sends a request to an URL and displays the status code
curl -so /dev/null -w "%{http_code}" "$1"
