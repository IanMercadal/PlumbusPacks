import json
import urllib.request
crawled = ["https://ianmercadal.github.io/PlumbusPacks/packtacano.html","https://ianmercadal.github.io/PlumbusPacks/packeconomico.html","https://ianmercadal.github.io/PlumbusPacks/packmedio.html", "https://ianmercadal.github.io/PlumbusPacks/packpremium.html","https://ianmercadal.github.io/PlumbusPacks/packdeluxe.html"]

def get_page(url):
    absoluta = "https://ianmercadal.github.io/PlumbusPacks/packs.html" 
    if url.find("http") == -1:
        url = absoluta + url
    request = urllib.request.urlopen(url)
    url = request.read().decode("utf-8")
    return url


if __name__ == "__main__":
    #assert get_next_target(url) == {"ada"}