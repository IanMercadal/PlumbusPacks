import urllib.request
list_links = []
url = "index.html" #Cambiar página si es necesario

def gethtml(url,webpage="https://ianmercadal.github.io/PlumbusPacks/"):
    try:
        request = urllib.request.urlopen(webpage + url)
    except:
        print(webpage + url)
    html = request.read().decode('utf-8')
    return html


def get_next_link(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        url = None
        end_quote = 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
    return url, end_quote


def print_all_links(page):
    while True:
        url, endpos = get_next_link(page)
        if url:
            if url == '#' or url in list_links or ".." in url:
                page = page[endpos+1:]
                continue
            else:
                list_links.append(url)
                page = page[endpos:]
        else:
            break

def get_all_pages(list_links):
    for url in list_links:
        page = gethtml(url)
        print_all_links(page)
        list_links = list(set(list_links))

page = gethtml(url)
print_all_links(page)
print(list_links)


get_all_pages(list_links)
print(list_links)
