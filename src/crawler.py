import urllib.request
list_links = []
url = "https://ianmercadal.github.io/PlumbusPacks/"

def get_page(url):
    absoluta = "https://ianmercadal.github.io/PlumbusPacks/"
    if url.find("http") == -1:
        url = absoluta + url
    try:
        request = urllib.request.urlopen(url)
    except:
        print(url)
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

def get_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            list_links.append(url)
            page = page[endpos:]
        else:
            break
    return list_links

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled


#page = get_page(url)
#get_all_links(page)
#print(list_links)
#get_all_links(list_links)

if __name__ == "__main__":
    #assert get_page(url) == "https://ianmercadal.github.io/PlumbusPacks/"
    #assert get_next_target('<!DOCTYPE html>\n<html lang="en">\n\n    <head>\n        <meta http-equiv="content-type" content="text/html;charset=utf-8" />\n        <meta name="description" content="Packs de Bienvenida">\n        <meta name="keywords" content="Packs de Bienvenida">\n        <link href="static/css/cssL.css" rel="stylesheet" type="text/css" media="(min-width:1000px)" />\n        <link href="static/css/cssM.css" rel="stylesheet" type="text/css" media="(min-width:551px) and (max-width:999px)"  />\n        <link href="static/css/cssS.css" rel="stylesheet" type="text/css" media="(max-width:550px)" />\n        <link rel="stylesheet" href="estilos.css">\n        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n        <link href="https://fonts.googleapis.com/css2?family=Quicksand&family=Roboto:wght@100&display=swap" rel="stylesheet">\n        <title>Plumbus Packs</title>\n        <link rel="icon" type="image/jpg"  href="imagenes/logo.png">\n        \n    </head>\n\n<body>\n    <header><img class="logo" src="imagenes/logo.png" alt="Imagen del logo"/>\n        <nav>\n            <ul id="menu"><!--Nuestro menu de navegación-->\n                <li><a href="index.html">Inicio</a></li>\n                <li><a href="packs.html">Packs</a></li>\n                <li><a href="productos.html">Productos</a></li>\n                <li><a href="blogs.html">Experiencias y viajes astrales</a></li>\n            </ul>\n        </nav>\n    \n    </header>\n    \n    <main>\n    \n        <div class="marquee" ><p>Posibles descuentos para que todo el mundo pueda disfrutar de los packs una vez sea legal hacer fiestas.</p></div>     \n        \n    <div class="container">\n        <img src="imagenes/imageninicio.jpg" alt="Avatar" class="image">\n    </div>\n\n    <hr>\n\n            <article class="inicio">\n\n                <h3>¿Quiénes somos?</h3>\n            \n                <p>Somos unos estudiantes que hemos creado un proyecto que va destinado a los packs de bienvenida para eventos.\n                    En esta página vamos a mostrar los tipos de packs que tenemos disponibles para cualquier tipo de eventos.\n                    Actualizaremos en la medida de lo posible nuestros productos para el tipo de evento, es decir, si en una boda,\n                    se puede solicitar un color dentro de nuestra paleta de colores más adecuado al evento, principalmente se solicita el nieve.\n                </p>\n                \n                <h3>¿Qué son nuestros packs?</h3>\n    \n                <p>\n                    Hemos hecho una serie de packs que varían en cuanto a productos según el precio de este. Para una mayor explicación,\n                    dirigete a la sección de Packs situada en el menu de navegación o si quieres saber más sobre los productos\n                    más individualmente, dirígete a productos. \n                </p>\n            </article>\n\n    </main>\n    \n    <hr>\n\n\n    <footer><!--Aquí ponemos, en nuestro caso, copyright y otros datos-->\n        <section class="columnfooter">\n            <ul class="footer">\n                <li>Copyright © 2020 All rights reserved.</li>\n                <li>Número de teléfono: 602194569-653583930</li>\n                <li>Nuestros correos: imercadal@cifpfbmoll.eu - afrongia@cifpfbmoll.eu</li>\n                <li>Alumnos: Ian Mercadal y Abril Frongia</li>\n            </ul>\n            \n        </section>\n        <section class="columnfooter">\n            <iframe class="footer" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3075.61854125192!2d2.66508651532964!3d39.56820797947284!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x129793b01716a01b%3A0x55bc574de040df4a!2sCIFP%20Francesc%20de%20Borja%20Moll!5e0!3m2!1sca!2ses!4v1605344013094!5m2!1sca!2ses" \n            width="300" height="150" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>\n        </section>\n    \n        </footer>\n\n</body>\n\n</html>') == []
    #assert get_all_pages == ""
    assert crawl_web("https://ianmercadal.github.io/PlumbusPacks/") == ['index.html', 'packs.html', 'productos.html', 'blogs.html']