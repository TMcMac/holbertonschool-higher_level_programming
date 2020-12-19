#!/bin/bash
# curl a url and get only the status code
curl -sw "%{http_code}" "$1" -o /dev/null
