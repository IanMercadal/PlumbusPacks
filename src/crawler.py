import urllib.request
list_links = []
wanted_links = ['packs.html', 'packtacano.html', 'packeconomico.html', 'packmedio.html', 'packpremium.html', 'packdeluxe.html']
url = "https://ianmercadal.github.io/PlumbusPacks/"

def get_page(url):
    absoluta = "https://ianmercadal.github.io/PlumbusPacks/" 
    if url.find("http") == -1:
        url = absoluta + url
    request = urllib.request.urlopen(url)
    html = request.read().decode("utf-8")
    return html


def get_next_target(page):
    start_link = page.find("<a href=")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p, q):
    for e in q:  
        if e not in p: 
            p.append(e)
            
def get_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            list_links.append(url)
            page = page[endpos:]
        else:
            break
    Links = list(dict.fromkeys(list_links))
    print(Links)
    return list_links

def crawl_web(seed):
    crawled = []
    tocrawl = [seed] # Links por crawlear
    while tocrawl: # Bucle que añade los links a las listas correspondientes
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

if __name__ == "__main__":
    #assert (url) == 'https://ianmercadal.github.io/PlumbusPacks/'
    #assert get_next_target() == ""
    #assert get_all_links() == ""
    #assert crawl_web() == ['https://ianmercadal.github.io/PlumbusPacks/', 'blogs.html', 'productos.html', 'packs.html', 'packdeluxe.html', 'packpremium.html', 'packmedio.html', 'packeconomico.html', 'packtacano.html', 'index.html']
    assert crawl_web("https://ianmercadal.github.io/PlumbusPacks/index.html") == ['index.html', 'packs.html', 'productos.html', 'blogs.html']
    #assert (list_links) == []