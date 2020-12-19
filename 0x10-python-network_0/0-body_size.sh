#!/bin/bash
# This script takes in a URL and returns the body size
curl -sI "$1" | awk '/Content-Length/{print $2}'
