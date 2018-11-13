import subprocess, parse, json, os
from pprint import pprint
import numpy as np
import time


#######  Prepare new & old JSON  ########

# Download Old json data
subprocess.call(["bash", "download_oldjson.sh"])


# Get author feeds
with open('authorlist.txt') as f:
    lines = f.read().splitlines()

# New json data: Parse feeds
dirname = ['']*len(lines)
for i in range(0, len(lines)):
    ls = lines[i].split(",")
    dirname[i] = ls[0]
    parse.feed2json(url=ls[2], author=ls[1], dirname=ls[0])
    


#########  Findout New Posts  ###########
for i in range(0, len(dirname)):
    
    ## Read data
    with open(dirname[i] + '/new.json') as f:
        new_data = json.load(f)
        
    if os.path.getsize(dirname[i] + '/old.json') == 0:
        old_data = {}
        old_data['id'] = ['']
#        old_data['date'] = ['']
#        old_data['tags'] = ['']
#        old_data['content'] = ['']
    else:
        with open(dirname[i] + '/old.json') as f2:
            old_data = json.load(f2)
    
    ## Find new post idx
    new_posts = set(new_data['id']) - set(old_data['id'])
    
    # If no new posts found
    if len(new_posts) == 0:
        continue # enter next for loop
    
    # If new posts are found
    new_urls = np.array(new_data['id'])
    new_idx = []
    for j in list(new_posts):
        idx = np.where(new_urls == j)[0][0]
        new_idx.append(int(idx))
    
    
    ## Contruct New posts data
    feed_dict = {}
    feed_dict['author'] = new_data['author']
    
    # If only 1 new post found
    if len(new_idx) == 1:
        new_idx = new_idx[0]
       
        feed_dict['id'] = new_data['id'][new_idx]
        feed_dict['rblog_url'] = new_data['rblog_url'][new_idx]
        feed_dict['date'] = new_data['date'][new_idx]
        feed_dict['tags'] = new_data['tags'][new_idx]
        feed_dict['content'] = new_data['content'][new_idx]
        
    # If more than 1 new posts found
    else:
        new_post_id = ['']*len(new_idx)
        new_post_rblog_url = ['']*len(new_idx)
        new_post_date = ['']*len(new_idx)
        new_post_tags = ['']*len(new_idx)
        new_post_title = ['']*len(new_idx)
        new_post_content = ['']*len(new_idx)
        
        for k in range(0, len(new_idx)):
            new_post_id[k] = new_data['id'][new_idx[k]]
            new_post_rblog_url[k] = new_data['rblog_url'][new_idx[k]]
            new_post_date[k] = new_data['date'][new_idx[k]]
            new_post_tags[k] = new_data['tags'][new_idx[k]]
            new_post_title[k] = new_data['title'][new_idx[k]]
            new_post_content[k] = new_data['content'][new_idx[k]]
        
        feed_dict['id'] = new_post_id
        feed_dict['rblog_url'] = new_post_rblog_url
        feed_dict['date'] = new_post_date
        feed_dict['tags'] = new_post_tags
        feed_dict['title'] = new_post_title
        feed_dict['content'] = new_post_content
        
    with open(dirname[i] + '/new_post.json', 'w') as fp:
        json.dump(feed_dict, fp)
    
    
    
