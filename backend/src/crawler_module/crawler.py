import urllib.request
url = "https://ianmercadal.github.io/PlumbusPacks/"

def get_page(url):
    absoluta = "https://ianmercadal.github.io/PlumbusPacks/" 
    if url.find("http") == -1:
        url = absoluta + url
    request = urllib.request.urlopen(url)
    url = request.read().decode("utf-8")
    return url


def get_next_target(page):
    start_link = page.find("<a href=")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]

    #PostCondiciones
    assert isinstance(url, str)
    assert isinstance(end_quote, int)

    return url, end_quote



def get_all_links(page):
    list_links = []
    assert isinstance(list_links, list)
    
    while True:
        url, endpos = get_next_target(page)
        if url:
            list_links.append(url)
            page = page[endpos:]
        else:
            break
        #* POSTCONDITIONAL
    assert list_links is not []
 
    return list_links


def union(p, q):
    if type(p) != list or type(q) != list:
        return False
    for e in q:  
        if e not in p: 
            p.append(e)
            

def crawl_web(seed):
    crawled = []
    tocrawl = [seed]
    Unwanted_links = ["https://ianmercadal.github.io/PlumbusPacks/index.html","https://ianmercadal.github.io/PlumbusPacks/blogs.html", "https://ianmercadal.github.io/PlumbusPacks/productos.html"]
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
        
    nuevos_crawleados = []
    for link in crawled:
        if link in Unwanted_links:
            continue
        else:
            nuevos_crawleados.append(link)
    print(nuevos_crawleados)
    return nuevos_crawleados

if __name__ == "__main__":
    pass
    #assert (url) == 'https://ianmercadal.github.io/PlumbusPacks/'
    #assert crawl_web("https://ianmercadal.github.io/PlumbusPacks/index.html") == ['https://ianmercadal.github.io/PlumbusPacks/index.html', 'blogs.html', 'productos.html', 'packs.html', 'packdeluxe.html', 'packpremium.html', 'packmedio.html', 'packeconomico.html', 'packtacano.html', 'index.html']