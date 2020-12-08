from src.crawler import crawl_web
import pytest

def crawl_web():
    assert crawl_web("https://ianmercadal.github.io/PlumbusPacks/index.html") == ['https://ianmercadal.github.io/PlumbusPacks/index.html', 'blogs.html', 'productos.html', 'packs.html', 'packdeluxe.html', 'packpremium.html', 'packmedio.html', 'packeconomico.html', 'packtacano.html', 'index.html']