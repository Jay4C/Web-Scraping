import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesCroatia(unittest.TestCase):
    def test_extract_one_email(self):
        url = "https://www.zutestranice.hr/tvrtke/Zagreb/L1889580/HOTEL+ANTUNOVI%C4%86+ZAGREB****/"

        # Request the content of a page from the url
        html = requests.get(url)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'data-ta': 'EmailClick'}) is not None:
            emails = soup.find_all('a', {'data-ta': 'EmailClick'})
            for email in emails:
                email_text = "info@" + email.text.split("@")[1]
                print("email : " + email_text)
        else:
            print('no email business')

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        activity = "hotel"
        city = "Zagreb"
        url_search = "https://www.zutestranice.hr/p/" + city + "/" + activity + "/"
        html_search = requests.get(url_search)
        soup_search = BeautifulSoup(html_search.content, 'html.parser')
        number_of_pages = 0

        if soup_search.find('div', {'class': 'pager'}) is not None:
            number_of_pages_with_coma = int(soup_search
                                            .find('div', {'class': 'pager'})
                                            .find_all('li')[1]
                                            .find('span')
                                            .text
                                            .split('/')[1]
                                            )/20

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))

        i_1 = 0

        if number_of_pages > 1:
            for i in range(1, number_of_pages+1):
                url_of_one_page_of_results = url_search + str(i)
                print(url_of_one_page_of_results)
                time.sleep(2)
                html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                if soup_of_one_page_of_results.select_one('#results') is not None:
                    for result_item in soup_of_one_page_of_results.select_one("#results").find_all('li'):
                        if result_item.find('section', {'class': 'profile'}):
                            url_result = "https://www.zutestranice.hr" + result_item\
                                .find('section', {'class': 'profile'})\
                                .find('div', {'class': 'col8'})\
                                .find('h2')\
                                .find('a', {'data-ta': 'FullProfileButtonClick'})\
                                .get('href')

                            # Request the content of a page from the url
                            html_result = requests.get(url_result)

                            # Parse the content of html_doc
                            soup_result = BeautifulSoup(html_result.content, 'html.parser')

                            if soup_result.find('a', {'data-ta': 'EmailClick'}) is not None:
                                emails = soup_result.find_all('a', {'data-ta': 'EmailClick'})
                                for email in emails:
                                    i_1 += 1
                                    email_text = "info@" + email.text.split("@")[1]
                                    print(str(i_1) + " email : " + email_text)
                            else:
                                i_1 += 1
                                print(str(i_1) + ' no email business')
                else:
                    print('sorry there is no results')

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            {'id': '1', 'url': 'zapošljavanje'},
            {'id': '2', 'url': 'nekretnine'},
            {'id': '3', 'url': 'regrutacija'},
            {'id': '4', 'url': 'softver'},
            {'id': '5', 'url': 'hotel'},
            {'id': '6', 'url': 'landlord'},
            {'id': '7', 'url': 'čišćenje'},
            {'id': '8', 'url': 'asocijacija'},
            {'id': '9', 'url': 'financijska'},
            {'id': '10', 'url': 'restoran'},
            {'id': '11', 'url': 'zgrada'},
            {'id': '12', 'url': 'frizer'},
            {'id': '13', 'url': 'cvjećar'},
            {'id': '14', 'url': 'bravar'},
            {'id': '15', 'url': 'pekara'},
            {'id': '16', 'url': 'osiguranje'},
            {'id': '17', 'url': 'ljekarna'},
            {'id': '18', 'url': 'potez'},
            {'id': '19', 'url': 'elektricitet'},
            {'id': '20', 'url': 'vodovodni'},
            {'id': '21', 'url': 'sigurnosti'},
            {'id': '22', 'url': 'pravnik'},
            {'id': '23', 'url': 'banka'},
            {'id': '24', 'url': 'garaža'},
            {'id': '25', 'url': 'stomatolog'},
            {'id': '26', 'url': 'liječnik'},
            {'id': '27', 'url': 'računovodstvo'},
            {'id': '28', 'url': 'supermarket'},
            {'id': '29', 'url': 'bilježnik'},
            {'id': '30', 'url': 'zlatar'},
            {'id': '31', 'url': 'modni+dizajner'},
            {'id': '32', 'url': 'mesar'},
            {'id': '33', 'url': 'knjižara'},
            {'id': '34', 'url': 'arhitekta'},
            {'id': '36', 'url': 'cement'},  # cement
            {'id': '37', 'url': 'grijanje'},  # heating
            {'id': '38', 'url': 'brod'},  # bateau
            {'id': '39', 'url': 'hladno'},  # cold
            {'id': '41', 'url': 'čelik'},  # steel
            {'id': '42', 'url': 'kemikalije'},  # chemicals
            {'id': '43', 'url': 'plin'},  # gas
            {'id': '44', 'url': 'zlatarnice'}  # Gold buyers
        ]

        capitales_du_monde = [
            {'id': '239', 'nom': 'Krapina'},
            {'id': '240', 'nom': 'Sisak'},
            {'id': '241', 'nom': 'Karlovac'},
            {'id': '242', 'nom': 'Varaždin'},
            {'id': '243', 'nom': 'Koprivnica'},
            {'id': '244', 'nom': 'Bjelovar'},
            {'id': '245', 'nom': 'Rijeka'},
            {'id': '246', 'nom': 'Gospić'},
            {'id': '247', 'nom': 'Virovitica'},
            {'id': '248', 'nom': 'Požega'},
            {'id': '249', 'nom': 'Slavonski Brod'},
            {'id': '250', 'nom': 'Zadar'},
            {'id': '251', 'nom': 'Osijek'},
            {'id': '252', 'nom': 'Šibenik'},
            {'id': '253', 'nom': 'Vukovar'},
            {'id': '254', 'nom': 'Split'},
            {'id': '255', 'nom': 'Pazin'},
            {'id': '256', 'nom': 'Dubrovnik'},
            {'id': '257', 'nom': 'Čakovec'},
            {'id': '258', 'nom': 'Zagreb'}
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get('url')
                        city = capitale.get('nom')
                        url_search = "https://www.zutestranice.hr/p/" + city + "/" + activity + "/"

                        headers = {
                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                        }

                        html_search = requests.get(url_search, headers=headers)

                        soup_search = BeautifulSoup(html_search.content, 'html.parser')

                        number_of_pages = 0

                        if soup_search.find('div', {'class': 'pager'}) is not None:
                            number_of_pages_with_coma = int(soup_search
                                                            .find('div', {'class': 'pager'})
                                                            .find_all('li')[1]
                                                            .find('span')
                                                            .text
                                                            .split('/')[1]
                                                            ) / 20

                            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                number_of_pages += round(number_of_pages_with_coma) + 1
                                print('number_of_pages : ' + str(number_of_pages))

                            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                number_of_pages += round(number_of_pages_with_coma)
                                print('number_of_pages : ' + str(number_of_pages))

                        i_1 = 0

                        if number_of_pages > 1:
                            for i in range(1, number_of_pages + 1):
                                url_of_one_page_of_results = url_search + str(i)
                                print(url_of_one_page_of_results)
                                time.sleep(2)

                                headers = {
                                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                                }

                                html_of_one_page_of_results = requests.get(url_of_one_page_of_results, headers=headers)

                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                if soup_of_one_page_of_results.select_one('#results') is not None:
                                    for result_item in soup_of_one_page_of_results.select_one("#results").find_all(
                                            'li'):
                                        if result_item.find('section', {'class': 'profile'}):
                                            url_result = "https://www.zutestranice.hr" + result_item \
                                                .find('section', {'class': 'profile'}) \
                                                .find('div', {'class': 'col8'}) \
                                                .find('h2') \
                                                .find('a', {'data-ta': 'FullProfileButtonClick'}) \
                                                .get('href')

                                            headers = {
                                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                                            }

                                            # Request the content of a page from the url
                                            html_result = requests.get(url_result, headers=headers)

                                            # Parse the content of html_doc
                                            soup_result = BeautifulSoup(html_result.content, 'html.parser')

                                            if soup_result.find('a', {'data-ta': 'EmailClick'}) is not None:
                                                emails = soup_result.find_all('a', {'data-ta': 'EmailClick'})
                                                for email in emails:
                                                    i_1 += 1
                                                    email_text = "info@" + email.text.split("@")[1]
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
                                                                    email_text))
                                                                connection.commit()
                                                                print(str(i_1) + " The record is stored : "
                                                                      + str(email_text))
                                                                connection.close()
                                                            except Exception as e:
                                                                print(str(i_1) + " The record already exists : "
                                                                      + str(email_text) + " " + str(e))
                                                                connection.close()
                                                    except Exception as e:
                                                        print(str(i_1) + " an error with the email : " + email_text + " " + str(e))
                                            else:
                                                i_1 += 1
                                                print(str(i_1) + ' no email business')
                                else:
                                    print('sorry there is no results')
                    except Exception as e:
                        print("There is an error connection at url : " + str(e))
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
