#!/bin/bash

# Login to access token
travis login --github-token=${GH_TOKEN}
travis_tk=`travis token`


body='{
"request": {
"message": "API request from RSSparser to build web page",
"branch": "dev"
}}'


curl -s -X POST \
   -H "Content-Type: application/json" \
   -H "Accept: application/json" \
   -H "Travis-API-Version: 3" \
   -H "Authorization: token ${travis_tk}" \
   -d "$body" 'https://api.travis-ci.org/repo/Rbloggers%2FRbloggers.github.io/requests'
   
