from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesArgentina(unittest.TestCase):
    def test_extract_email_from_one_result(self):
        print("test_extract_email_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.paginasamarillas.com.ar/fichas/hotel-grand-hotel_16370207/"

        time.sleep(3)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#Web") is not None:
            email = "info@" + soup \
                .select_one("#Web") \
                .get("href") \
                .replace('www.', '') \
                .replace("https://", "") \
                .replace("http://", "")

            print("email : " + email)
        else:
            print("no email business")

    def test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.paginasamarillas.com.ar/buscar/catamarca/q/hotel/p-2/?tieneCobertura=true"

        time.sleep(2)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {'class': 'companyName'}) is not None:
            all_a = soup.find_all("a", {'class': 'companyName'})

            for a in all_a:
                url = a.get('href')

                time.sleep(2)

                # Request the content of a page from the url
                html = requests.get(url, headers=headers)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.select_one("#Web") is not None:
                    email = "info@" + soup \
                        .select_one("#Web") \
                        .get("href") \
                        .lower() \
                        .replace('www.', '') \
                        .replace("https://", "") \
                        .replace("http://", "") \
                        .split("/")[0]

                    print("email : " + email)
                else:
                    print("no email business")
        else:
            print("no a class companyName")

    def test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activity = "hotel"

        city = "catamarca"

        number_of_pages = 0

        url_page = "https://www.paginasamarillas.com.ar/buscar/" + city + "/q/" + activity + "/"

        time.sleep(2)

        html_search = requests.get(url_page, headers=headers)

        soup_search = BeautifulSoup(html_search.content, 'html.parser')

        if soup_search.find("h1", {"class": "light"}) is not None:
            number_of_pages_with_coma = int(soup_search.find("h1", {"class": "light"})
                                            .text
                                            .split("|")[1]
                                            .replace(" ", "")
                                            .replace("resultados", "")
                                            ) / 17

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print("error pages")

        i_1 = 0

        if number_of_pages > 1:
            for i in range(1, number_of_pages + 1):
                url = url_page + "p-" + str(i) + "/?tieneCobertura=true"

                print(url)

                time.sleep(2)

                # Request the content of a page from the url
                html = requests.get(url, headers=headers)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("a", {'class': 'companyName'}) is not None:
                    all_a = soup.find_all("a", {'class': 'companyName'})

                    for a in all_a:
                        i_1 += 1

                        url = a.get('href')

                        time.sleep(2)

                        # Request the content of a page from the url
                        html = requests.get(url, headers=headers)

                        # Parse the content of html_doc
                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.select_one("#Web") is not None:
                            email = "info@" + soup \
                                .select_one("#Web") \
                                .get("href") \
                                .lower() \
                                .replace('www.', '') \
                                .replace("https://", "") \
                                .replace("http://", "") \
                                .split("/")[0]

                            print(str(i_1) + " email : " + email)
                        else:
                            print(str(i_1) + " no email business")
                else:
                    print("no a class companyName")
        else:
            if soup_search.find("a", {'class': 'companyName'}) is not None:
                all_a = soup_search.find_all("a", {'class': 'companyName'})

                for a in all_a:
                    url = a.get('href')

                    time.sleep(2)

                    # Request the content of a page from the url
                    html = requests.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.select_one("#Web") is not None:
                        email = "info@" + soup \
                            .select_one("#Web") \
                            .get("href") \
                            .lower() \
                            .replace('www.', '') \
                            .replace("https://", "") \
                            .replace("http://", "") \
                            .split("/")[0]

                        print("email : " + email)
                    else:
                        print("no email business")
            else:
                print("no a class companyName")

    def test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals(self):
        print("test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activites = [
            {'id': '1', 'url': 'agencias-trabajo'}, # Temporary employment agencies
            {'id': '2', 'url': 'inmobiliario'}, # Real estate
            {'id': '3', 'url': 'reclutamiento'}, # Recruiter
            {'id': '4', 'url': 'software'}, # software
            {'id': '5', 'url': 'hotel'}, # hotel
            {'id': '6', 'url': 'propietario-social'}, # social landlord
            {'id': '7', 'url': 'limpieza'}, # cleaning
            {'id': '8', 'url': 'organizaciones-beneficas'}, # Charities
            {'id': '9', 'url': 'financiero'}, # financial
            {'id': '10', 'url': 'restaurante'}, # restaurant
            {'id': '11', 'url': 'edificio'}, # building
            {'id': '12', 'url': 'peluquero'}, # hairdresser
            {'id': '13', 'url': 'florista'}, # florist
            {'id': '14', 'url': 'cerrajero'}, # locksmith
            {'id': '15', 'url': 'panaderia'}, # bakery
            {'id': '16', 'url': 'seguro'}, # insurance
            {'id': '17', 'url': 'farmacias'}, # Pharmacies
            {'id': '18', 'url': 'motores'}, # movers
            {'id': '19', 'url': 'electricidad'}, # electricity
            {'id': '20', 'url': 'plomeria'}, # plumbing
            {'id': '21', 'url': 'seguridad'}, # security
            {'id': '22', 'url': 'abogado'}, # attorney
            {'id': '23', 'url': 'banco'}, # bank
            {'id': '24', 'url': 'mecanico'}, # mechanic
            {'id': '25', 'url': 'dentista'}, # dentist
            {'id': '26', 'url': 'medico'}, # doctor
            {'id': '27', 'url': 'contador'}, # accountant
            {'id': '28', 'url': 'tienda-de-comestibles'}, # Grocery Stores
            {'id': '29', 'url': 'notario'}, # notary
            {'id': '30', 'url': 'joyeria'}, # jewellery
            {'id': '31', 'url': 'sastre'}, # tailors
            {'id': '32', 'url': 'carnes'}, # butcher
            {'id': '33', 'url': 'biblioteca'}, # library
            {'id': '34', 'url': 'arquitecto'}, # Architects
            {'id': '36', 'url': 'cemento'}, # cement
            {'id': '37', 'url': 'calefaccion'}, # heating
            {'id': '38', 'url': 'bote'}, # boat
            {'id': '39', 'url': 'frio'}, # cold
            {'id': '41', 'url': 'acero'}, # steel
            {'id': '42', 'url': 'quimico'}, # chemicals
            {'id': '43', 'url': 'gas'}, # gas
            {'id': '44', 'url': 'oro'} # gold
        ]

        capitales_du_monde = [
            {'id': '546', 'nom': 'buenos-aires', 'pays': 'Argentina'}, # Around La Plata
            {'id': '547', 'nom': 'catamarca', 'pays': 'Argentina'}, # Around Catamarca
            {'id': '548', 'nom': 'chaco', 'pays': 'Argentina'}, # Around Resistencia
            {'id': '549', 'nom': 'chubut', 'pays': 'Argentina'}, # Around Rawson
            {'id': '550', 'nom': 'cordoba', 'pays': 'Argentina'}, # Around Córdoba
            {'id': '551', 'nom': 'corrientes', 'pays': 'Argentina'}, # Around Corrientes
            {'id': '552', 'nom': 'entre-rios', 'pays': 'Argentina'}, # Around Paraná
            {'id': '553', 'nom': 'formosa', 'pays': 'Argentina'}, # Around Formosa
            {'id': '554', 'nom': 'jujuy', 'pays': 'Argentina'}, # Around Jujuy
            {'id': '555', 'nom': 'la-pampa', 'pays': 'Argentina'}, # Around Santa Rosa
            {'id': '556', 'nom': 'la-rioja', 'pays': 'Argentina'}, # Around La Rioja
            {'id': '557', 'nom': 'mendoza', 'pays': 'Argentina'}, # Around Mendoza
            {'id': '558', 'nom': 'misiones', 'pays': 'Argentina'}, # Around Posadas
            {'id': '559', 'nom': 'neuquen', 'pays': 'Argentina'}, # Around Neuquén
            {'id': '560', 'nom': 'rio-negro', 'pays': 'Argentina'}, # Around Viedma
            {'id': '561', 'nom': 'salta', 'pays': 'Argentina'}, # Around Salta
            {'id': '562', 'nom': 'san-juan', 'pays': 'Argentina'}, # Around San Juan
            {'id': '563', 'nom': 'san-luis', 'pays': 'Argentina'}, # Around San Luis
            {'id': '564', 'nom': 'santa-cruz', 'pays': 'Argentina'}, # Around Río Gallegos
            {'id': '565', 'nom': 'santa-fe', 'pays': 'Argentina'}, # Around Santa Fe
            {'id': '566', 'nom': 'santiago-del-estero', 'pays': 'Argentina'}, # Around Estero
            {'id': '567', 'nom': 'tierra-del-fuego', 'pays': 'Argentina'}, # Around Tierra del Fuego
            {'id': '568', 'nom': 'tucuman', 'pays': 'Argentina'}, # Around ucumán
        ]

        try:
            for activite in activites:
                for capitale in capitales_du_monde:
                    activity = activite.get('url')

                    city = capitale.get('nom')

                    number_of_pages = 0

                    url_page = "https://www.paginasamarillas.com.ar/buscar/" + city + "/q/" + activity + "/"

                    time.sleep(2)

                    html_search = requests.get(url_page, headers=headers)

                    soup_search = BeautifulSoup(html_search.content, 'html.parser')

                    if soup_search.find("h1", {"class": "light"}) is not None:
                        number_of_pages_with_coma = int(soup_search.find("h1", {"class": "light"})
                                                        .text
                                                        .split("|")[1]
                                                        .replace(" ", "")
                                                        .replace("resultados", "")
                                                        ) / 17

                        if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                            number_of_pages += round(number_of_pages_with_coma) + 1
                            print('number_of_pages : ' + str(number_of_pages))
                        elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                            number_of_pages += round(number_of_pages_with_coma)
                            print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print("error pages")

                    i_1 = 0

                    if number_of_pages > 1:
                        for i in range(1, number_of_pages + 1):
                            url = url_page + "p-" + str(i) + "/?tieneCobertura=true"

                            print(url)

                            time.sleep(2)

                            # Request the content of a page from the url
                            html = requests.get(url, headers=headers)

                            # Parse the content of html_doc
                            soup = BeautifulSoup(html.content, 'html.parser')

                            if soup.find("a", {'class': 'companyName'}) is not None:
                                all_a = soup.find_all("a", {'class': 'companyName'})

                                for a in all_a:
                                    i_1 += 1

                                    url = a.get('href')

                                    time.sleep(2)

                                    # Request the content of a page from the url
                                    html = requests.get(url, headers=headers)

                                    # Parse the content of html_doc
                                    soup = BeautifulSoup(html.content, 'html.parser')

                                    if soup.select_one("#Web") is not None:
                                        email = "info@" + soup \
                                            .select_one("#Web") \
                                            .get("href") \
                                            .lower() \
                                            .replace('www.', '') \
                                            .replace("https://", "") \
                                            .replace("http://", "") \
                                            .split("/")[0]

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
                                                    print(str(i_1)
                                                          + " The record is stored : "
                                                          + email)
                                                    connection.close()
                                                except Exception as e:
                                                    print(str(i_1)
                                                          + " The record already exists : "
                                                          + email
                                                          + " " + str(e))
                                                    connection.close()
                                        except Exception as e:
                                            print(str(i_1) + " An error with the email : " + email + " " + str(e))
                                    else:
                                        print(str(i_1) + " no email business")
                            else:
                                print("no a class companyName")
                    else:
                        if soup_search.find("a", {'class': 'companyName'}) is not None:
                            all_a = soup_search.find_all("a", {'class': 'companyName'})

                            for a in all_a:
                                i_1 += 1

                                url = a.get('href')

                                time.sleep(2)

                                # Request the content of a page from the url
                                html = requests.get(url, headers=headers)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                if soup.select_one("#Web") is not None:
                                    email = "info@" + soup \
                                        .select_one("#Web") \
                                        .get("href") \
                                        .lower() \
                                        .replace('www.', '') \
                                        .replace("https://", "") \
                                        .replace("http://", "") \
                                        .split("/")[0]

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
                                                print(str(i_1)
                                                      + " The record is stored : "
                                                      + email)
                                                connection.close()
                                            except Exception as e:
                                                print(str(i_1)
                                                      + " The record already exists : "
                                                      + email
                                                      + " " + str(e))
                                                connection.close()
                                    except Exception as e:
                                        print(str(i_1) + " An error with the email : " + email + " " + str(e))
                                else:
                                    print(str(i_1) + " no email business")
                        else:
                            print("no a class companyName")
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
