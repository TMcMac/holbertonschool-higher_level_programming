#!/bin/bash
# curl a url and get only the status code
curl -s -o /dev/null -I -w "%{http_code}\n" "$1"
