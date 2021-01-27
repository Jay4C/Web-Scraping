import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesPortugal(unittest.TestCase):
    def test_extract_email_from_one_result(self):
        print("test_extract_email_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.pai.pt/paginas/60747-hotel-mar-e-sol-setubal"

        time.sleep(3)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {'data-trackable-event': 'visit-webpage'}) is not None:
            email = "info@" + soup.find("a", {'data-trackable-event': 'visit-webpage'}) \
                .get('href') \
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

        url = "https://www.pai.pt/searches?search[category_id]=&search[center]=&search[free_search]=true&search[group_id]=&search[location]=lisbon&search[location_id]=&search[location_value]=lisbon&search[map]=&search[ne]=&search[query]=hotel&search[sw]=&search[tag_id]=&page=1"

        time.sleep(2)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'class': 'card-link'}) is not None:
            all_single_product = soup.find_all('a', {'class': 'card-link'})

            for single_product in all_single_product:
                url = 'https://www.pai.pt' + single_product.get('href')

                time.sleep(3)

                # Request the content of a page from the url
                html = requests.get(url, headers=headers)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("a", {'data-trackable-event': 'visit-webpage'}) is not None:
                    email = "info@" + soup.find("a", {'data-trackable-event': 'visit-webpage'}) \
                        .get('href') \
                        .replace('www.', '') \
                        .replace("https://", "") \
                        .replace("http://", "") \
                        .split('/')[0]

                    print("email : " + email)
                else:
                    print("no email business")
        else:
            print("no div class single-product")

    def test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activity = "hotel"

        city = "lisbon"

        number_of_pages = 0

        url_page = "https://www.pai.pt/searches?search[category_id]=&search[center]=&search[free_search]=true&search[group_id]=&search[location]=" + city + "&search[location_id]=&search[location_value]=" + city + "&search[map]=&search[ne]=&search[query]=" + activity + "&search[sw]=&search[tag_id]"

        time.sleep(2)

        html_search = requests.get(url_page, headers=headers)

        soup_search = BeautifulSoup(html_search.content, 'html.parser')

        if soup_search.find("div", {"class": "results-title"}) is not None:
            number_of_pages_with_coma = int(soup_search.find("div", {"class": "results-title"})
                                            .find('p', {'class': 'separator'})
                                            .find('strong')
                                            .text
                                            .replace(" ", "")
                                            .replace("resultado(s)", "")
                                            ) / 10

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
                url = url_page + "&page=" + str(i)

                print(url)

                time.sleep(2)

                # Request the content of a page from the url
                html = requests.get(url, headers=headers)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find('a', {'class': 'card-link'}) is not None:
                    all_single_product = soup.find_all('a', {'class': 'card-link'})

                    for single_product in all_single_product:
                        i_1 += 1

                        url = 'https://www.pai.pt' + single_product.get('href')

                        time.sleep(3)

                        # Request the content of a page from the url
                        html = requests.get(url, headers=headers)

                        # Parse the content of html_doc
                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.find("a", {'data-trackable-event': 'visit-webpage'}) is not None:
                            email = "info@" + soup.find("a", {'data-trackable-event': 'visit-webpage'}) \
                                .get('href') \
                                .replace('www.', '') \
                                .replace("https://", "") \
                                .replace("http://", "") \
                                .split('/')[0]

                            print(str(i_1) + " email : " + email)
                        else:
                            print(str(i_1) + " no email business")
                else:
                    print("no div class single-product")
        else:
            if soup_search.find('a', {'class': 'card-link'}) is not None:
                all_single_product = soup_search.find_all('a', {'class': 'card-link'})

                for single_product in all_single_product:
                    i_1 += 1

                    url = 'https://www.pai.pt' + single_product.get('href')

                    time.sleep(3)

                    # Request the content of a page from the url
                    html = requests.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("a", {'data-trackable-event': 'visit-webpage'}) is not None:
                        email = "info@" + soup.find("a", {'data-trackable-event': 'visit-webpage'}) \
                            .get('href') \
                            .replace('www.', '') \
                            .replace("https://", "") \
                            .replace("http://", "") \
                            .split('/')[0]

                        print(str(i_1) + " email : " + email)
                    else:
                        print(str(i_1) + " no email business")
            else:
                print("no div class single-product")

    def test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals(self):
        print("test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activites = [
            {'id': '1', 'url': 'emprego'},  # Temporary employment agencies
            {'id': '2', 'url': 'imobiliária'},  # Real estate
            {'id': '3', 'url': 'recrutamento'},  # Recruiter
            {'id': '4', 'url': 'informática'},  # software
            {'id': '5', 'url': 'hotel'},  # hotel
            {'id': '6', 'url': 'social'},  # social landlord
            {'id': '7', 'url': 'limpeza'},  # cleaning
            {'id': '8', 'url': 'caridade'},  # charity
            {'id': '9', 'url': 'financeiro'},  # financial
            {'id': '10', 'url': 'restaurante'},  # restaurant
            {'id': '11', 'url': 'construção'},  # building
            {'id': '12', 'url': 'cabeleireiro'},  # hairdresser
            {'id': '13', 'url': 'florista'},  # florist
            {'id': '14', 'url': 'chaveiro'},  # locksmith
            {'id': '15', 'url': 'padaria'},  # bakery
            {'id': '16', 'url': 'seguro'},  # insurance
            {'id': '17', 'url': 'farmacia'},  # pharmacy
            {'id': '18', 'url': 'motor'},  # mover
            {'id': '19', 'url': 'eletricidade'},  # electricity
            {'id': '20', 'url': 'canalização'},  # plumbing
            {'id': '21', 'url': 'segurança'},  # security
            {'id': '22', 'url': 'advogado'},  # attorney
            {'id': '23', 'url': 'banco'},  # bank
            {'id': '24', 'url': 'garagem'},  # garage
            {'id': '25', 'url': 'dentista'},  # dentist
            {'id': '26', 'url': 'médico'},  # doctor
            {'id': '27', 'url': 'contabilista'},  # accountant
            {'id': '28', 'url': 'mercearia'},  # grocery stores
            {'id': '29', 'url': 'notário'},  # notary
            {'id': '30', 'url': 'jóias'},  # jewellery
            {'id': '31', 'url': 'alfaiate'},  # tailor
            {'id': '32', 'url': 'carne'},  # butcher
            {'id': '33', 'url': 'biblioteca'},  # library
            {'id': '34', 'url': 'arquiteto'},  # architect
            {'id': '36', 'url': 'cimento'},  # cement
            {'id': '37', 'url': 'aquecimento'},  # heating
            {'id': '38', 'url': 'marítimo'},  # boat
            {'id': '39', 'url': 'frio'},  # cold
            {'id': '41', 'url': 'aço'},  # steel
            {'id': '42', 'url': 'químico'},  # chemical
            {'id': '43', 'url': 'gás'},  # gas
            {'id': '44', 'url': 'ouro'}  # gold
        ]

        capitales_du_monde = [
            {'id': '802', 'nom': 'Lisbon', 'pays': 'portugal'},
            {'id': '803', 'nom': 'Leiria', 'pays': 'portugal'},
            {'id': '804', 'nom': 'Santarém', 'pays': 'portugal'},
            {'id': '805', 'nom': 'Setúbal', 'pays': 'portugal'},
            {'id': '806', 'nom': 'Beja', 'pays': 'portugal'},
            {'id': '807', 'nom': 'Faro', 'pays': 'portugal'},
            {'id': '808', 'nom': 'Évora', 'pays': 'portugal'},
            {'id': '809', 'nom': 'Portalegre', 'pays': 'portugal'},
            {'id': '810', 'nom': 'Castelo+Branco', 'pays': 'portugal'},
            {'id': '811', 'nom': 'Guarda', 'pays': 'portugal'},
            {'id': '812', 'nom': 'Coimbra', 'pays': 'portugal'},
            {'id': '813', 'nom': 'Aveiro', 'pays': 'portugal'},
            {'id': '814', 'nom': 'Viseu', 'pays': 'portugal'},
            {'id': '815', 'nom': 'Bragança', 'pays': 'portugal'},
            {'id': '816', 'nom': 'Vila+Real', 'pays': 'portugal'},
            {'id': '817', 'nom': 'Porto', 'pays': 'portugal'},
            {'id': '818', 'nom': 'Braga', 'pays': 'portugal'},
            {'id': '819', 'nom': 'Viana+do+Castelo', 'pays': 'portugal'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    activity = activite.get('url')

                    city = capitale.get('nom')

                    number_of_pages = 0

                    url_page = "https://www.pai.pt/searches?search[category_id]=&search[center]=&search[free_search]=true&search[group_id]=&search[location]=" + city + "&search[location_id]=&search[location_value]=" + city + "&search[map]=&search[ne]=&search[query]=" + activity + "&search[sw]=&search[tag_id]"

                    time.sleep(2)

                    html_search = requests.get(url_page, headers=headers)

                    soup_search = BeautifulSoup(html_search.content, 'html.parser')

                    if soup_search.find("div", {"class": "results-title"}) is not None:
                        number_of_pages_with_coma = int(soup_search.find("div", {"class": "results-title"})
                                                        .find('p', {'class': 'separator'})
                                                        .find('strong')
                                                        .text
                                                        .replace(" ", "")
                                                        .replace("resultado(s)", "")
                                                        ) / 10

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
                            url = url_page + "&page=" + str(i)

                            print(url)

                            time.sleep(2)

                            # Request the content of a page from the url
                            html = requests.get(url, headers=headers)

                            # Parse the content of html_doc
                            soup = BeautifulSoup(html.content, 'html.parser')

                            if soup.find('a', {'class': 'card-link'}) is not None:
                                all_single_product = soup.find_all('a', {'class': 'card-link'})

                                for single_product in all_single_product:
                                    i_1 += 1

                                    url = 'https://www.pai.pt' + single_product.get('href')

                                    time.sleep(3)

                                    # Request the content of a page from the url
                                    html = requests.get(url, headers=headers)

                                    # Parse the content of html_doc
                                    soup = BeautifulSoup(html.content, 'html.parser')

                                    if soup.find("a", {'data-trackable-event': 'visit-webpage'}) is not None:
                                        email = "info@" + soup.find("a", {'data-trackable-event': 'visit-webpage'}) \
                                            .get('href') \
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
                                        print(str(i_1) + " no email business")
                            else:
                                print("no div class single-product")
                    else:
                        if soup_search.find('a', {'class': 'card-link'}) is not None:
                            all_single_product = soup_search.find_all('a', {'class': 'card-link'})

                            for single_product in all_single_product:
                                i_1 += 1

                                url = 'https://www.pai.pt' + single_product.get('href')

                                time.sleep(3)

                                # Request the content of a page from the url
                                html = requests.get(url, headers=headers)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                if soup.find("a", {'data-trackable-event': 'visit-webpage'}) is not None:
                                    email = "info@" + soup.find("a", {'data-trackable-event': 'visit-webpage'}) \
                                        .get('href') \
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
                                    print(str(i_1) + " no email business")
                        else:
                            print("no div class single-product")
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
