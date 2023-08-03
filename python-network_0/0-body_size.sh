#!/bin/bash
# Script that shows the Content-length from HTTP request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f2
