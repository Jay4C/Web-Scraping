import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest
import warnings


class UnitTestsDataMinerYellowPagesPoland(unittest.TestCase):
    def test_extract_one_email(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.pkt.pl/firma/kom-rol-kobylniki-sp-z-o-o-120512369"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('div', {'class': 'call-cell call--email'})\
                .find('a', {'data-popup': 'email-popup'})\
                .find('span', {'data-tooltip': 'tooltip'}) is not None:
            email = "info@" + soup.find('div', {'class': 'call-cell call--email'})\
                    .find('a', {'data-popup': 'email-popup'})\
                    .find('span', {'data-tooltip': 'tooltip'})\
                    .get('title')\
                    .split("@")[1]
            print("email : " + email)
        else:
            print("no call-cell call--email")

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        activity = "hotel"

        city = "kujawsko-pomorskie"

        url_search = "https://www.pkt.pl/szukaj/" + activity + "/" + city

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }

        html_search = requests.get(url_search, headers=headers)

        soup_search = BeautifulSoup(html_search.content, 'html.parser')

        number_of_pages = 0

        if soup_search.select_one('#main') is not None:
            number_of_pages_with_coma = int(soup_search
                                            .find('div', {'class': 'box-fall-back-messages'})
                                            .find('h1')
                                            .find_all('b')[0]
                                            .text
                                            )/25

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print("no result header")

        i_1 = 0

        for i in range(1, number_of_pages+1):
            url_of_one_page_of_results = url_search + "/" + str(i)

            print(url_of_one_page_of_results)

            time.sleep(2)

            html_of_one_page_of_results = requests.get(url_of_one_page_of_results, headers=headers)

            soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

            if soup_of_one_page_of_results.find('div', {'class': 'box-content'}) is not None:
                for result_item in soup_of_one_page_of_results.find_all('div', {'class': 'box-content'}):
                    if result_item.find('h2', {'class': 'company-name'}) is not None:
                        i_1 += 1

                        url_result = "https://www.pkt.pl" + result_item.find('h2', {'class': 'company-name'})\
                            .find('a')\
                            .get('href')

                        time.sleep(2)

                        # Request the content of a page from the url
                        html = requests.get(url_result, headers=headers)

                        # Parse the content of html_doc
                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.find('div', {'class': 'call-cell call--email'}) is not None:
                            if soup.find('div', {'class': 'call-cell call--email'})\
                                    .find('a', {'data-popup': 'email-popup'})\
                                    .find('span', {'data-tooltip': 'tooltip'}) is not None:
                                email = "info@" + soup.find('div', {'class': 'call-cell call--email'}) \
                                    .find('a', {'data-popup': 'email-popup'}) \
                                    .find('span', {'data-tooltip': 'tooltip'}) \
                                    .get('title') \
                                    .split("@")[1]

                                print(str(i_1) + " - email : " + email)
                        else:
                            print(str(i_1) + " - no call-cell call--email")
                    else:
                        print(str(i_1) + " - no more info")
            else:
                print('sorry there is nothing')

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            {'id': '1', 'url': 'Agencje pracy tymczasowej'},
            {'id': '2', 'url': 'nieruchomość'},
            {'id': '3', 'url': 'rekrutacja'},
            {'id': '4', 'url': 'oprogramowanie'},
            {'id': '5', 'url': 'hotel'},
            {'id': '6', 'url': 'gospodarz'},
            {'id': '7', 'url': 'czyszczenie'},
            {'id': '8', 'url': 'stowarzyszenie'},
            {'id': '9', 'url': 'budżetowy'},
            {'id': '10', 'url': 'restauracja'},
            {'id': '11', 'url': 'budynek'},
            {'id': '12', 'url': 'fryzjer'},
            {'id': '13', 'url': 'kwiaciarz'},
            {'id': '14', 'url': 'ślusarz'},
            {'id': '15', 'url': 'piekarnia'},
            {'id': '16', 'url': 'ubezpieczenie'},
            {'id': '17', 'url': 'apteka'},
            {'id': '18', 'url': 'w ruchu'},
            {'id': '19', 'url': 'Elektryczność'},
            {'id': '20', 'url': 'instalacja wodociągowa'},
            {'id': '21', 'url': 'bezpieczeństwo'},
            {'id': '22', 'url': 'prawni'},
            {'id': '23', 'url': 'banki'},
            {'id': '24', 'url': 'garaż'},
            {'id': '25', 'url': 'stomatolodzy'},
            {'id': '26', 'url': 'lekarz'},
            {'id': '27', 'url': 'biura rachunkowe'},
            {'id': '28', 'url': 'centra handlowe'},
            {'id': '29', 'url': 'notariusze'},
            {'id': '30', 'url': 'jubilerzy'},
            {'id': '31', 'url': 'dostosować'},
            {'id': '32', 'url': 'mięso'},
            {'id': '33', 'url': 'biblioteki i czytelnie'},
            {'id': '34', 'url': 'architekci'},
            {'id': '36', 'url': 'cement'},
            {'id': '37', 'url': 'ogrzewanie'},
            {'id': '38', 'url': 'łódź'},
            {'id': '39', 'url': 'zimno'},
            {'id': '41', 'url': 'stal'},
            {'id': '42', 'url': 'chemikalia'},
            {'id': '43', 'url': 'gaz'},
            {'id': '44', 'url': 'złoto'}
        ]

        capitales_du_monde = [
            {'id': '494', 'nom': 'wielkopolskie'},
            {'id': '495', 'nom': 'kujawsko-pomorskie'},
            {'id': '496', 'nom': 'małopolskie'},
            {'id': '497', 'nom': 'łódzkie'},
            {'id': '498', 'nom': 'dolnośląskie'},
            {'id': '499', 'nom': 'lubelskie'},
            {'id': '500', 'nom': 'lubuskie'},
            {'id': '501', 'nom': 'mazowieckie'},
            {'id': '502', 'nom': 'opolskie'},
            {'id': '503', 'nom': 'podlaskie'},
            {'id': '504', 'nom': 'pomorskie'},
            {'id': '505', 'nom': 'śląskie'},
            {'id': '506', 'nom': 'podkarpackie'},
            {'id': '507', 'nom': 'świętokrzyskie'},
            {'id': '508', 'nom': 'warmińsko-mazurskie'},
            {'id': '509', 'nom': 'zachodniopomorskie'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get('url')

                        city = capitale.get('nom')

                        url_search = "https://www.pkt.pl/szukaj/" + activity + "/" + city

                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
                        }

                        html_search = requests.get(url_search, headers=headers)

                        soup_search = BeautifulSoup(html_search.content, 'html.parser')

                        number_of_pages = 0

                        if soup_search.select_one('#main') is not None:
                            number_of_pages_with_coma = int(soup_search
                                                            .find('div', {'class': 'box-fall-back-messages'})
                                                            .find('h1')
                                                            .find_all('b')[0]
                                                            .text
                                                            ) / 25

                            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                number_of_pages += round(number_of_pages_with_coma) + 1
                                print('number_of_pages : ' + str(number_of_pages))

                            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                number_of_pages += round(number_of_pages_with_coma)
                                print('number_of_pages : ' + str(number_of_pages))
                        else:
                            print("no result header")

                        i_1 = 0

                        for i in range(1, number_of_pages + 1):
                            url_of_one_page_of_results = url_search + "/" + str(i)

                            print(url_of_one_page_of_results)

                            time.sleep(2)

                            html_of_one_page_of_results = requests.get(url_of_one_page_of_results, headers=headers)

                            soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                        'html.parser')

                            if soup_of_one_page_of_results.find('div', {'class': 'box-content'}) is not None:
                                for result_item in soup_of_one_page_of_results.find_all('div',
                                                                                        {'class': 'box-content'}):
                                    if result_item.find('h2', {'class': 'company-name'}) is not None:
                                        i_1 += 1

                                        url_result = "https://www.pkt.pl" + result_item\
                                            .find('h2', {'class': 'company-name'}) \
                                            .find('a') \
                                            .get('href')

                                        time.sleep(2)

                                        # Request the content of a page from the url
                                        html = requests.get(url_result, headers=headers)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        if soup.find('div', {'class': 'call-cell call--email'}) is not None:
                                            if soup.find('div', {'class': 'call-cell call--email'}) \
                                                    .find('a', {'data-popup': 'email-popup'}) \
                                                    .find('span', {'data-tooltip': 'tooltip'}) is not None:
                                                email = "info@" + soup.find('div', {'class': 'call-cell call--email'}) \
                                                    .find('a', {'data-popup': 'email-popup'}) \
                                                    .find('span', {'data-tooltip': 'tooltip'}) \
                                                    .get('title') \
                                                    .split("@")[1]

                                                print(str(i_1) + " - email : " + email)

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
                                                            print(str(i_1) + " The record is stored : " + email)
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
                                            print(str(i_1) + " - no call-cell call--email")
                                    else:
                                        print(str(i_1) + " - no more info")
                            else:
                                print('sorry there is nothing')
                    except Exception as e:
                        print("There is an error connection at url : " + str(e))
        finally:
            print('done')


if __name__ == '__main__':
    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
    unittest.main()
