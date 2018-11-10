#!/bin/bash

while read p; do
    authorname=$(echo "$p" | cut -d ',' -f 1)
    
    # Check if dir exist
    [[ -d $authorname ]] || mkdir $authorname
    
    # Download old data
    curl "https://rbloggers.github.io/authors/$authorname/new.json" > "$authorname/old.json"
done < authorlist.txt
