
#url = 'http://127.0.0.1:4000/feed.twRloggers.xml'
#author = 'Need submission data'

#feed2json("http://127.0.0.1:4000/feed.twRloggers.xml", "Need submission data", "author/author.json")
def feed2json(url, author, dirname):
    import feedparser
    import time
    import json
    import os, sys
    
    d = feedparser.parse(url)

    ## Initialize variables
    post_url = ['']*len(d.entries)
    date = ['']*len(d.entries)
    title = ['']*len(d.entries)
    content = ['']*len(d.entries)
    tags = ['']*len(d.entries)
    

    ## Parse feed
    for i in range(0, len(d.entries)):
        post_url[i] = d.entries[i].link
        date[i] = d.entries[i].published_parsed
        date[i] = time.strftime('%Y-%m-%d', date[i])
        title[i] = d.entries[i].title
        content[i] = d.entries[i].description
        
        if 'tags' in d.entries[i]:
            onepost_tags = []
            for j in range(0, len(d.entries[i].tags)):
                onepost_tags.append(d.entries[i].tags[j].term)
            tags[i] = onepost_tags
        else:
            tags[i] = ['']
        
    ## Construct dictionary
    feed_dict = {}
    feed_dict['author'] = author
    feed_dict['title'] = title
    feed_dict['id'] = post_url
    feed_dict['date'] = date
    feed_dict['tags'] = tags
    feed_dict['content'] = content

    ## Save to JSON
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    with open(dirname + '/new.json', 'w') as fp:
        json.dump(feed_dict, fp)



