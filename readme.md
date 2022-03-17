#HTTP-сервер предоставляет REST API для предоставления информации по географическим объектам
Сервер запускается следующим образом: ```python3 script.py```


## Метод принимает идентификатор geonameid и возвращает информацию о городе

`GET geonameid` вернёт информацию о городе.

### Пример запроса
`GET 12394958`

### Ответ



```json
{
    "geonameid": "12394958",
    "name": "Ozero Zaton",
    "asciiname": "Ozero Zaton",
    "alternatenames": "Ozero Zaton,\u041e\u0437\u0435\u0440\u043e \u0417\u0430\u0442\u043e\u043d",
    "latitude": "52.53151",
    "longitude": "33.66945",
    "feature class": "H",
    "feature code": "LK",
    "country code": "RU",
    "cc2": "",
    "admin1 code": "10",
    "admin2 code": "",
    "admin3 code": "",
    "admin4 code": "",
    "population": "0",
    "elevation": "",
    "dem": "110",
    "timezone": "Europe/Moscow",
    "modification date": "2021-12-19"
}
```

На python можно получить словарь с информацией об этом городе (geonameid=12394958) следующим образом:
```python
import requests
import json

r = requests.get('http://127.0.0.1:8000/12394958')
geo_info1 = json.loads(r.json())
```
В переменной ```geo_info1``` будет находиться словарь с информацией о городе (geonameid=12394958).

--------------------------------------------

## Метод принимает страницу и количество отображаемых на странице городов и возвращает список городов с их информацией
`GET pages` возвращает список городов с их информацией.

Параметры:
* `page` – номер страницы
* `num` – количество результатов на страницу


### Пример запроса
`GET pages/?page=5&num=2`

### Ответ
```json
[
    {
        "geonameid": "451755", 
        "name": "Zasten\u2019ye", 
        "asciiname": "Zasten'ye",
        "alternatenames": "",
        "latitude": "57.27055",
        "longitude": "34.73",
        "feature class": "P",
        "feature code": "PPL",
        "country code": "RU",
        "cc2": "", 
        "admin1 code": "77", 
        "admin2 code": "", 
        "admin3 code": "", "admin4 code": "", 
        "population": "0", "elevation": "", 
        "dem": "184", 
        "timezone": "Europe/Moscow", 
        "modification date": "2011-07-09"
    }, 

    {
        "geonameid": "451756", 
        "name": "Zarech\u2019ye", 
        "asciiname": "Zarech'ye", 
        "alternatenames": "", 
        "latitude": "56.68265", 
        "longitude": "34.70984", 
        "feature class": "P", 
        "feature code": "PPL", 
        "country code": "RU", 
        "cc2": "", 
        "admin1 code": "77", 
        "admin2 code": "", 
        "admin3 code": "", 
        "admin4 code": "", 
        "population": "0", 
        "elevation": "", 
        "dem": "178", 
        "timezone": "Europe/Moscow",
        "modification date": "2011-07-09"
    }
]
```
На python можно получить страницу в виде списка словарей с информацией о городах следующим образом:
```python
import requests
import json

r = requests.get('http://127.0.0.1:8000/pages/?page=5&num=2')
geo_info2 = json.loads(r.json())
```
В переменной ```geo_info2``` будет находиться список словарей с информацией о городах на странице page.

--------------------------------------------

## Метод принимает названия двух городов (на русском языке) и возвращает информацию о найденных городах 
`GET two_cities` возвращает список городов с их информацией, с информацией кто севернее, с информацией об 
 временных зонах (совпадает/не совпадает), с информацией на сколько часов различаются часовые зоны.

Параметры:
* `city1` – Название первого города на русском языке
* `city2` – Название второго города на русском языке

