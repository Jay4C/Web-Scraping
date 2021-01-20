from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesColombia(unittest.TestCase):
    def test_extract_email_from_one_result(self):
        print("test_extract_email_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.paginasamarillas.com.co/empresas/my-english-idiomas-y-traducciones/leticia-16392376?ad=27565330"

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
                .replace("http://", "") \
                .split("/")[0]

            print("email : " + email)
        else:
            print("no email business")

    def test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.paginasamarillas.com.co/amazonas/servicios/hoteles?page=2"

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

        activity = "bancos"

        city = "antioquia"

        number_of_pages = 0

        url_page = "https://www.paginasamarillas.com.co/" + city + "/servicios/" + activity

        time.sleep(2)

        html_search = requests.get(url_page, headers=headers)

        soup_search = BeautifulSoup(html_search.content, 'html.parser')

        if soup_search.find("h1", {"class": "light"}) is not None:
            number_of_pages_with_coma = int(soup_search.find("h1", {"class": "light"})
                                            .text
                                            .split("|")[1]
                                            .replace(" ", "")
                                            .replace("resultados", "")
                                            ) / 20

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
                url = url_page + "?page=" + str(i)

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

    def test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals(self):
        print("test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activites = [
            {'id': '1', 'url': 'agencias-trabajo'}, # Temporary employment agencies
            {'id': '2', 'url': 'inmobiliarias'}, # Real estate
            {'id': '3', 'url': 'reclutamientos'}, # Recruiter
            {'id': '4', 'url': 'software'}, # software
            {'id': '5', 'url': 'hoteles'}, # hotel
            {'id': '6', 'url': 'propietarios-social'}, # social landlord
            {'id': '7', 'url': 'aseo-y-limpieza'}, # cleaning
            {'id': '8', 'url': 'organizaciones-beneficas'}, # Charities
            {'id': '9', 'url': 'financiero'}, # financial
            {'id': '10', 'url': 'restaurantes'}, # restaurant
            {'id': '11', 'url': 'edificios'}, # building
            {'id': '12', 'url': 'peluqueros'}, # hairdresser
            {'id': '13', 'url': 'floristas'}, # florist
            {'id': '14', 'url': 'cerrajerias'}, # locksmith
            {'id': '15', 'url': 'panaderias'}, # bakery
            {'id': '16', 'url': 'seguros'}, # insurance
            {'id': '17', 'url': 'farmacias'}, # Pharmacies
            {'id': '18', 'url': 'motores'}, # movers
            {'id': '19', 'url': 'electricidad'}, # electricity
            {'id': '20', 'url': 'plomerias'}, # plumbing
            {'id': '21', 'url': 'seguridad'}, # security
            {'id': '22', 'url': 'abogados'}, # attorney
            {'id': '23', 'url': 'bancos'}, # bank
            {'id': '24', 'url': 'mecanicos'}, # mechanic
            {'id': '25', 'url': 'dentistas'}, # dentist
            {'id': '26', 'url': 'medicina-general'}, # doctor
            {'id': '27', 'url': 'contadores'}, # accountant
            {'id': '28', 'url': 'tiendas'}, # Grocery Stores
            {'id': '29', 'url': 'notarias'}, # notary
            {'id': '30', 'url': 'joyerias'}, # jewellery
            {'id': '31', 'url': 'sastres'}, # tailors
            {'id': '32', 'url': 'carnes'}, # butcher
            {'id': '33', 'url': 'bibliotecas'}, # library
            {'id': '34', 'url': 'arquitectos'}, # Architects
            {'id': '36', 'url': 'cementos'}, # cement
            {'id': '37', 'url': 'calefaccion'}, # heating
            {'id': '38', 'url': 'botes'}, # boat
            {'id': '39', 'url': 'frios'}, # cold
            {'id': '41', 'url': 'aceros'}, # steel
            {'id': '42', 'url': 'quimicos'}, # chemicals
            {'id': '43', 'url': 'gas'}, # gas
            {'id': '44', 'url': 'oro'} # gold
        ]

        capitales_du_monde = [
            {'id': '569', 'nom': 'bogota', 'pays': 'Colombia'}, # Around Bogotá
            {'id': '570', 'nom': 'amazonas', 'pays': 'Colombia'}, # Around Leticia
            {'id': '571', 'nom': 'antioquia', 'pays': 'Colombia'}, # Around Medellín
            {'id': '572', 'nom': 'arauca', 'pays': 'Colombia'}, # Around Arauca
            {'id': '573', 'nom': 'atlantico', 'pays': 'Colombia'}, # Around Barranquilla
            {'id': '574', 'nom': 'cartagena', 'pays': 'Colombia'}, # Around Cartagena
            {'id': '575', 'nom': 'boyaca', 'pays': 'Colombia'}, # Around Tunja
            {'id': '576', 'nom': 'caldas', 'pays': 'Colombia'}, # Around Manizales
            {'id': '577', 'nom': 'caqueta', 'pays': 'Colombia'}, # Around Florencia
            {'id': '578', 'nom': 'casanare', 'pays': 'Colombia'}, # Around Yopal
            {'id': '579', 'nom': 'cauca', 'pays': 'Colombia'}, # Around Popayán
            {'id': '580', 'nom': 'cesar', 'pays': 'Colombia'}, # Around Valledupar
            {'id': '581', 'nom': 'choco', 'pays': 'Colombia'}, # Around Quibdó
            {'id': '582', 'nom': 'cordoba', 'pays': 'Colombia'}, # Around Montería
            {'id': '583', 'nom': 'cundinamarca', 'pays': 'Colombia'}, # Around Cundinamarca
            {'id': '584', 'nom': 'inirida', 'pays': 'Colombia'}, # Around Inirida
            {'id': '585', 'nom': 'guaviare', 'pays': 'Colombia'}, # Around Guaviare
            {'id': '586', 'nom': 'huila', 'pays': 'Colombia'}, # Around Neiva
            {'id': '587', 'nom': 'riohacha', 'pays': 'Colombia'}, # Around Riohacha
            {'id': '588', 'nom': 'magdalena', 'pays': 'Colombia'}, # Around Santa Marta
            {'id': '589', 'nom': 'meta', 'pays': 'Colombia'}, # Around Villavicencio
            {'id': '590', 'nom': 'narino', 'pays': 'Colombia'}, # Around Pasto
            {'id': '591', 'nom': 'norte-de-santander', 'pays': 'Colombia'}, # Around Cúcuta
            {'id': '592', 'nom': 'putumayo', 'pays': 'Colombia'}, # Around Mocoa
            {'id': '593', 'nom': 'quindio', 'pays': 'Colombia'}, # Around Armenia
            {'id': '594', 'nom': 'risaralda', 'pays': 'Colombia'}, # Around Pereira
            {'id': '595', 'nom': 'san-andres-y-providencia', 'pays': 'Colombia'}, # Around San Andrés
            {'id': '596', 'nom': 'santander', 'pays': 'Colombia'}, # Around Bucaramanga
            {'id': '597', 'nom': 'sucre', 'pays': 'Colombia'}, # Around Sincelejo
            {'id': '598', 'nom': 'tolima', 'pays': 'Colombia'}, # Around Ibagué
            {'id': '599', 'nom': 'valle-del-cauca', 'pays': 'Colombia'}, # Around Cali
            {'id': '600', 'nom': 'vaupes', 'pays': 'Colombia'}, # Around Mitú
            {'id': '601', 'nom': 'vichada', 'pays': 'Colombia'} # Around Vichada
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    activity = activite.get('url')

                    city = capitale.get('nom')

                    number_of_pages = 0

                    url_page = "https://www.paginasamarillas.com.co/" + city + "/servicios/" + activity

                    time.sleep(2)

                    html_search = requests.get(url_page, headers=headers)

                    soup_search = BeautifulSoup(html_search.content, 'html.parser')

                    if soup_search.find("h1", {"class": "light"}) is not None:
                        number_of_pages_with_coma = int(soup_search.find("h1", {"class": "light"})
                                                        .text
                                                        .split("|")[1]
                                                        .replace(" ", "")
                                                        .replace("resultados", "")
                                                        ) / 20

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
                            url = url_page + "?page=" + str(i)

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

                                        print(str(i_1) + " email : " + email)
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

                                    print(str(i_1) + " email : " + email)
                                else:
                                    print(str(i_1) + " no email business")
                        else:
                            print("no a class companyName")
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
