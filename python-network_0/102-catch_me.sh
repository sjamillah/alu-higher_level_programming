#!/bin/bash
# Script that makes a request to causes an specific response
curl -s "0.0.0.0:5000/catch_me_3" | grep -o "You got me!"