### Пример запроса
`GET two_cities/?city1=Папушево&city2=Низинный`
### Ответ
```json

[
    {
        "geonameid": "506321", 
        "name": "Papushevo", 
        "asciiname": "Papushevo", 
        "alternatenames": "Papushevo,Papusjevo,Popushevo,Popush\u00ebvo,Prapushevo,\u041f\u0430\u043f\u0443\u0448\u0435\u0432\u043e", 
        "latitude": "54.69237", 
        "longitude": "40.87259", 
        "feature class": "P", 
        "feature code": "PPL", 
        "country code": "RU", 
        "cc2": "", 
        "admin1 code": "62", 
        "admin2 code": "", 
        "admin3 code": "", 
        "admin4 code": "", 
        "population": "0", 
        "elevation": "", 
        "dem": "95", 
        "timezone": "Europe/Moscow", 
        "modification date": "2012-01-17"
    }, 

    {
        "geonameid": "11288646", 
        "name": "Nizinnyy", 
        "asciiname": "Nizinnyy", 
        "alternatenames": "Nizinnyj,\u041d\u0438\u0437\u0438\u043d\u043d\u044b\u0439", 
        "latitude": "70.87287", 
        "longitude": "178.78944", 
        "feature class": "H", 
        "feature code": "STM", 
        "country code": "RU", 
        "cc2": "", 
        "admin1 code": "15", 
        "admin2 code": "", 
        "admin3 code": "", 
        "admin4 code": "", 
        "population": "0", 
        "elevation": "", 
        "dem": "3", 
        "timezone": "Asia/Anadyr", 
        "modification date": "2016-11-22"
    }, 

    {
      "who_north": "\u041d\u0438\u0437\u0438\u043d\u043d\u044b\u0439 \u0441\u0435\u0432\u0435\u0440\u043d\u0435\u0435 \u041f\u0430\u043f\u0443\u0448\u0435\u0432\u043e"
    }, 

    {
      "timezones": "\u041f\u0430\u043f\u0443\u0448\u0435\u0432\u043e \u0438 \u041d\u0438\u0437\u0438\u043d\u043d\u044b\u0439 \u043d\u0430\u0445\u043e\u0434\u044f\u0442\u0441\u044f \u043d\u0435 \u0432 \u043e\u0434\u043d\u043e\u0439 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439 \u0437\u043e\u043d\u0435"
    }, 

    {
      "time_difference": 9
    }
]
```
На python можно получить список json с информацией об этих двух городах следующим образом:
```python
import requests
import json

r = requests.get('http://127.0.0.1:8000/two_cities/?city1=Папушево&city2=Низинный')
geo_info3 = json.loads(r.json())
```
В переменной ```geo_info3``` будет находиться список словарей с информацией об этих двух городах:
```pythonstub
[
{'geonameid': '506321', 
'name': 'Papushevo', 
'asciiname': 'Papushevo', 
'alternatenames': 'Papushevo,Papusjevo,Popushevo,Popushëvo,Prapushevo,Папушево', 
'latitude': '54.69237', 
'longitude': '40.87259', 
'feature class': 'P', 
'feature code': 'PPL', 
'country code': 'RU', 
'cc2': '', 'admin1 code': '62', 
'admin2 code': '', 
'admin3 code': '', 
'admin4 code': '', 
'population': '0', 
'elevation': '', 
'dem': '95', 
'timezone': 'Europe/Moscow', 
'modification date': '2012-01-17'}, 

{'geonameid': '11288646', 
'name': 'Nizinnyy', 
'asciiname': 'Nizinnyy', 
'alternatenames': 'Nizinnyj,Низинный', 
'latitude': '70.87287', 
'longitude': '178.78944', 
'feature class': 'H', 
'feature code': 'STM', 
'country code': 'RU', 
'cc2': '', 
'admin1 code': '15', 
'admin2 code': '', 
'admin3 code': '', 
'admin4 code': '', 
'population': '0', 
'elevation': '', 
'dem': '3', 
'timezone': 'Asia/Anadyr', 
'modification date': '2016-11-22'}, 

{'who_north': 'Низинный севернее Папушево'}, 

{'timezones': 'Папушево и Низинный находятся не в одной временной зоне'}, 

{'time_difference': 9}
]
```

---------

## Метод принимает часть названия города и возвращает "подсказку" - список возможных вариантов продолжений  
`GET clue` возвращает список возможных вариантов продолжений части названия города name.

Параметр:
* `name` – Название первого города на русском языке


