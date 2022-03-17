from fastapi import FastAPI
from functions import geo_to_info, page_to_list, two_city, piece_of_name_to_variants

app = FastAPI()


@app.get('/')                 # ненужный метод
def home():
    return {'key': 'hello'}


@app.get('/{geoid}')         # Метод принимает идентификатор geonameid и возвращает информацию о городе
def get_info(geoid: str):
    return geo_to_info(geoid)


# Метод принимает страницу и количество отображаемых на странице городов и возвращает список городов с их информацией
@app.get('/pages/')
def get_page(page: int, num: int):
    return page_to_list(page, num)


# Метод принимает названия двух городов (на русском языке) и получает информацию о найденных городах,
# а также дополнительно: какой из них расположен севернее и одинаковая ли у них временная зона
# (когда несколько городов имеют одно и то же название, выбирает город с большим населением;
# если население совпадает, берет первый попавшийся)
# Также показывает пользователю не только факт различия временных зон, но и на сколько часов они различаются
@app.get('/two_cities/')
def get_two_city(city1: str, city2: str):
    return two_city(city1, city2)


# метод принимает часть названия города и возвращает подсказку с возможными вариантами продолжений (json list)
@app.get('/clue/')
def get_clue(name: str):
    return piece_of_name_to_variants(name)
