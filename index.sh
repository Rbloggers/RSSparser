#!/bin/bash

cat >> index.md  << _EOF_

# List of JSON
<br><br>

_EOF_

while read p; do
    dir=$(echo "$p" | cut -d ',' -f 1)
    author=$(echo "$p" | cut -d ',' -f 2)
    printf "$author ([new](${dir}/new.json), [old](${dir}/old.json), [post](${dir}/new_post.json))\n\n" >> index.md
    
done < authorlist.txt
