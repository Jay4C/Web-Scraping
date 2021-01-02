import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest
from validate_email import validate_email


class UnitTestsDataMinerYellowPagesGermany(unittest.TestCase):
    def test_extract_one_email(self):
        url = "https://www.gelbeseiten.de/gsbiz/68a73bb6-672f-48e3-b677-2e341473fd67"

        # Request the content of a page from the url
        html = requests.get(url)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'property': 'email'}) is not None:
            email = soup.find('a', {'property': 'email'}).get('content')
            print("email : " + email)

        else:
            print('no email business')

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        url_search = "https://www.gelbeseiten.de/Suche/Hotel/Wiesbaden"
        html_search = requests.get(url_search)
        soup_search = BeautifulSoup(html_search.content, 'html.parser')
        number_of_pages = 0

        if soup_search.select('#mod-TrefferlisteInfo') is not None:
            number_of_pages_with_coma = int(soup_search.select_one('#mod-TrefferlisteInfo').text)/50

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(int(soup_search.select_one('#mod-TrefferlisteInfo').text) / 50) + 1
                print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(int(soup_search.select_one('#mod-TrefferlisteInfo').text) / 50)
                print('number_of_pages : ' + str(number_of_pages))

        i_1 = 0

        for i in range(1, number_of_pages+1):
            url_of_one_page_of_results = url_search + "/Seite-" + str(i)
            time.sleep(2)
            html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
            soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

            if soup_of_one_page_of_results.find('article', {'class': 'mod mod-Treffer'}) is not None:
                for result_item in soup_of_one_page_of_results.find_all('article', {'class': 'mod mod-Treffer'}):
                    i_1 += 1
                    url_result = result_item.find('a', {'class': 'contains-icon-details gs-btn'}).get('href')

                    # Request the content of a page from the url
                    html_result = requests.get(url_result)

                    # Parse the content of html_doc
                    soup_result = BeautifulSoup(html_result.content, 'html.parser')

                    if soup_result.find('a', {'property': 'email'}) is not None:
                        email = "info@" + soup_result.find('a', {'property': 'email'}).get('content').split("@")[1]
                        print("email " + str(i_1) + " : " + email)
                    else:
                        print('no email business')
            else:
                print('sorry there is nothing')

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            # {'id': '1', 'url': 'Zeitarbeit'}
            # {'id': '2', 'url': 'Immobilien'},
            # {'id': '3', 'url': 'Personalagentur'},
            # {'id': '4', 'url': 'Software'},
            # {'id': '5', 'url': 'Hotel'},
            # {'id': '6', 'url': 'Vermieter'},
            # {'id': '7', 'url': 'Reinigung'},
            # {'id': '8', 'url': 'Verein'},
            # {'id': '9', 'url': 'Finanziell'},
            # {'id': '10', 'url': 'Restaurant'},
            # {'id': '11', 'url': 'Baufirma'},
            # {'id': '12', 'url': 'Friseur'},
            # {'id': '13', 'url': 'Florist'},
            # {'id': '14', 'url': 'Schlosser'},
            # {'id': '15', 'url': 'Bäckerei'},
            # {'id': '16', 'url': 'Versicherung'},
            # {'id': '17', 'url': 'Apotheke'},
            # {'id': '18', 'url': 'Bewegen'},
            # {'id': '19', 'url': 'Strom'},
            # {'id': '20', 'url': 'Sanitär'},
            # {'id': '21', 'url': 'Sicherheit'},
            # {'id': '22', 'url': 'Anwalt'},
            # {'id': '23', 'url': 'Bank'},
            # {'id': '24', 'url': 'Garage'},
            # {'id': '25', 'url': 'Zahnarzt'},
            # {'id': '26', 'url': 'Arzt'},
            # {'id': '27', 'url': 'Buchhalter'},
            # {'id': '28', 'url': 'Supermarkt'},
            # {'id': '29', 'url': 'Notar'},
            # {'id': '30', 'url': 'Juwelier'},
            # {'id': '31', 'url': 'Modedesigner'},
            # {'id': '32', 'url': 'Metzger'},
            # {'id': '33', 'url': 'Buchhandlung'},
            # {'id': '34', 'url': 'Architekt'},
            # {'id': '36', 'url': 'Zementwerk'}, # cimenterie
            # {'id': '37', 'url': 'Heizung'}, # chauffage
            # {'id': '38', 'url': 'Boot'}, # naval
            # {'id': '39', 'url': 'kalt'},# froid
            # {'id': '41', 'url': 'Stahlindustrie'}, # sidérurgie
            # {'id': '42', 'url': 'Chemieindustrie'}, # industrie chimique
            # {'id': '43', 'url': 'gas'}, # gaz
            {'id': '44', 'url': 'Goldkauf'} # gold
        ]

        capitales_du_monde = [
            # {'id': '122', 'nom': 'Wiesbaden'}
            {'id': '123', 'nom': 'Stuttgart'},
            {'id': '124', 'nom': 'Schwerin'},
            {'id': '125', 'nom': 'Saarbrücken'},
            {'id': '126', 'nom': 'Potsdam'},
            {'id': '127', 'nom': 'München'},
            {'id': '128', 'nom': 'Mainz'},
            {'id': '129', 'nom': 'Magdeburg'},
            {'id': '130', 'nom': 'Kiel'},
            {'id': '131', 'nom': 'Hannover'},
            {'id': '132', 'nom': 'Erfurt'},
            {'id': '133', 'nom': 'Düsseldorf'},
            {'id': '134', 'nom': 'Dresden'},
            {'id': '135', 'nom': 'Bremen'},
            {'id': '136', 'nom': 'Berlin'},
            {'id': '137', 'nom': 'Hamburg'}
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        url_search = "https://www.gelbeseiten.de/Suche/" + activite.get("url") + "/" \
                                     + capitale.get("nom")

                        print("url_search : " + url_search)

                        html_search = requests.get(url_search)
                        soup_search = BeautifulSoup(html_search.content, 'html.parser')
                        number_of_pages = 0

                        if soup_search.select('#mod-TrefferlisteInfo') is not None:
                            number_of_pages_with_coma = int(soup_search.select_one('#mod-TrefferlisteInfo').text) / 50

                            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                number_of_pages += round(
                                    int(soup_search.select_one('#mod-TrefferlisteInfo').text) / 50) + 1
                                print('number_of_pages : ' + str(number_of_pages))

                            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                number_of_pages += round(int(soup_search.select_one('#mod-TrefferlisteInfo').text) / 50)
                                print('number_of_pages : ' + str(number_of_pages))

                        i_1 = 0

                        try:
                            for i in range(1, number_of_pages + 1):
                                url_of_one_page_of_results = url_search + "/Seite-" + str(i)
                                time.sleep(2)
                                html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                if soup_of_one_page_of_results.find('article', {'class': 'mod mod-Treffer'}) is not None:
                                    for result_item in soup_of_one_page_of_results.find_all('article',
                                                                                            {'class': 'mod mod-Treffer'}):
                                        i_1 += 1

                                        url_result = result_item.find('a', {'class': 'contains-icon-details gs-btn'})\
                                            .get('href')

                                        # Request the content of a page from the url
                                        html_result = requests.get(url_result)

                                        # Parse the content of html_doc
                                        soup_result = BeautifulSoup(html_result.content, 'html.parser')

                                        if soup_result.find('a', {'property': 'email'}) is not None:
                                            email = "info@" + soup_result.find('a', {'property': 'email'}).get('content').split("@")[1]

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
                                                        print(str(i_1) + " The record is stored : " + str(email))
                                                        connection.close()
                                                    except Exception as e:
                                                        print(str(e) + " - " + str(i_1) + " The record already exists : " + str(email))
                                                        connection.close()
                                            except Exception as e:
                                                print(str(e) + " - " + str(i_1) + " An error with the email : " + email)
                                        else:
                                            print(str(i_1) + ' no email business')
                                else:
                                    print('sorry there is nothing')
                        except Exception as e:
                            print(str(e) + " - There is an error connection at url_page")
                    except Exception as e:
                        print(str(e) + " - There is an error connection at url")
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
