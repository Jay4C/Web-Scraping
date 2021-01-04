import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest
import warnings


class UnitTestsDataMinerYellowPagesEspagne(unittest.TestCase):
    def test_extract_one_email(self):
        try:
            url = "https://www.paginasamarillas.es/f/alicante-alacant/oro-aguilera_226089316_000000001.html"

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            # Request the content of a page from the url
            html = requests.get(url, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            print(html.content)

            if soup.find("a", {"data-omniclick": "website"}) is not None:
                email = "info@" + soup \
                    .find("a", {"data-omniclick": "website"}) \
                    .get("href") \
                    .split("?")[0] \
                    .replace("http://www.", "") \
                    .replace("https://www.", "") \
                    .replace("http://", "") \
                    .replace("https://", "")

                print("email : " + str(email))
            else:
                print("no email business")
        except Exception as e:
            print("error : " + str(e))

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        try:
            activity = "hotel"
            city = "madrid"
            url_search = "https://www.paginasamarillas.es/search/alojamientos/all-ma/" \
                         + city + "/all-is/" \
                         + city + "/all-ba/all-pu/all-nc/" \
                         + activity + "/all-ct/1?what=" \
                         + activity + "&where=" \
                         + city + "&ub=ubicado"
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            html_search = requests.get(url_search, headers=headers)

            soup_search = BeautifulSoup(html_search.content, 'html.parser')

            number_of_pages = 0

            try:
                if soup_search\
                        .find("", {"class": "bloque-central"})\
                        .find("div", {"class": "negocio"})\
                        .find("div", {"class": "box"})\
                        .find("span", {"class": "h1"}) is not None:

                    number_of_pages_with_coma = int(soup_search
                                                    .find("", {"class": "bloque-central"})
                                                    .find("div", {"class": "negocio"})
                                                    .find("div", {"class": "box"})
                                                    .find("span", {"class": "h1"})
                                                    .text
                                                    .replace("(", "")
                                                    .replace(")", "")
                                                    .replace(".", "")
                                                    .replace(",", "")
                                                    ) / 30

                    if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                        number_of_pages += round(number_of_pages_with_coma) + 1
                        print('number_of_pages : ' + str(number_of_pages))

                    elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                        number_of_pages += round(number_of_pages_with_coma)
                        print('number_of_pages : ' + str(number_of_pages))

                    i_1 = 0

                    for i in range(1, number_of_pages + 1):
                        url_of_one_page_of_results = "https://www.paginasamarillas.es/search/alojamientos/all-ma/" \
                                                     + city + "/all-is/" \
                                                     + city + "/all-ba/all-pu/all-nc/" \
                                                     + activity + "/all-ct/" + str(i) + "?what=" \
                                                     + activity + "&where=" \
                                                     + city + "&ub=ubicado"
                        print(url_of_one_page_of_results)

                        time.sleep(2)

                        html_of_one_page_of_results = requests.get(url_of_one_page_of_results, headers=headers)

                        soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                        if soup_of_one_page_of_results\
                                .find("div", {"class": "central"})\
                                .find("div", {"class": "listado-item"}) is not None:
                            for result_item in soup_of_one_page_of_results\
                                    .find("div", {"class": "central"})\
                                    .find_all("div", {"class": "listado-item"}):
                                i_1 += 1

                                if result_item\
                                        .find("div", {"class": "box"})\
                                        .find("div", {"class": "cabecera"})\
                                        .find("div", {"class": "row"})\
                                        .find("div", {"class": "comercial-nombre"})\
                                        .find("a", {"data-omniclick": "name"}):
                                    url_result = result_item\
                                        .find("div", {"class": "box"})\
                                        .find("div", {"class": "cabecera"})\
                                        .find("div", {"class": "row"})\
                                        .find("div", {"class": "comercial-nombre"})\
                                        .find("a", {"data-omniclick": "name"})\
                                        .get("href")

                                    try:
                                        # Request the content of a page from the url
                                        html = requests.get(url_result, headers=headers)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        if soup.find("a", {"data-omniclick": "website"}) is not None:
                                            email = "info@" + soup \
                                                .find("a", {"data-omniclick": "website"}) \
                                                .get("href") \
                                                .split("?")[0] \
                                                .replace("http://www.", "") \
                                                .replace("https://www.", "") \
                                                .replace("http://", "") \
                                                .replace("https://", "") \
                                                .replace("/", "")

                                            print(str(i_1) + " email : " + str(email))
                                        else:
                                            print("no email business")
                                    except Exception as e:
                                        print("error 1 : " + str(e))
                        else:
                            print('sorry there is no results')
                else:
                    print("no pages at all")
            except Exception as e:
                print("error 2 : " + str(e))
        except Exception as e:
            print(str(e))

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        """
        {'id': '1', 'what': 'interina', 'block_of_activity': 'interina', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '2', 'what': 'agente+inmobiliario', 'block_of_activity': 'agente-inmobiliario', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '3', 'what': 'reclutador', 'block_of_activity': 'recaudador', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '4', 'what': 'software', 'block_of_activity': 'software', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '5', 'what': 'hotel', 'block_of_activity': 'alojamientos', 'url_activite': '/all-ba/all-pu/all-nc/hotel/all-ct'},
        {'id': '6', 'what': 'arrendadora', 'block_of_activity': 'all-ac', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '7', 'what': 'limpieza', 'block_of_activity': 'limpieza', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '8', 'what': 'asociación', 'block_of_activity': 'asociacion', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '9', 'what': 'financiero', 'block_of_activity': 'financiero', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '10', 'what': 'restaurante', 'block_of_activity': 'restaurantes', 'url_activite': '/all-ba/all-pu/all-nc/all-co'},
        {'id': '11', 'what': 'Edificio', 'block_of_activity': 'edificio', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '12', 'what': 'peluquero', 'block_of_activity': 'peluquero', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '13', 'what': 'florista', 'block_of_activity': 'florista', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '14', 'what': 'cerrajero', 'block_of_activity': 'cerrajero', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '15', 'what': 'panaderia', 'block_of_activity': 'panaderia', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '16', 'what': 'seguro', 'block_of_activity': 'seguro', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '17', 'what': 'farmacia', 'block_of_activity': 'farmacia', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '18', 'what': 'mover', 'block_of_activity': 'mover', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '19', 'what': 'electricidad', 'block_of_activity': 'electricidad', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '20', 'what': 'fontaneria', 'block_of_activity': 'fontaneria', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '21', 'what': 'seguridad', 'block_of_activity': 'seguridad', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '22', 'what': 'abogado', 'block_of_activity': 'abogado', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '23', 'what': 'banco', 'block_of_activity': 'banco', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '24', 'what': 'garaje', 'block_of_activity': 'garaje', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '25', 'what': 'dentista', 'block_of_activity': 'dentista', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '26', 'what': 'doctor', 'block_of_activity': 'doctor', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '27', 'what': 'contador', 'block_of_activity': 'contador', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '28', 'what': 'supermercado', 'block_of_activity': 'supermercado', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '29', 'what': 'notario', 'block_of_activity': 'notario', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '30', 'what': 'joyero', 'block_of_activity': 'joyero', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '31', 'what': 'diseño+de+moda', 'block_of_activity': 'diseño-de-moda', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '32', 'what': 'carnicero', 'block_of_activity': 'carnicero', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '33', 'what': 'librería', 'block_of_activity': 'libreria', 'url_activite': '/all-ba/all-pu/all-nc'},
        {'id': '34', 'what': 'arquitecto', 'block_of_activity': 'arquitecto', 'url_activite': '/all-ba/all-pu/all-nc'},
        """

        activites = [
            {'id': '36', 'what': 'cemento', 'block_of_activity': 'cemento', 'url_activite': '/all-ba/all-pu/all-nc'},
            {'id': '37', 'what': 'calefacciones', 'block_of_activity': 'calefacciones', 'url_activite': '/all-ba/all-pu/all-nc'},
            {'id': '38', 'what': 'barco', 'block_of_activity': 'barco', 'url_activite': '/all-ba/all-pu/all-nc'},
            {'id': '39', 'what': 'frio', 'block_of_activity': 'frio', 'url_activite': '/all-ba/all-pu/all-nc'},
            {'id': '41', 'what': 'acero', 'block_of_activity': 'acero', 'url_activite': '/all-ba/all-pu/all-nc'},
            {'id': '42', 'what': 'quimica', 'block_of_activity': 'quimica', 'url_activite': '/all-ba/all-pu/all-nc'},
            {'id': '43', 'what': 'gas', 'block_of_activity': 'gas', 'url_activite': '/all-ba/all-pu/all-nc'},
            {'id': '44', 'what': 'compro-oro-y-plata', 'block_of_activity': 'compro-oro-y-plata', 'url_activite': '/all-ba/all-pu/all-nc'}
        ]

        capitales_du_monde = [
            {'id': '280', 'all_ma': 'alicante', 'all_is': 'alicante', 'where': 'alicante&ub=false&qc=true'},# alicante
            {'id': '281', 'all_ma': 'albacete', 'all_is': 'albacete', 'where': 'albacete&ub=false&qc=true'},# albacete
            {'id': '282', 'all_ma': 'almeria', 'all_is': 'almeria', 'where': 'almeria&ub=false&qc=true'},# almeria
            {'id': '283', 'all_ma': 'avila', 'all_is': 'avila', 'where': 'avila&ub=false&qc=true'},# avila
            {'id': '284', 'all_ma': 'barcelona', 'all_is': 'barcelona', 'where': 'barcelona&ub=false&qc=true'},# barcelona
            {'id': '285', 'all_ma': 'badajoz', 'all_is': 'merida', 'where': 'merida&ub=false&qc=true'},# merida
            {'id': '286', 'all_ma': 'bizkaia', 'all_is': 'bilbao', 'where': 'bilbao&ub=false&qc=true'},# bilbao
            {'id': '287', 'all_ma': 'burgos', 'all_is': 'burgos', 'where': 'burgos&ub=false&qc=true'},# burgos
            {'id': '288', 'all_ma': 'a-coruña', 'all_is': 'santiago-de-compostela', 'where': 'santiago&ub=false&hl=SANTIAGO&qc=true'},# santiago-de-compostela
            {'id': '289', 'all_ma': 'cadiz', 'all_is': 'cadiz', 'where': 'cadiz&ub=false&qc=true'},# cadiz
            {'id': '290', 'all_ma': 'caceres', 'all_is': 'caceres', 'where': 'caceres&ub=false&qc=true'},# caceres
            {'id': '291', 'all_ma': 'cordoba', 'all_is': 'cordoba', 'where': 'cordoba&ub=false&qc=true'},# cordoba
            {'id': '292', 'all_ma': 'ciudad-real', 'all_is': 'ciudad-real', 'where': 'ciudad+real&ub=false&qc=true'},# ciudad-real
            {'id': '293', 'all_ma': 'castellon', 'all_is': 'castello-de-la-plana', 'where': 'castello+de+la+plana&ub=false&qc=true'},# castello-de-la-plana
            {'id': '294', 'all_ma': 'all-pr', 'all_is': 'cuenca', 'where': 'cuenca&ub=false&pc=Cuenca%26jaen%26soria%26cordoba&qc=true'},# cuenca
            {'id': '295', 'all_ma': 'las-palmas', 'all_is': 'las-palmas', 'where': 'las+palmas&ub=false&qc=true'},# las-palmas
            {'id': '296', 'all_ma': 'girona', 'all_is': 'girona', 'where': 'girona&ub=false&qc=true'},# girona
            {'id': '297', 'all_ma': 'granada', 'all_is': 'granada', 'where': 'granada&ub=false&qc=true'},# granada
            {'id': '298', 'all_ma': 'guadalajara', 'all_is': 'guadalajara', 'where': 'guadalajara&ub=false&qc=true'},# guadalajara
            {'id': '299', 'all_ma': 'huelva', 'all_is': 'huelva', 'where': 'huelva&ub=false&qc=true'},# huelva
            {'id': '300', 'all_ma': 'huesca', 'all_is': 'huesca', 'where': 'huesca&ub=false&qc=true'},# huesca
            {'id': '301', 'all_ma': 'jaen', 'all_is': 'jaen', 'where': 'jaen&ub=false&qc=true'},# jaen
            {'id': '302', 'all_ma': 'lleida', 'all_is': 'lleida', 'where': 'lleida&ub=false&qc=true'},# lleida
            {'id': '303', 'all_ma': 'all-pr', 'all_is': 'leon', 'where': 'leon&ub=false&pc=A+Coruña%26leon%26lugo&qc=true'},# leon
            {'id': '304', 'all_ma': 'la-rioja', 'all_is': 'logroño', 'where': 'logroño&ub=false&qc=true'},# logroño
            {'id': '305', 'all_ma': 'lugo', 'all_is': 'lugo', 'where': 'lugo&ub=false&qc=true'},# lugo
            {'id': '306', 'all_ma': 'madrid', 'all_is': 'madrid', 'where': 'madrid&ub=false&qc=true'},# madrid
            {'id': '307', 'all_ma': 'malaga', 'all_is': 'malaga', 'where': 'malaga&ub=false&qc=true'},# malaga
            {'id': '308', 'all_ma': 'murcia', 'all_is': 'murcia', 'where': 'murcia&ub=false&qc=true'},# murcia
            {'id': '309', 'all_ma': 'navarra', 'all_is': 'pamplona', 'where': 'pamplona&ub=false&qc=true'},# pamplona
            {'id': '310', 'all_ma': 'asturias', 'all_is': 'oviedo', 'where': 'oviedo&ub=false&qc=true'},# oviedo
            {'id': '311', 'all_ma': 'ourense', 'all_is': 'ourense', 'where': 'ourense&ub=false&qc=true'},# ourense
            {'id': '312', 'all_ma': 'palencia', 'all_is': 'palencia', 'where': 'palencia&ub=false&qc=true'},# palencia
            {'id': '313', 'all_ma': 'illes-balears', 'all_is': 'palma-de-mallorca', 'where': 'palma+de+mallorca&ub=false&qc=true'},# palma-de-mallorca
            {'id': '314', 'all_ma': 'all-pr', 'all_is': 'pontevedra', 'where': 'pontevedra&ub=false&pc=A+Coruña%26pontevedra&qc=true'},# pontevedra
            {'id': '315', 'all_ma': 'cantabria', 'all_is': 'santander', 'where': 'santander&ub=false&qc=true'},# santander
            {'id': '316', 'all_ma': 'salamanca', 'all_is': 'salamanca', 'where': 'salamanca&ub=false&qc=true'},# salamanca
            {'id': '317', 'all_ma': 'sevilla', 'all_is': 'sevilla', 'where': 'sevilla&ub=false&qc=true'},# sevilla
            {'id': '318', 'all_ma': 'all-pr', 'all_is': 'segovia', 'where': 'segovia&ub=false&pc=Lugo%26segovia&qc=true'},# segovia
            {'id': '319', 'all_ma': 'all-pr', 'all_is': 'soria', 'where': 'soria&ub=false&pc=Las+Palmas%26soria&qc=true'},# soria
            {'id': '320', 'all_ma': 'gipuzkoa', 'all_is': 'donostia-san-sebastian', 'where': 'donostia+san+sebastian&ub=false&qc=true'},# donostia-san-sebastian
            {'id': '321', 'all_ma': 'tarragona', 'all_is': 'tarragona', 'where': 'tarragona&ub=false&qc=true'},# tarragona
            {'id': '322', 'all_ma': 'teruel', 'all_is': 'teruel', 'where': 'teruel&ub=false&qc=true'},# teruel
            {'id': '323', 'all_ma': 'santa-cruz-de-tenerife', 'all_is': 'santa-cruz-de-tenerife', 'where': 'santa+cruz+de+tenerife&ub=false&qc=true'},# santa-cruz-de-tenerife
            {'id': '324', 'all_ma': 'toledo', 'all_is': 'toledo', 'where': 'toledo&ub=false&qc=true'},# toledo
            {'id': '325', 'all_ma': 'valencia', 'all_is': 'valencia', 'where': 'valencia&ub=false&qc=true'},# valencia
            {'id': '326', 'all_ma': 'valladolid', 'all_is': 'valladolid', 'where': 'valladolid&ub=false&qc=true'},# valladolid
            {'id': '327', 'all_ma': 'araba', 'all_is': 'gasteiz', 'where': 'gasteiz&ub=false&qc=true'},# gasteiz
            {'id': '328', 'all_ma': 'zaragoza', 'all_is': 'zaragoza', 'where': 'zaragoza&ub=false&qc=true'},# zaragoza
            {'id': '329', 'all_ma': 'all-pr', 'all_is': 'zamora', 'where': 'zamora&ub=false&pc=Las+Palmas%26zamora&qc=true'}# zamora
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        try:
                            what = activite.get("what")
                            url_activite = activite.get("url_activite")
                            block_of_activity = activite.get("block_of_activity")

                            all_ma = capitale.get("all_ma")
                            all_is = capitale.get("all_is")
                            where = capitale.get("where")

                            url_search = "https://www.paginasamarillas.es/search/" + block_of_activity \
                                         + "/all-ma/" + all_ma \
                                         + "/all-is/" + all_is \
                                         + url_activite \
                                         + "/1?what=" + what \
                                         + "&where=" + where

                            time.sleep(5)

                            headers = {
                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                            }

                            html_search = requests.get(url_search, headers=headers)

                            soup_search = BeautifulSoup(html_search.content, 'html.parser')

                            number_of_pages = 0

                            try:
                                if soup_search \
                                        .find("div", {"class": "bloque-central"}) \
                                        .find("div", {"class": "negocio"}) \
                                        .find("div", {"class": "box"}) \
                                        .find("span", {"class": "h1"}) is not None:

                                    number_of_pages_with_coma = int(soup_search
                                                                    .find("", {"class": "bloque-central"})
                                                                    .find("div", {"class": "negocio"})
                                                                    .find("div", {"class": "box"})
                                                                    .find("span", {"class": "h1"})
                                                                    .text
                                                                    .replace("(", "")
                                                                    .replace(")", "")
                                                                    .replace(".", "")
                                                                    .replace(",", "")
                                                                    ) / 30

                                    if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                        number_of_pages += round(number_of_pages_with_coma) + 1
                                        print('number_of_pages : ' + str(number_of_pages))

                                    elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                        number_of_pages += round(number_of_pages_with_coma)
                                        print('number_of_pages : ' + str(number_of_pages))

                                    i_1 = 0

                                    for i in range(1, number_of_pages + 1):
                                        url_of_one_page_of_results = "https://www.paginasamarillas.es/search/" \
                                                                     + block_of_activity \
                                                                     + "/all-ma/" + all_ma \
                                                                     + "/all-is/" + all_is \
                                                                     + url_activite \
                                                                     + "/" + str(i) + "?what=" + what \
                                                                     + "&where=" + where

                                        print(url_of_one_page_of_results)

                                        time.sleep(5)

                                        html_of_one_page_of_results = requests.get(url_of_one_page_of_results, headers=headers)

                                        soup_of_one_page_of_results = BeautifulSoup(
                                            html_of_one_page_of_results.content,
                                            'html.parser')

                                        if soup_of_one_page_of_results \
                                                .find("div", {"class": "central"}) \
                                                .find("div", {"class": "listado-item"}) is not None:
                                            for result_item in soup_of_one_page_of_results \
                                                    .find("div", {"class": "central"}) \
                                                    .find_all("div", {"class": "listado-item"}):
                                                i_1 += 1

                                                if result_item \
                                                        .find("div", {"class": "box"}) \
                                                        .find("div", {"class": "cabecera"}) \
                                                        .find("div", {"class": "row"}) \
                                                        .find("div", {"class": "comercial-nombre"}) \
                                                        .find("a", {"data-omniclick": "name"}):
                                                    url_result = result_item \
                                                        .find("div", {"class": "box"}) \
                                                        .find("div", {"class": "cabecera"}) \
                                                        .find("div", {"class": "row"}) \
                                                        .find("div", {"class": "comercial-nombre"}) \
                                                        .find("a", {"data-omniclick": "name"}) \
                                                        .get("href")

                                                    try:
                                                        time.sleep(5)

                                                        # Request the content of a page from the url
                                                        html = requests.get(url_result, headers=headers)

                                                        # Parse the content of html_doc
                                                        soup = BeautifulSoup(html.content, 'html.parser')

                                                        if soup.find("a", {"data-omniclick": "website"}) is not None:
                                                            email = "info@" + soup \
                                                                .find("a", {"data-omniclick": "website"}) \
                                                                .get("href") \
                                                                .split("?")[0] \
                                                                .replace("http://www.", "") \
                                                                .replace("https://www.", "") \
                                                                .replace("http://", "") \
                                                                .replace("https://", "") \
                                                                .replace("/", "")

                                                            try:
                                                                connection = pymysql.connect(
                                                                    host='localhost',
                                                                    port=3306,
                                                                    user='',
                                                                    password='',
                                                                    db='contacts_professionnels',
                                                                    charset='utf8mb4',
                                                                    cursorclass=pymysql.cursors.DictCursor
                                                                )

                                                                with connection.cursor() as cursor:
                                                                    try:
                                                                        sql = "INSERT INTO `emails` (" \
                                                                              "`id_activite`, " \
                                                                              "`id_capitale_du_monde`, " \
                                                                              "`email`) VALUE (%s, %s, %s)"
                                                                        cursor.execute(sql, (
                                                                            activite.get('id'),
                                                                            capitale.get('id'),
                                                                            email))
                                                                        connection.commit()
                                                                        print(str(
                                                                            i_1) + " The record is stored : "
                                                                              + str(email))
                                                                        connection.close()
                                                                    except Exception as e:
                                                                        print(str(i_1)
                                                                              + " The record already exists : "
                                                                              + str(email) + " _ "
                                                                              + str(e))
                                                                        connection.close()
                                                            except Exception as e:
                                                                print(str(i_1) + " An error with the email : "
                                                                      + email
                                                                      + str(e))
                                                        else:
                                                            print(str(i_1) + " no email business")
                                                    except Exception as e:
                                                        print("error result_item : " + str(e))
                                        else:
                                            print('sorry there is no results')
                                else:
                                    print("no pages at all")
                            except Exception as e:
                                print("error .find('', {'class': 'bloque-central'}) : " + str(e))
                        except Exception as e:
                            print("error capitale and activity : " + str(e))
                    except Exception as e:
                        print("there is an error connection at url : " + str(e))
        finally:
            print('done')


if __name__ == '__main__':
    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
    unittest.main()
