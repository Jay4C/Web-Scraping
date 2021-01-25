from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesUruguay(unittest.TestCase):
    def test_extract_email_from_one_result(self):
        print("test_extract_email_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.paginasamarillas.com.uy/compania/UNION/L144145/Comercio+Playa+Hotel/"

        time.sleep(3)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("span", {'itemprop': 'email'}) is not None:
            email = "info@" + soup.find("span", {'itemprop': 'email'}) \
                .text \
                .split("@")[1]

            print("email : " + email)
        else:
            print("no email business")

    def test_extract_email_from_website_from_one_result(self):
        print("test_extract_email_from_website_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.paginasamarillas.com.uy/compania/UNION/L144145/Comercio+Playa+Hotel/"

        time.sleep(3)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("span", {'itemprop': 'url'}) is not None:
            email = "info@" + soup.find("span", {'itemprop': 'url'}) \
                .text \
                .lower() \
                .replace('www.', '') \
                .replace("https://", "") \
                .replace("http://", "") \
                .split('/')[0]

            print("email : " + email)
        else:
            print("no email business")

    def test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.paginasamarillas.com.uy/buscar/Montevideo/hotel/1/"

        time.sleep(2)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {'class': 't-fpbc'}) is not None:
            all_a = soup.find_all("a", {'class': 't-fpbc'})

            for a in all_a:
                url = "https://www.paginasamarillas.com.uy" + a.get('href')

                time.sleep(3)

                # Request the content of a page from the url
                html = requests.get(url, headers=headers)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                # extract email
                if soup.find("span", {'itemprop': 'email'}) is not None:
                    email = "info@" + soup.find("span", {'itemprop': 'email'}) \
                        .text \
                        .split("@")[1]

                    print("email : " + email)
                else:
                    print("no email business from email")

                # extract email from website
                if soup.find("span", {'itemprop': 'url'}) is not None:
                    email = "info@" + soup.find("span", {'itemprop': 'url'}) \
                        .text \
                        .lower() \
                        .replace('www.', '') \
                        .replace("https://", "") \
                        .replace("http://", "") \
                        .split('/')[0]

                    print("email : " + email)
                else:
                    print("no email business from website")
        else:
            print("no a class t-fpbc")

    def test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activity = "hotel"

        city = "Montevideo"

        number_of_pages = 0

        url_page = "https://www.paginasamarillas.com.uy/buscar/" + city + "/" + activity + "/1/"

        time.sleep(2)

        html_search = requests.get(url_page, headers=headers)

        soup = BeautifulSoup(html_search.content, 'html.parser')

        if soup.find("li", {"class": "single"}) is not None:
            number_of_pages_with_coma = int(soup.find("li", {"class": "single"})
                                            .text
                                            .split("/")[1]
                                            .replace(" ", "")
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
                if i < 20:
                    url = "https://www.paginasamarillas.com.uy/buscar/" + city + "/" + activity + "/" + str(i) + "/"

                    print(url)

                    time.sleep(2)

                    # Request the content of a page from the url
                    html = requests.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("a", {'class': 't-fpbc'}) is not None:
                        all_a = soup.find_all("a", {'class': 't-fpbc'})

                        for a in all_a:
                            i_1 += 1

                            url = "https://www.paginasamarillas.com.uy" + a.get('href')

                            time.sleep(3)

                            # Request the content of a page from the url
                            html = requests.get(url, headers=headers)

                            # Parse the content of html_doc
                            soup = BeautifulSoup(html.content, 'html.parser')

                            # extract email
                            if soup.find("span", {'itemprop': 'email'}) is not None:
                                email = "info@" + soup.find("span", {'itemprop': 'email'}) \
                                    .text \
                                    .split("@")[1]

                                print(str(i_1) + " email : " + email)
                            else:
                                print(str(i_1) + " no email business from email")

                            # extract email from website
                            if soup.find("span", {'itemprop': 'url'}) is not None:
                                email = "info@" + soup.find("span", {'itemprop': 'url'}) \
                                    .text \
                                    .lower() \
                                    .replace('www.', '') \
                                    .replace("https://", "") \
                                    .replace("http://", "") \
                                    .split('/')[0]

                                print(str(i_1) + " email : " + email)
                            else:
                                print(str(i_1) + " no email business from website")
                    else:
                        print("no a class t-fpbc")
        else:
            if soup.find("a", {'class': 't-fpbc'}) is not None:
                all_a = soup.find_all("a", {'class': 't-fpbc'})

                for a in all_a:
                    i_1 += 1

                    url = "https://www.paginasamarillas.com.uy" + a.get('href')

                    time.sleep(3)

                    # Request the content of a page from the url
                    html = requests.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    # extract email
                    if soup.find("span", {'itemprop': 'email'}) is not None:
                        email = "info@" + soup.find("span", {'itemprop': 'email'}) \
                            .text \
                            .split("@")[1]

                        print(str(i_1) + " email : " + email)
                    else:
                        print(str(i_1) + " no email business from email")

                    # extract email from website
                    if soup.find("span", {'itemprop': 'url'}) is not None:
                        email = "info@" + soup.find("span", {'itemprop': 'url'}) \
                            .text \
                            .lower() \
                            .replace('www.', '') \
                            .replace("https://", "") \
                            .replace("http://", "") \
                            .split('/')[0]

                        print(str(i_1) + " email : " + email)
                    else:
                        print(str(i_1) + " no email business from website")
            else:
                print("no a class t-fpbc")

    def test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals(self):
        print("test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activites = [
            {'id': '1', 'url': 'trabajo'}, # Temporary employment agencies
            {'id': '2', 'url': 'inmobiliario'}, # Real estate
            {'id': '3', 'url': 'reclutador'}, # Recruiter
            {'id': '4', 'url': 'software'}, # software
            {'id': '5', 'url': 'hotel'}, # hotel
            {'id': '6', 'url': 'social'}, # social landlord
            {'id': '7', 'url': 'limpieza'}, # cleaning
            {'id': '8', 'url': 'beneficas'}, # Charities
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
            {'id': '28', 'url': 'comestibles'}, # Grocery Stores
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
            {'id': '683', 'nom': 'Artigas', 'pays': 'Uruguay'},
            {'id': '684', 'nom': 'Canelones', 'pays': 'Uruguay'},
            {'id': '685', 'nom': 'Cerro+Largo', 'pays': 'Uruguay'},
            {'id': '686', 'nom': 'Colonia', 'pays': 'Uruguay'},
            {'id': '687', 'nom': 'Durazno', 'pays': 'Uruguay'},
            {'id': '688', 'nom': 'Flores', 'pays': 'Uruguay'},
            {'id': '689', 'nom': 'Florida', 'pays': 'Uruguay'},
            {'id': '690', 'nom': 'Lavalleja', 'pays': 'Uruguay'},
            {'id': '691', 'nom': 'Maldonado', 'pays': 'Uruguay'},
            {'id': '692', 'nom': 'Montevideo', 'pays': 'Uruguay'},
            {'id': '693', 'nom': 'Paysandú', 'pays': 'Uruguay'},
            {'id': '694', 'nom': 'Río+Negro', 'pays': 'Uruguay'},
            {'id': '695', 'nom': 'Rivera', 'pays': 'Uruguay'},
            {'id': '696', 'nom': 'Rocha', 'pays': 'Uruguay'},
            {'id': '697', 'nom': 'Salto', 'pays': 'Uruguay'},
            {'id': '698', 'nom': 'San+José', 'pays': 'Uruguay'},
            {'id': '699', 'nom': 'Soriano', 'pays': 'Uruguay'},
            {'id': '700', 'nom': 'Tacuarembó', 'pays': 'Uruguay'},
            {'id': '701', 'nom': 'Treinta+y+Tres', 'pays': 'Uruguay'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    activity = activite.get('url')

                    city = capitale.get('nom')

                    number_of_pages = 0

                    url_page = "https://www.paginasamarillas.com.uy/buscar/" + city + "/" + activity + "/1/"

                    time.sleep(2)

                    html_search = requests.get(url_page, headers=headers)

                    soup = BeautifulSoup(html_search.content, 'html.parser')

                    if soup.find("li", {"class": "single"}) is not None:
                        number_of_pages_with_coma = int(soup.find("li", {"class": "single"})
                                                        .text
                                                        .split("/")[1]
                                                        .replace(" ", "")
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
                            if i < 20:
                                url = "https://www.paginasamarillas.com.uy/buscar/" + city + "/" + activity + "/" + str(
                                    i) + "/"

                                print(url)

                                time.sleep(2)

                                # Request the content of a page from the url
                                html = requests.get(url, headers=headers)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                if soup.find("a", {'class': 't-fpbc'}) is not None:
                                    all_a = soup.find_all("a", {'class': 't-fpbc'})

                                    for a in all_a:
                                        i_1 += 1

                                        url = "https://www.paginasamarillas.com.uy" + a.get('href')

                                        time.sleep(3)

                                        # Request the content of a page from the url
                                        html = requests.get(url, headers=headers)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        # extract email
                                        if soup.find("span", {'itemprop': 'email'}) is not None:
                                            email = "info@" + soup.find("span", {'itemprop': 'email'}) \
                                                .text \
                                                .split("@")[1]

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
                                            print(str(i_1) + " no email business from email")

                                        # extract email from website
                                        if soup.find("span", {'itemprop': 'url'}) is not None:
                                            email = "info@" + soup.find("span", {'itemprop': 'url'}) \
                                                .text \
                                                .lower() \
                                                .replace('www.', '') \
                                                .replace("https://", "") \
                                                .replace("http://", "") \
                                                .split('/')[0]

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
                                            print(str(i_1) + " no email business from website")
                                else:
                                    print("no a class t-fpbc")
                    else:
                        if soup.find("a", {'class': 't-fpbc'}) is not None:
                            all_a = soup.find_all("a", {'class': 't-fpbc'})

                            for a in all_a:
                                i_1 += 1

                                url = "https://www.paginasamarillas.com.uy" + a.get('href')

                                time.sleep(3)

                                # Request the content of a page from the url
                                html = requests.get(url, headers=headers)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                # extract email
                                if soup.find("span", {'itemprop': 'email'}) is not None:
                                    email = "info@" + soup.find("span", {'itemprop': 'email'}) \
                                        .text \
                                        .split("@")[1]

                                    print(str(i_1) + " email : " + email)

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
                                    print(str(i_1) + " no email business from email")

                                # extract email from website
                                if soup.find("span", {'itemprop': 'url'}) is not None:
                                    email = "info@" + soup.find("span", {'itemprop': 'url'}) \
                                        .text \
                                        .lower() \
                                        .replace('www.', '') \
                                        .replace("https://", "") \
                                        .replace("http://", "") \
                                        .split('/')[0]

                                    print(str(i_1) + " email : " + email)

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
                                    print(str(i_1) + " no email business from website")
                        else:
                            print("no a class t-fpbc")
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
