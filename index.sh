#!/bin/bash

cat >> index.md  << _EOF_
[![Build Status](https://travis-ci.org/Rbloggers/RSSparser.svg?branch=master)](https://travis-ci.org/Rbloggers/RSSparser)

# Authors
<br><br>

_EOF_

while read p; do
    dir=$(echo "$p" | cut -d ',' -f 1)
    author=$(echo "$p" | cut -d ',' -f 2)
    printf "$author ([new](${dir}/new.json), [old](${dir}/old.json), [post](${dir}/new_post.json))\n\n" >> index.md
    
done < authorlist.txt
