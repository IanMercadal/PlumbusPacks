from src.crawler_module.crawler import union, crawl_web

def test_index():
    assert crawl_web("https://ianmercadal.github.io/PlumbusPacks/index.html") == ['https://ianmercadal.github.io/PlumbusPacks/index.html', 'blogs.html', 'productos.html', 'packs.html', 'packdeluxe.html', 'packpremium.html', 'packmedio.html', 'packeconomico.html', 'packtacano.html', 'index.html']

def test_int_value():
    assert union(["a", "b", "c"], 777777) == False

def test_two_arrays_false():
    assert union("Hola", "Adiós") == False

def test_array_false():
    assert union("No es lo mismo", ["a", "b", "c", "d",
                           "e", "f", "g", "h", "i"]) == False
def test_Int_String():
    assert union(123456, "string") == False
