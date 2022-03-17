from list_and_dict import key_names, timezones


def geo_to_info(geonameid):
    """
    Функция принимает параметр geonameid (int) и возвращает информацию по этому географическому объекту в форме json,
    если информация есть в файле RU.txt. Если информации нет, возвращает '{"response":"error"}'.

    Для работы необходим файл RU.txt.

    :param geonameid:integer id of record in geonames database (int)

    :return:json information about geoname (str)
    """
    f = open('RU.txt', 'r', encoding='utf-8')  # читаем файл RU.txt
    for line in f:
        line1 = line.strip().split('\t')       # из каждой строки файла делаем список
        if geonameid == line1[0]:              # если geoname id совпадает, то

            geo_info = dict(zip(key_names, line1))
            f.close()
            return geo_info
    f.close()
    return {'response': 'error'}


def page_to_list(page, numb):
    """
    Функция принимает параметры page (int) - номер страницы, numb (int) - количество отображаемых на странице городов.
    Выводит такую страницу в виде списка json (str). Если страницы не существует, выводим сообщение об ошибке
    в виде json (str).

    :param page: number of page (int)
    :param numb: number of geographical points on 1 page (int)
    :return: json list with information about geographical points (str)
    """
    f = open('RU.txt', 'r', encoding='utf-8')       # читаем файл RU.txt
    dd = [line.strip().split('\t') for line in f]   # делаем список списков, список информации о городах в виде списков
    f.close()
    j = [dict(zip(key_names, cit_inf)) for cit_inf in dd]
    # делаем список словарей, список информации о городах в виде словарей

    if page == len(j)//numb + 1:                   # для последней страницы
        listik = j[-1:-1-len(j) % numb:-1]         # здесь можно в одну строку j[-1-len(j):-1]
        listik.reverse()
        return {"response": listik}

    elif page <= len(j)//numb:                             # для непоследних страниц
        listik = j[(page * numb - numb): (page * numb)]

        return {"response": listik}
    elif page > len(j)//numb + 1:                          # если такой страницы не существует, выводим json об ошибке
        return {"response": "error"}


def name_to_city(name):
    """
    Функция принимает на вход название города на русском языке (str), возвращает список информации о
    городе с таким названием с наибольшим населением (list).

    :param name: name of geographical point (str)
    :return: information about geographical point (list)
    """
    f = open('RU.txt', 'r', encoding='utf-8')         # читаем файл RU.txt
    dd = [line.strip().split('\t') for line in f]   # делаем список списков, список информации о городах в виде списков
    f.close()
    cities = []                                     # пустой список для занесения в него городов с названием name
    for city in dd:                # цикл для поиска городов с названием name
        if name == city[3]:
            cities.append(city)
    big_city = cities[0]
    for city2 in cities:         # цикл для определения города с наибольшим населением
        if int(big_city[14]) < int(city2[14]):
            big_city = city2

    return big_city


def two_city_to_who_north(city1, city2):
    """
    Функция принимает параметры city1 и city2 - названия городов на русском языке (str), возвращает информацию о том,
    какой из городов находится севернее, или о том, что города находятся на одной широте (str).

    :param city1: name of geographical point (str)
    :param city2: name of geographical point (str)
    :return: information about which of the cities is located to the north (str)
    """
    city1_l = name_to_city(city1)
    city2_l = name_to_city(city2)
    result = ''
    if float(city1_l[4]) > float(city2_l[4]):
        result = f'{city1} севернее {city2}'
    elif float(city1_l[4]) < float(city2_l[4]):
        result = f'{city2} севернее {city1}'
    elif float(city1_l[4]) == float(city2_l[4]):
        result = f'{city1} и {city2} на одной широте'
    return result


def two_city_to_same_timezone(city1, city2):
    """
    Функция принимает параметры city1 и city2 - названия городов на русском языке (str), возвращает информацию о том,
    находятся ли города в одной временной зоне (str).

    :param city1: name of geographical point (str)
    :param city2: name of geographical point (str)
    :return: information about time zones of cities (str)
    """
    city1_l = name_to_city(city1)
    city2_l = name_to_city(city2)
    result = ''
    if city1_l[17] == city2_l[17]:
        result = f'{city1} и {city2} находятся в одной временной зоне GMT +{timezones[city1_l[17]]}'
    elif city1_l[17] != city2_l[17]:
        result = f'{city1} и {city2} находятся не в одной временной зоне'
    return result


def two_city(city1, city2):
    """
    Функция принимает параметры city1 и city2 - названия городов на русском языке (str), возвращает json с различной
    информацией: какой из городов находится севернее (или они на одной широте), находятся ли города в одной временной
    зоне, разница между временными зонами городов (str).

    :param city1: name of geographical point (str)
    :param city2: name of geographical point (str)
    :return: json list with information about: cities, which of the cities is located to the north, time zones of
    cities and time zones difference (str)
    """
    city1_l = name_to_city(city1)
    city2_l = name_to_city(city2)
    city1_d = dict(zip(key_names, city1_l))
    city2_d = dict(zip(key_names, city2_l))
    return {"response": [city1_d, city2_d, {"who_north": two_city_to_who_north(city1, city2)},
                                           {"timezones": two_city_to_same_timezone(city1, city2)},
                                           {"time_difference": abs(timezones[city1_l[17]]-timezones[city2_l[17]])}]}


def piece_of_name_to_variants(name):
    """
    Функция принимает параметр name - часть названия на русском или английском языке (str), возвращает "подсказку" -
    json список названий соответствующих name.
    :param name: name of geographical point (str)
    :return: json list names of cities (str)
    """
    f = open('RU.txt', 'r', encoding='utf-8')
    dd = [line.strip().split('\t') for line in f]
    f.close()
    cities = []
    for city in dd:
        if name in city[3]:
            cities.append(city[1])

    return {"response": cities}
