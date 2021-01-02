from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest
from validate_email import validate_email


class UnitTestsDataMinerYellowPagesAustria(unittest.TestCase):
    def test_email_corporation(self):
        url = "https://www.herold.at/gelbe-seiten/oberwart/j19V8/" \
              "maschinenring-service-burgenland-reggenmbh/?hdg=INET_5022_Personalleasing"
        # Request the content of a page from the url
        html = requests.get(url)
        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'data-category': 'E-Mail'}) is not None:
            email = "info@" + soup.find('a', {'data-category': 'E-Mail'}).get('href')[7:].split('@')[1]
            print(email)

        else:
            print('no email business')

    def test_list_results_profil(self):
        url_search = "https://www.herold.at/gelbe-seiten/burgenland/was_immobilienagenturen/"
        html_search = requests.get(url_search)
        soup_search = BeautifulSoup(html_search.content, 'html.parser')
        number_of_pages = round(int(soup_search.find('nav', {'class': 'pagination-result'})
                                    .find_all('b')[1].text)) + 1

        print('number_of_pages : ' + str(number_of_pages))

        for i in range(1, number_of_pages):
            url = url_search + "?page=" + str(i)
            html = requests.get(url)
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find('div', {'class': 'result-item'}) is not None:
                print('ok : ' + str(i))
                for result_item in soup.find_all('div', {'class': 'result-item'}):
                    url_result = result_item.get('data-detail-url')
                    print('url : ' + url_result)

            else:
                print('sorry there is nothing')

    def test_web_scraper_email_austria(self):
        activites = [
            # {'id': '1', 'url': 'zeitarbeitsfirmen'},
            # {'id': '2', 'url': 'immobilienagenturen'},
            # {'id': '3', 'url': 'personalvermittlungs'},
            # {'id': '4', 'url': 'software'},
            # {'id': '5', 'url': 'hotel'},
            # {'id': '6', 'url': 'vermieter'},
            # {'id': '7', 'url': 'reinigung'},
            # {'id': '8', 'url': 'verein'},
            # {'id': '9', 'url': 'finanz'},
            # {'id': '10', 'url': 'restaurant'},
            # {'id': '11', 'url': 'gebäude'},
            # {'id': '12', 'url': 'friseur'},
            # {'id': '13', 'url': 'blumenhändler'},
            # {'id': '14', 'url': 'schlosser'},
            # {'id': '15', 'url': 'bäckerei'},
            # {'id': '16', 'url': 'versicherung'},
            # {'id': '17', 'url': 'apotheke'},
            # {'id': '18', 'url': 'umzug'},
            # {'id': '19', 'url': 'strom'},
            # {'id': '20', 'url': 'rohrleitungen'},
            # {'id': '21', 'url': 'sicherheit'},
            # {'id': '22', 'url': 'rechtsanwalt'},
            # {'id': '23', 'url': 'bank'},
            # {'id': '24', 'url': 'garage'},
            # {'id': '25', 'url': 'zahnarzt'},
            # {'id': '26', 'url': 'arzt'},
            # {'id': '27', 'url': 'buchhaltung'},
            # {'id': '28', 'url': 'supermarkt'},
            # {'id': '29', 'url': 'notar'},
            # {'id': '30', 'url': 'juwelier'},
            # {'id': '31', 'url': 'schneider'},
            # {'id': '32', 'url': 'metzger'},
            # {'id': '33', 'url': 'buchhandlungen'},
            # {'id': '34', 'url': 'architekt'},
            {'id': '36', 'url': 'zement'}, # cement
            {'id': '37', 'url': 'heizung'}, # heating
            {'id': '38', 'url': 'marine'}, # naval
            {'id': '39', 'url': 'kühlung'}, # cold
            {'id': '41', 'url': 'stahlwerk'}, # steel
            {'id': '42', 'url': 'chemisch'}, # chemicals
            {'id': '43', 'url': 'gas'}, # gas
            {'id': '44', 'url': 'goldkauf'} # Gold buyers
        ]

        capitales_du_monde = [
            {'id': '113', 'nom': 'burgenland'},
            {'id': '114', 'nom': 'kärnten'},
            {'id': '115', 'nom': 'niederösterreich'},
            {'id': '116', 'nom': 'salzburg'},
            {'id': '117', 'nom': 'steiermark'},
            {'id': '118', 'nom': 'tirol'},
            {'id': '119', 'nom': 'oberösterreich'},
            {'id': '120', 'nom': 'wien'},
            {'id': '121', 'nom': 'vorarlberg'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        url_search = "https://www.herold.at/gelbe-seiten/" + capitale.get('nom') + "/was_" \
                                     + activite.get('url') + "/"

                        html_search = requests.get(url_search)
                        soup_search = BeautifulSoup(html_search.content, 'html.parser')
                        number_of_pages = round(int(soup_search.find('nav', {'class': 'pagination-result'})
                                                    .find_all('b')[1].text)) + 1
                        print('number_of_pages : ' + str(number_of_pages))
                        for i in range(1, number_of_pages):
                            try:
                                url = url_search + "?page=" + str(i)
                                html = requests.get(url)
                                soup = BeautifulSoup(html.content, 'html.parser')

                                if soup.find('div', {'class': 'result-item'}) is not None:
                                    print('ok : ' + str(i) + " : " + url)
                                    for result_item in soup.find_all('div', {'class': 'result-item'}):
                                        url_result = result_item.get('data-detail-url')
                                        print("url_result : " + url_result)
                                        html = requests.get(url_result)
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        if soup.find('a', {'data-category': 'E-Mail'}) is not None:
                                            email = "info@" + soup.find('a', {'data-category': 'E-Mail'}).get('href')[7:].split('@')[1]

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
                                                        print("The record is stored : " + str(email))
                                                        connection.close()
                                                    except:
                                                        print("The record already exists : " + str(email))
                                                        connection.close()
                                            except Exception as e:
                                                print(str(e) + " An error with the email : " + email)
                                        else:
                                            print('no email business')
                                else:
                                    print('sorry there is nothing')
                            except Exception as e:
                                print(str(e) + " There is an error connection at url_page")
                    except Exception as e:
                        print(str(e) + " There is an error connection at url")
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