### Пример запроса
`GET clue/?name=Orl`
### Ответ
```json
["Boloto Orlovskoye", "Orlovka", "Orlovo", "Orlovka", "Orlova Luka", "Orlovo Vtoroye", "Verkhnyaya Orlyanka", "Troitse-Orlovka", "Tersko-Orlovskiy Mayak", "Sukhaya Orlitsa", "Srednyaya Orlyanka", "Rechki Orlovy", "Puyalka-Orlovo", "Proletarskiy", "Pochinok Orlovo", "Pamyatoy", "Arlyanovo", "Orlyanka", "Orlyanka", "Orlyanka", "Orlyanka", "Orlyanka", "Orlya", "Orlya", "Orly", "Orly", "Orly", "Orly", "Mys Orlov-Terskiy Tonkiy", "Mys Orlov-Terskiy Tolstyy", "Boloto Orlovskoye", "Orlovskoye", "Orlovskiy Shlyuz", "Orlovskiy Rayon", "Orlovskiy Rayon", "Orlovskiye Dvoriki", "Guba Orlovka", "Mys Orlovskiy", "Liman Bol\u2019shoy Orlinyy", "Orlovka", "Orlovskiy", "Orlovskiy", "Orlovskiy", "Karaman", "Orlovskiy", "Orlovskiy", "Orlovka", "Orlovskiy", "Orlovskiy", "Orly", "Orlovskiy", "Orlovskiy", "Orlovskiy", "Orlov", "Proliv Orlovskaya Salma", "Orel Oblast", "Orlovskaya", "Orlovskaya", "Orlovskoye", "Ozero Bol\u2019shoye Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orly", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovo Pervoye", "Orlovo", "Orlovo", "Orlovo", "Mys Orlov Navolok", "Guba Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Novaya Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Urochishche Orlovka", "Orlovka", "Urochishche Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovskiy", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Urochishche Orlovka", "Orlovka", "Orlovka", "Bol\u2019shaya Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovitsa", "Orlovik", "Orlov Gay", "Orlovets", "Orlova Dacha", "Gora Orlova", "Orlova", "Orlova", "Orlovo", "Mys Orlov", "Orlov", "Orlov", "Orlov", "Orlov", "Orlov", "Orlov", "Orlov", "Orliya Slobodka", "Orliya", "Orlitsa", "Ozero Orlinskoye", "Orlinoye Gnezdo", "Ozero Orlinoye", "Orlinovskiy", "Orlino", "Orlino", "Orlinka", "Orlinaya Shishka", "Orliki", "Orlik", "Orlik", "Orlik", "Orlik", "Orlik", "Orlik", "Orlik", "Ozero Orleya", "Orleya", "Ozero Orl\u00ebvo", "Orletsy", "Orletsy", "Orlets", "Kolkhoz Novoye Orlovo", "Novoorlovka", "Novaya Orlovka", "Nizhnyaya Orlyanka", "Nizhneye Bugayevo", "Natal\u2019yevka", "Myshinka", "Mokraya Orlovka", "Malaya Orlovka", "Malaya Orlovka", "Maloorlovskiy", "Lysovka", "Mys Letniy Orlov", "Krasnyye Orly", "Guba Konyukhova", "Verkhnyaya Orlovka", "Orlovskiy Rayon", "Orlov", "Kolkhoz Imeni Orlova", "Stantsiya Gryazi Orlovskiye", "Dmitrovsk-Orlovskiy", "Stantsiya Bryansk-Orlovskiy", "Bol\u2019shiye Orlovichi", "Bol\u2019shaya Orlovskaya Koshka", "Bol\u2019shaya Orlovka", "Bol\u2019shaya Orlovka", "Bol\u2019shaya Orlovka", "Mayak Tersko-Orlovskiy", "Banka Letne-Orlovskaya", "Orlov", "Orlov", "Ozero Bol\u2019shoye Orlovo", "Orlov", "Stantsiya Orlovka", "Gora Orlinaya", "Balka Orlinaya", "Orlovskiy", "Balka Orlova", "Orlovka", "Orlovskiy", "Orlinoye", "Orlovka", "Orlyanka", "Orlov", "Balka Orlova", "Orly", "Lipovka", "Orlovka", "Sovkhoz Orlovskiy", "Orly", "Orlovka", "Imeni Orlova", "Orlinka", "Orlino", "Orlinskoye Ozero", "Ozero Bol\u2019shoye Orlovo", "Orlovka", "Orlovka", "Urochishche Orlovka", "Orlova Shchel\u2019", "Kurgan Orlova Mogila", "Gora Orlova", "Urochishche Orlik", "Orlovskoye", "Les Orlinyy", "Urochishche Orlovskoye", "Gora Orlova", "Urochishche Orly-Saban", "Mayak Orlovskikh Koshok Severnyy", "Pionerlager\u2019 Orl\u00ebnok", "Urochishche Orlova Polyana", "Orlovka", "Urochishche Orlovskoye", "Orlovka", "Gory Orlovskiye", "Mys Orlova", "Koshek Orlovskiye", "Orlovka", "Orlovka", "Orlovka", "Ozero Orlu-Nur", "Boloto Orlovskoye Zaymishche", "Sovkhoz Orlovskiy", "Ostrov Orlovskiy", "Urochishche Orly", "Dal\u2019nyaya Orlovka", "Orlovka", "Orlovskiy", "Orlovskiy", "Orlovka", "Orlovskiy", "Orlovo-Rozovo", "Orlovo-Kukushkino", "Ozero Orlovo", "Ozero Orlovo", "Ozero Orlovo", "Orlovo", "Orlovo", "Orlovo", "Orlovka", "Orlovo", "Orlovka", "Orlovka", "Orlovka", "Urochishche Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Urochishche Orlovka", "Urochishche Orlovka", "Orlovo", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Razvaliny Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovskiy", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovik", "Orlova", "Orlova", "Orlovo", "Orlinka", "Orlik", "Orlean", "Ozero Orlovo", "Novoorlovka", "Novoorlovka", "Stantsiya Krasnyye Orly", "Letnik Sovkhoza Krasnyye Orly", "Krasnyye Orly", "Krasnyye Orly", "Krasnyye Orly", "Krasnyye Orly", "Feoktistovka", "Dubrovskiy", "Atkul\u2019", "Orlovskiy", "Ozero Orlovo", "Orlovka", "Orla", "Orlovka", "Orlovka", "Orlovka", "Urochishche Orlovka", "Ostrov Orlovskogo", "Kordon Orlinskiy", "Orlovka", "Vodokhranilishche Orlovskoye", "Urochishche Orloik", "Boloto Bol\u2019shoye Orlovo", "Boloto Maloye Orlovo", "Urochishche Orlovik", "Urochishche Orlinoye", "Ozero Orlovo", "Orlovka", "Boloto Orlovo", "Orlova", "Pionerlager\u2019 Orlenok", "Kapitana Orla", "Nizhnyaya Orlovka", "Srednyaya Orlovka", "Orlovka", "Pionerlager\u2019 Orl\u00ebnok", "Samaro-Orlovka", "Orlovskoye", "Orlovskiy", "Orlovskiy", "Orlovskiy", "Orlovskaya Kolonna", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Orlok", "Orlinyy", "Gora Orlinoye Gnezdo", "Polevoy Stan Orlinoye", "Orlinoye", "Orlinga", "Orlinga", "Gora Orlinaya", "Ozero Orlik", "Mys Malyy Orlinyy", "Stantsiya Areda", "Zaliv Orlinyy", "Mys Orlinyy", "Sopka Orlinaya", "Orlik", "Mys Orlik", "Bukhta Orlinaya", "Orlik", "Gora Orlinaya", "Gora Orlan", "Gora Orlinaya", "Skala Orlinoye Krylo", "Gora Orlinaya", "Orlinyy", "Orlovka", "Orlik", "Pravaya Orlovka", "Orlovskaya", "Orlovo", "Orlovo", "Orlovo", "Orlovka", "Orlovka", "Orlovka", "Orlovka", "Mys Orlova", "Mys Orlova", "Mys Orlova", "Mys Orlova", "Gora Orlova", "Orlova", "Orlinaya", "Orlinaya", "Orlinaya", "Mys Oria", "Argakhtakh", "Ozero Orlinoye", "Mys Orlinyy", "Gora Orlinaya", "Gora Orlanaya", "Orlovka", "Samaro-Orlovka", "Kordon Orlinka", "Orlinka", "Urochishche Orlovskiye Luga", "Orlinoye", "Ozero Orlovo", "Boloto Orlovskoye", "Orlovskiy", "Ostanovochnyy Punkt Orlovskiy", "Orlov", "Gora Orlovka", "Orlinka", "Orlinyy", "Orlovka", "Orlovsk", "Bol\u2019shaya Orlovitsa", "Orlya", "Ostanovochnyy Punkt Maloye Orlovskoye", "Maloye Orlovskoye", "Orlikha", "Gora Orlikha", "Orlikha", "Orlovka", "Ozero Orlovskoye", "Gora Orlovka", "Orlikha", "Gora Orlinaya", "Orlovskiye Dvoriki", "Gora Orlinaya Sopka", "Orlova Pad\u2019", "Orlovka", "Orlovskoye", "Orletskoye", "Orlovka", "Ostanovochnyy Punkt Orlovo", "Prud Orlov", "Orlova", "Orlovka", "Zaprudnyy", "Pionerlager\u2019 Orl\u00ebnok", "Pionerlager\u2019 Orl\u00ebnok", "Orlik", "Zimov\u2019ye Ust\u2019-Orlik", "Orlovka", "Orlovka", "Orlovskiy Peschanyy Kar\u2019yer", "Koshara Orlova", "Orlovo", "Orlovka", "Pionerlager\u2019 Orl\u00ebnok", "Or\u00ebl", "Orlovo Pervoye", "Orlovo Vtoroye", "Orlovo", "Turbaza Orlinka", "Orly", "Orlovo", "Orlovka", "Ostanovochnyy Punkt 1418 km", "Stantsiya Orlovka-Kubanskaya", "Orlovo-Kubanskiy", "Orlyanka", "Stantsiya Luzhki-Orlovskiye", "Orlovka", "Orlovka", "Orlovka", "Novoposel\u00ebnnaya Orlovka", "Urochishche Orlovka", "Orlovka", "Novaya Orlovka", "Orlovka", "Orlovo", "Krasnaya Orlovka", "Orlovka", "Orlovka", "Orlovo", "Orlovitsa", "Stantsiya Orlenok", "Orlov Pochinok", "Urochishche Orlovskiy Uchastok", "Boloto Orlovskoye", "Ozero Orlovo", "Orlovka", "Orlovskoye", "Orlovo", "Orlovka", "Orlovo Gnezdo", "Kordon Orlik", "Boloto Bol\u2019shoye Orlashkino", "Ozero Orle", "Orlikha Vtoraya", "Orlikha", "Malaya Orlikha", "Bol\u2019shaya Orlikha", "Urochishche Orly", "Orlovo", "Orlovo", "Orli", "Boloto Orlovo", "Orlovka", "Orlovskiy", "Levyy Orlovskiy", "Pravyy Orlovskiy", "Ozero Orlinoye", "Krasnyye Orly", "Orlovo-Nikol\u2019skiy", "Orlovka", "Pionerlager\u2019 Orl\u00ebnok", "Orlov", "Orlov Log", "Orlovka", "Orlovka", "Orlovka", "Orlyanovka", "Orl\u00ebnok", "Balka Orl\u00ebnok", "Orlovskiy", "Pionerlager\u2019 Orl\u00ebnok", "Ferma Sovkhoza Orlovskiy Nomer Tri", "Ferma Sovkhoza Orlovskiy Nomer Chetyre", "Koshara Sovkhoza Orlovskiy", "Ferma Sovkhoza Orlovskiy Nomer Odin", "Ferma Sovkhoza Orlovskiy Nomer Dva", "Orlovskiy Raspredelitel\u2019nyy Kanal", "Liman Orlovskiy", "Ozero Orlovo", "Orlovskiy Uval", "Prud Orlovskiy", "Orlovo", "Pad\u2019 Orlova", "Orlovskiye", "Kurgan Mogila Orlova", "Orlovtsy", "Urochishche Orlovskoye", "Pionerlager\u2019 Orl\u00ebnok", "Orlovka", "Mys Orlinyy", "Orlova", "Balka Orlinaya", "Urochishche Orlov Rodnik", "Orlova", "Orlov", "Orlingskaya Nyucha", "Orlinga", "Urochishche Krasnyye Orly", "Molochnotovarnaya Ferma Sovkhoza Krasnyye Orly", "Lager\u2019 Orl\u00ebnok", "Pionerlager\u2019 Orl\u00ebnok", "Pionerlager\u2019 Orl\u00ebnok", "Mayak Orlovskiy", "Rybnyy Stan Malyy Orlov", "Orletsy", "Ozero Orlovskoye", "Orlinyy", "Ozero Orlovo", "Ozero Orlovo", "Orly", "Orletskiy", "Izba Pod Orletsom", "Ozero Orlovskoye", "Detskiy Lager\u2019 Orl\u00ebnok", "Orlovets", "Boloto Orlovskoye", "Orlovskiy", "Orlik", "Orlovskiy", "Orlovo", "Orlok", "Orlovskiy", "Orlinoye", "Kosa Orlikha", "Orlovka Vtoraya", "Moscow Orlovo Heliport", "Vernoye Orlovka", "Ozero Maloye Orlovo", "Ozero Orlovskoye", "Urochishche Orlovo Gnyezdo", "Ozero Orlinoye", "Balka Orlov Rov", "Urochishche Orlinoye", "Balka Orlov Log", "Ozero Orlovskoye", "Balka Orlushina", "Urochishche Orlovskoye", "Orly", "Ozero Orlovo", "Ovrag Orlov Log"]
```

