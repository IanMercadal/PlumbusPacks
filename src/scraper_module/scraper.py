#from src.crawler_module.crawler import Links
import json
import urllib.request
crawled = ["https://ianmercadal.github.io/PlumbusPacks/packtacano.html","https://ianmercadal.github.io/PlumbusPacks/packeconomico.html","https://ianmercadal.github.io/PlumbusPacks/packmedio.html", "https://ianmercadal.github.io/PlumbusPacks/packpremium.html","https://ianmercadal.github.io/PlumbusPacks/packdeluxe.html"]

def get_page(url):
    absoluta = "https://ianmercadal.github.io/PlumbusPacks/" 
    if url.find("http") == -1:
        url = absoluta + url
    request = urllib.request.urlopen(url)
    url = request.read().decode("utf-8")
    return url

def conseguir_links(codigo, link):
    if link in crawled:
        nombre = codigo[codigo.find("<h2>") : codigo.find("</h2>")]
        precio = codigo[codigo.find("<h3>") + 7 : codigo.find("</h3>")]
    while codigo.count("<h2>") != 0:
        caracteristicas = []
        caracteristicas.append(codigo[codigo.find("") : codigo.find("")])
        codigo = codigo[ codigo.find("</h2>")]
    packs = {'nombre':nombre,'precio':precio}
    print(packs)
    return packs

#if __name__ == "__main__":
    #assert get_next_target(url) == {"ada"}
    #assert conseguir_links(codigo,link) == ("dad")