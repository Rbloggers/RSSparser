#!/bin/bash





while read p; do
    authorname=$(echo "$p" | cut -d ',' -f 1)
    
    # Check if dir exist
    [[ -d $authorname ]] || mkdir $authorname
    

    ################ Normal ####################
    # Download old data
    curl --fail "https://rbloggers.github.io/web/authors/$authorname/new.json" > "$authorname/old.json"
    ############################################
    
    ####### Interupution: make old post empty ########
    > "$authorname/old.json"
    ##########################

done < authorlist.txt