На python можно получить список с возможными вариантами продолжения name:
```python
import requests
import json

r = requests.get('http://127.0.0.1:8000/clue/?name=Orl')
geo_info4 = json.loads(r.json())
```
В переменной ```geo_info4``` будет находиться список с возможными вариантами продолжения:
```pythonstub
['Boloto Orlovskoye', 'Orlovka', 'Orlovo', 'Orlovka', 'Orlova Luka', 'Orlovo Vtoroye', 'Verkhnyaya Orlyanka', 'Troitse-Orlovka', 'Tersko-Orlovskiy Mayak', 'Sukhaya Orlitsa', 'Srednyaya Orlyanka', 'Rechki Orlovy', 'Puyalka-Orlovo', 'Proletarskiy', 'Pochinok Orlovo', 'Pamyatoy', 'Arlyanovo', 'Orlyanka', 'Orlyanka', 'Orlyanka', 'Orlyanka', 'Orlyanka', 'Orlya', 'Orlya', 'Orly', 'Orly', 'Orly', 'Orly', 'Mys Orlov-Terskiy Tonkiy', 'Mys Orlov-Terskiy Tolstyy', 'Boloto Orlovskoye', 'Orlovskoye', 'Orlovskiy Shlyuz', 'Orlovskiy Rayon', 'Orlovskiy Rayon', 'Orlovskiye Dvoriki', 'Guba Orlovka', 'Mys Orlovskiy', 'Liman Bol’shoy Orlinyy', 'Orlovka', 'Orlovskiy', 'Orlovskiy', 'Orlovskiy', 'Karaman', 'Orlovskiy', 'Orlovskiy', 'Orlovka', 'Orlovskiy', 'Orlovskiy', 'Orly', 'Orlovskiy', 'Orlovskiy', 'Orlovskiy', 'Orlov', 'Proliv Orlovskaya Salma', 'Orel Oblast', 'Orlovskaya', 'Orlovskaya', 'Orlovskoye', 'Ozero Bol’shoye Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orly', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovo Pervoye', 'Orlovo', 'Orlovo', 'Orlovo', 'Mys Orlov Navolok', 'Guba Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Novaya Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Urochishche Orlovka', 'Orlovka', 'Urochishche Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovskiy', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Urochishche Orlovka', 'Orlovka', 'Orlovka', 'Bol’shaya Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovitsa', 'Orlovik', 'Orlov Gay', 'Orlovets', 'Orlova Dacha', 'Gora Orlova', 'Orlova', 'Orlova', 'Orlovo', 'Mys Orlov', 'Orlov', 'Orlov', 'Orlov', 'Orlov', 'Orlov', 'Orlov', 'Orlov', 'Orliya Slobodka', 'Orliya', 'Orlitsa', 'Ozero Orlinskoye', 'Orlinoye Gnezdo', 'Ozero Orlinoye', 'Orlinovskiy', 'Orlino', 'Orlino', 'Orlinka', 'Orlinaya Shishka', 'Orliki', 'Orlik', 'Orlik', 'Orlik', 'Orlik', 'Orlik', 'Orlik', 'Orlik', 'Ozero Orleya', 'Orleya', 'Ozero Orlëvo', 'Orletsy', 'Orletsy', 'Orlets', 'Kolkhoz Novoye Orlovo', 'Novoorlovka', 'Novaya Orlovka', 'Nizhnyaya Orlyanka', 'Nizhneye Bugayevo', 'Natal’yevka', 'Myshinka', 'Mokraya Orlovka', 'Malaya Orlovka', 'Malaya Orlovka', 'Maloorlovskiy', 'Lysovka', 'Mys Letniy Orlov', 'Krasnyye Orly', 'Guba Konyukhova', 'Verkhnyaya Orlovka', 'Orlovskiy Rayon', 'Orlov', 'Kolkhoz Imeni Orlova', 'Stantsiya Gryazi Orlovskiye', 'Dmitrovsk-Orlovskiy', 'Stantsiya Bryansk-Orlovskiy', 'Bol’shiye Orlovichi', 'Bol’shaya Orlovskaya Koshka', 'Bol’shaya Orlovka', 'Bol’shaya Orlovka', 'Bol’shaya Orlovka', 'Mayak Tersko-Orlovskiy', 'Banka Letne-Orlovskaya', 'Orlov', 'Orlov', 'Ozero Bol’shoye Orlovo', 'Orlov', 'Stantsiya Orlovka', 'Gora Orlinaya', 'Balka Orlinaya', 'Orlovskiy', 'Balka Orlova', 'Orlovka', 'Orlovskiy', 'Orlinoye', 'Orlovka', 'Orlyanka', 'Orlov', 'Balka Orlova', 'Orly', 'Lipovka', 'Orlovka', 'Sovkhoz Orlovskiy', 'Orly', 'Orlovka', 'Imeni Orlova', 'Orlinka', 'Orlino', 'Orlinskoye Ozero', 'Ozero Bol’shoye Orlovo', 'Orlovka', 'Orlovka', 'Urochishche Orlovka', 'Orlova Shchel’', 'Kurgan Orlova Mogila', 'Gora Orlova', 'Urochishche Orlik', 'Orlovskoye', 'Les Orlinyy', 'Urochishche Orlovskoye', 'Gora Orlova', 'Urochishche Orly-Saban', 'Mayak Orlovskikh Koshok Severnyy', 'Pionerlager’ Orlënok', 'Urochishche Orlova Polyana', 'Orlovka', 'Urochishche Orlovskoye', 'Orlovka', 'Gory Orlovskiye', 'Mys Orlova', 'Koshek Orlovskiye', 'Orlovka', 'Orlovka', 'Orlovka', 'Ozero Orlu-Nur', 'Boloto Orlovskoye Zaymishche', 'Sovkhoz Orlovskiy', 'Ostrov Orlovskiy', 'Urochishche Orly', 'Dal’nyaya Orlovka', 'Orlovka', 'Orlovskiy', 'Orlovskiy', 'Orlovka', 'Orlovskiy', 'Orlovo-Rozovo', 'Orlovo-Kukushkino', 'Ozero Orlovo', 'Ozero Orlovo', 'Ozero Orlovo', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovka', 'Orlovo', 'Orlovka', 'Orlovka', 'Orlovka', 'Urochishche Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Urochishche Orlovka', 'Urochishche Orlovka', 'Orlovo', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Razvaliny Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovskiy', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovik', 'Orlova', 'Orlova', 'Orlovo', 'Orlinka', 'Orlik', 'Orlean', 'Ozero Orlovo', 'Novoorlovka', 'Novoorlovka', 'Stantsiya Krasnyye Orly', 'Letnik Sovkhoza Krasnyye Orly', 'Krasnyye Orly', 'Krasnyye Orly', 'Krasnyye Orly', 'Krasnyye Orly', 'Feoktistovka', 'Dubrovskiy', 'Atkul’', 'Orlovskiy', 'Ozero Orlovo', 'Orlovka', 'Orla', 'Orlovka', 'Orlovka', 'Orlovka', 'Urochishche Orlovka', 'Ostrov Orlovskogo', 'Kordon Orlinskiy', 'Orlovka', 'Vodokhranilishche Orlovskoye', 'Urochishche Orloik', 'Boloto Bol’shoye Orlovo', 'Boloto Maloye Orlovo', 'Urochishche Orlovik', 'Urochishche Orlinoye', 'Ozero Orlovo', 'Orlovka', 'Boloto Orlovo', 'Orlova', 'Pionerlager’ Orlenok', 'Kapitana Orla', 'Nizhnyaya Orlovka', 'Srednyaya Orlovka', 'Orlovka', 'Pionerlager’ Orlënok', 'Samaro-Orlovka', 'Orlovskoye', 'Orlovskiy', 'Orlovskiy', 'Orlovskiy', 'Orlovskaya Kolonna', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlok', 'Orlinyy', 'Gora Orlinoye Gnezdo', 'Polevoy Stan Orlinoye', 'Orlinoye', 'Orlinga', 'Orlinga', 'Gora Orlinaya', 'Ozero Orlik', 'Mys Malyy Orlinyy', 'Stantsiya Areda', 'Zaliv Orlinyy', 'Mys Orlinyy', 'Sopka Orlinaya', 'Orlik', 'Mys Orlik', 'Bukhta Orlinaya', 'Orlik', 'Gora Orlinaya', 'Gora Orlan', 'Gora Orlinaya', 'Skala Orlinoye Krylo', 'Gora Orlinaya', 'Orlinyy', 'Orlovka', 'Orlik', 'Pravaya Orlovka', 'Orlovskaya', 'Orlovo', 'Orlovo', 'Orlovo', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlovka', 'Mys Orlova', 'Mys Orlova', 'Mys Orlova', 'Mys Orlova', 'Gora Orlova', 'Orlova', 'Orlinaya', 'Orlinaya', 'Orlinaya', 'Mys Oria', 'Argakhtakh', 'Ozero Orlinoye', 'Mys Orlinyy', 'Gora Orlinaya', 'Gora Orlanaya', 'Orlovka', 'Samaro-Orlovka', 'Kordon Orlinka', 'Orlinka', 'Urochishche Orlovskiye Luga', 'Orlinoye', 'Ozero Orlovo', 'Boloto Orlovskoye', 'Orlovskiy', 'Ostanovochnyy Punkt Orlovskiy', 'Orlov', 'Gora Orlovka', 'Orlinka', 'Orlinyy', 'Orlovka', 'Orlovsk', 'Bol’shaya Orlovitsa', 'Orlya', 'Ostanovochnyy Punkt Maloye Orlovskoye', 'Maloye Orlovskoye', 'Orlikha', 'Gora Orlikha', 'Orlikha', 'Orlovka', 'Ozero Orlovskoye', 'Gora Orlovka', 'Orlikha', 'Gora Orlinaya', 'Orlovskiye Dvoriki', 'Gora Orlinaya Sopka', 'Orlova Pad’', 'Orlovka', 'Orlovskoye', 'Orletskoye', 'Orlovka', 'Ostanovochnyy Punkt Orlovo', 'Prud Orlov', 'Orlova', 'Orlovka', 'Zaprudnyy', 'Pionerlager’ Orlënok', 'Pionerlager’ Orlënok', 'Orlik', 'Zimov’ye Ust’-Orlik', 'Orlovka', 'Orlovka', 'Orlovskiy Peschanyy Kar’yer', 'Koshara Orlova', 'Orlovo', 'Orlovka', 'Pionerlager’ Orlënok', 'Orël', 'Orlovo Pervoye', 'Orlovo Vtoroye', 'Orlovo', 'Turbaza Orlinka', 'Orly', 'Orlovo', 'Orlovka', 'Ostanovochnyy Punkt 1418 km', 'Stantsiya Orlovka-Kubanskaya', 'Orlovo-Kubanskiy', 'Orlyanka', 'Stantsiya Luzhki-Orlovskiye', 'Orlovka', 'Orlovka', 'Orlovka', 'Novoposelënnaya Orlovka', 'Urochishche Orlovka', 'Orlovka', 'Novaya Orlovka', 'Orlovka', 'Orlovo', 'Krasnaya Orlovka', 'Orlovka', 'Orlovka', 'Orlovo', 'Orlovitsa', 'Stantsiya Orlenok', 'Orlov Pochinok', 'Urochishche Orlovskiy Uchastok', 'Boloto Orlovskoye', 'Ozero Orlovo', 'Orlovka', 'Orlovskoye', 'Orlovo', 'Orlovka', 'Orlovo Gnezdo', 'Kordon Orlik', 'Boloto Bol’shoye Orlashkino', 'Ozero Orle', 'Orlikha Vtoraya', 'Orlikha', 'Malaya Orlikha', 'Bol’shaya Orlikha', 'Urochishche Orly', 'Orlovo', 'Orlovo', 'Orli', 'Boloto Orlovo', 'Orlovka', 'Orlovskiy', 'Levyy Orlovskiy', 'Pravyy Orlovskiy', 'Ozero Orlinoye', 'Krasnyye Orly', 'Orlovo-Nikol’skiy', 'Orlovka', 'Pionerlager’ Orlënok', 'Orlov', 'Orlov Log', 'Orlovka', 'Orlovka', 'Orlovka', 'Orlyanovka', 'Orlënok', 'Balka Orlënok', 'Orlovskiy', 'Pionerlager’ Orlënok', 'Ferma Sovkhoza Orlovskiy Nomer Tri', 'Ferma Sovkhoza Orlovskiy Nomer Chetyre', 'Koshara Sovkhoza Orlovskiy', 'Ferma Sovkhoza Orlovskiy Nomer Odin', 'Ferma Sovkhoza Orlovskiy Nomer Dva', 'Orlovskiy Raspredelitel’nyy Kanal', 'Liman Orlovskiy', 'Ozero Orlovo', 'Orlovskiy Uval', 'Prud Orlovskiy', 'Orlovo', 'Pad’ Orlova', 'Orlovskiye', 'Kurgan Mogila Orlova', 'Orlovtsy', 'Urochishche Orlovskoye', 'Pionerlager’ Orlënok', 'Orlovka', 'Mys Orlinyy', 'Orlova', 'Balka Orlinaya', 'Urochishche Orlov Rodnik', 'Orlova', 'Orlov', 'Orlingskaya Nyucha', 'Orlinga', 'Urochishche Krasnyye Orly', 'Molochnotovarnaya Ferma Sovkhoza Krasnyye Orly', 'Lager’ Orlënok', 'Pionerlager’ Orlënok', 'Pionerlager’ Orlënok', 'Mayak Orlovskiy', 'Rybnyy Stan Malyy Orlov', 'Orletsy', 'Ozero Orlovskoye', 'Orlinyy', 'Ozero Orlovo', 'Ozero Orlovo', 'Orly', 'Orletskiy', 'Izba Pod Orletsom', 'Ozero Orlovskoye', 'Detskiy Lager’ Orlënok', 'Orlovets', 'Boloto Orlovskoye', 'Orlovskiy', 'Orlik', 'Orlovskiy', 'Orlovo', 'Orlok', 'Orlovskiy', 'Orlinoye', 'Kosa Orlikha', 'Orlovka Vtoraya', 'Moscow Orlovo Heliport', 'Vernoye Orlovka', 'Ozero Maloye Orlovo', 'Ozero Orlovskoye', 'Urochishche Orlovo Gnyezdo', 'Ozero Orlinoye', 'Balka Orlov Rov', 'Urochishche Orlinoye', 'Balka Orlov Log', 'Ozero Orlovskoye', 'Balka Orlushina', 'Urochishche Orlovskoye', 'Orly', 'Ozero Orlovo', 'Ovrag Orlov Log']
```
