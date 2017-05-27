def get_page(link):
   import urllib.request
   sourcecode =urllib.request.urlopen(link).read().decode('utf-8')
   return sourcecode

def get_next_target(page):
    start_link = page.find('<a href=')
    if (start_link != -1):
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote #This is done to obtain string of url as well as starting position to find next link
    else:
        return None, 0

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

##url, endpos = get_next_target(page)
##
##print (url)
#Now to print all links:
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled


print(crawl_web(get_page('https://xkcd.com/353/')))
