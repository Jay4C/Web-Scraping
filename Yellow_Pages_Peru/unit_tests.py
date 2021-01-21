from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesPeru(unittest.TestCase):
    def test_extract_email_from_one_result(self):
        print("test_extract_email_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.paginasamarillas.com.pe/empresas/amazon-gold-travel-peru/amazonas-80629011"

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

        url = "https://www.paginasamarillas.com.pe/amazonas/servicios/hotel?page=1"

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

        city = "amazonas"

        number_of_pages = 0

        url_page = "https://www.paginasamarillas.com.pe/" + city + "/servicios/" + activity

        time.sleep(2)

        html_search = requests.get(url_page, headers=headers)

        soup_search = BeautifulSoup(html_search.content, 'html.parser')

        if soup_search.find("h1", {"class": "light"}) is not None:
            number_of_pages_with_coma = int(soup_search.find("h1", {"class": "light"})
                                            .text
                                            .split("|")[1]
                                            .replace(" ", "")
                                            .replace("resultados", "")
                                            ) / 35

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
                if i < 20:
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
                    i_1 = 0

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
            {'id': '2', 'url': 'inmobiliario'}, # Real estate
            {'id': '3', 'url': 'reclutamiento'}, # Recruiter
            {'id': '4', 'url': 'software'}, # software
            {'id': '5', 'url': 'hotel'}, # hotel
            {'id': '6', 'url': 'propietario-social'}, # social landlord
            {'id': '7', 'url': 'limpieza'}, # cleaning
            {'id': '8', 'url': 'organizaciones-beneficas'}, # Charities
            {'id': '9', 'url': 'financiero'}, # financial
            {'id': '10', 'url': 'restaurante'}, # restaurant
            {'id': '11', 'url': 'constructor'}, # building
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
            {'id': '602', 'nom': 'amazonas', 'pays': 'Peru'},
            {'id': '603', 'nom': 'ancash', 'pays': 'Peru'},
            {'id': '604', 'nom': 'apurimac', 'pays': 'Peru'},
            {'id': '605', 'nom': 'arequipa', 'pays': 'Peru'},
            {'id': '606', 'nom': 'ayacucho', 'pays': 'Peru'},
            {'id': '607', 'nom': 'cajamarca', 'pays': 'Peru'},
            {'id': '608', 'nom': 'callao', 'pays': 'Peru'},
            {'id': '609', 'nom': 'Cusco', 'pays': 'Peru'},
            {'id': '610', 'nom': 'huancavelica', 'pays': 'Peru'},
            {'id': '611', 'nom': 'huanuco', 'pays': 'Peru'},
            {'id': '612', 'nom': 'ica', 'pays': 'Peru'},
            {'id': '613', 'nom': 'junin', 'pays': 'Peru'},
            {'id': '614', 'nom': 'la-libertad', 'pays': 'Peru'},
            {'id': '615', 'nom': 'lambayeque', 'pays': 'Peru'},
            {'id': '616', 'nom': 'lima', 'pays': 'Peru'},
            {'id': '617', 'nom': 'loreto', 'pays': 'Peru'},
            {'id': '618', 'nom': 'madre-de-dios', 'pays': 'Peru'},
            {'id': '619', 'nom': 'moquegua', 'pays': 'Peru'},
            {'id': '620', 'nom': 'pasco', 'pays': 'Peru'},
            {'id': '621', 'nom': 'piura', 'pays': 'Peru'},
            {'id': '622', 'nom': 'puno', 'pays': 'Peru'},
            {'id': '623', 'nom': 'san-martin', 'pays': 'Peru'},
            {'id': '624', 'nom': 'tacna', 'pays': 'Peru'},
            {'id': '625', 'nom': 'tumbes', 'pays': 'Peru'},
            {'id': '626', 'nom': 'ucayali', 'pays': 'Peru'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    activity = activite.get('url')

                    city = capitale.get('nom')

                    number_of_pages = 0

                    url_page = "https://www.paginasamarillas.com.pe/" + city + "/servicios/" + activity

                    time.sleep(2)

                    html_search = requests.get(url_page, headers=headers)

                    soup_search = BeautifulSoup(html_search.content, 'html.parser')

                    if soup_search.find("h1", {"class": "light"}) is not None:
                        number_of_pages_with_coma = int(soup_search.find("h1", {"class": "light"})
                                                        .text
                                                        .split("|")[1]
                                                        .replace(" ", "")
                                                        .replace("resultados", "")
                                                        ) / 35

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
                            if i < 20:
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
