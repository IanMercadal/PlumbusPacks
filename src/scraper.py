import urllib.request
list_links = []
page = "https://ianmercadal.github.io/PlumbusPacks/"

def get_page(page):
    try:
        request = urllib.request.urlopen(page)
    except:
        print(page)
    #si tiene el charset puesto:
    #html = request.read().decode(request.headers.get_content_charset())
    #si no:
    html = request.read().decode('utf-8')
    return html

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    page = page[start_quote + 1:end_quote]
    return page, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        page,endpos = get_next_target(page)
        if page:
            links.append(page)
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
            union(tocrawl,get_all_links(get_page(page)))
            crawled.append(page)
    return crawled
print (list_links)