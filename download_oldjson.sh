#!/bin/bash
RED='\033[0;31m'
NC='\033[0m'

while read p; do
    authorname=$(echo "$p" | cut -d ',' -f 1)
    
    # Check if dir exist
    [[ -d $authorname ]] || mkdir $authorname
    
    ################ Normal ####################
    # Download old data
    curl --silent --show-error --fail "https://raw.githubusercontent.com/Rbloggers/RSSparser/gh-pages/$authorname/new.json" > "$authorname/old.json" || printf "${RED}$authorname${NC} old.json\n\n"
    ############################################
    
    ######## Interupution: make old post empty ########
    #> "$authorname/old.json"
    ##########################

done < authorlist.txt
