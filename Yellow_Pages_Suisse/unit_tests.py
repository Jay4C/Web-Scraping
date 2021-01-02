import unittest
from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors


class UnitTestsDataMinerYellowPagesSuisse(unittest.TestCase):
    def test_web_scraper_email_suisse_1(self):
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='',
            password='',
            db='contacts_professionnels',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        activites = [
            {'id': '1', 'url':'https://tel.local.ch/en/q/?what=Temporary+and+permanent+employment&where='},
            {'id': '2', 'url':'https://tel.local.ch/en/q/?what=real+estate&where='},
            {'id': '3', 'url':''},
            {'id': '4', 'url':''},
            {'id': '5', 'url':''},
            {'id': '6', 'url':''},
            {'id': '7', 'url':''},
            {'id': '8', 'url':''},
            {'id': '9', 'url':''},
            {'id': '10', 'url':''},
            {'id': '11', 'url':''},
            {'id': '12', 'url':''},
            {'id': '13', 'url':''},
            {'id': '14', 'url':''},
            {'id': '15', 'url':''},
            {'id': '16', 'url':''},
            {'id': '17', 'url':''},
            {'id': '18', 'url':''},
            {'id': '19', 'url':''},
            {'id': '20', 'url':''},
            {'id': '21', 'url':''},
            {'id': '22', 'url':''},
            {'id': '23', 'url':''},
        ]

        '''
        {'id':'10', 'nom':'Bern'},
        {'id':'11', 'nom':''},
        {'id':'', 'nom':''},
        {'id':'', 'nom':''},
        {'id':'', 'nom':''},
        '''

        capitales = [
            {'id':'8', 'nom':'Zurich'}
        ]

        try:
            for activite in activites:
                for capitale in capitales:
                    i = 1
                    var = 1
                    while var == 1:
                        url = activite.get('url') + str(capitale.get('nom')) + "+(Canton)&page=" + str(i)
                        
                        print(url)

                        # Request the content of a page from the url of contacts
                        html = requests.get(url)

                        time.sleep(5)

                        # Parse the content of html
                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.find("a", {"title": "E-Mail"}) is None:
                            print(soup.find('h2', {'class': 'lui-margin-vertical-zero'}).text)
                            break

                        else:
                            for a in soup.find_all("a", {"title": "E-Mail"}):
                                email_business = a.get('href')[7:]
                                email = "info@" + str(email_business.split("@")[1])

                                with connection.cursor() as cursor:
                                    try:
                                        sql = "INSERT INTO `emails` (`id_activite`, `id_capitale_du_monde`, `email`) " \
                                              "VALUE (%s, %s, %s)"
                                        cursor.execute(sql, (activite.get('id'), capitale.get('id'), email))
                                        connection.commit()
                                        print("The record is stored : " + str(email))

                                    except:
                                        print("The record already exists : " + str(email))

                        i += 1

        finally:
            connection.close()
            print("finally ok")

    def test_sorry(self):
        url = "https://tel.local.ch/en/q/?what=Restaurant&where=Zurich+(Canton)&page=423"
        #url = "https://tel.local.ch/en/q/?what=Restaurant&where=Zurich+(Canton)&page=42"

        # Request the content of a page from the url of contacts
        html = requests.get(url)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"title": "E-Mail"}) is None:
            print(soup.find('h2', {'class': 'lui-margin-vertical-zero'}).text[:6])

        else:
            print('good')

    def test_web_scraper_email_suisse_2(self):
        print("test_web_scraper_email_suisse_2")

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='',
            password='',
            db='contacts_professionnels',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        activites = [
            # {'id': '1', 'url': 'https://tel.local.ch/en/q/?what=Temporary+and+permanent+employment&where='},
            # {'id': '2', 'url': 'https://tel.local.ch/en/q/?what=real+estate&where='},
            # {'id': '3', 'url': 'https://tel.local.ch/en/q/?what=recruiters&where='},
            # {'id': '4', 'url': 'https://tel.local.ch/en/q/?what=software&where='},
            # {'id': '5', 'url': 'https://tel.local.ch/en/q/?what=hotel&where='},
            # {'id': '6', 'url': 'https://tel.local.ch/en/q/?what=landlord&where='},
            # {'id': '7', 'url': 'https://tel.local.ch/en/q/?what=Cleaning+company&where='},
            # {'id': '8', 'url': 'https://tel.local.ch/en/q/?what=Charitable&where='},
            # {'id': '9', 'url': 'https://tel.local.ch/en/q/?what=Financial+services&where='},
            # {'id': '10', 'url': 'https://tel.local.ch/en/q/?what=Restaurant&where='},
            # {'id': '11', 'url': 'https://tel.local.ch/en/q/?what=building&where='},
            # {'id': '12', 'url': 'https://tel.local.ch/en/q/?what=Hairdresser&where='},
            # {'id': '13', 'url': 'https://tel.local.ch/en/q/?what=Florist&where='},
            # {'id': '14', 'url': 'https://tel.local.ch/en/q/?what=Locksmith&where='},
            # {'id': '15', 'url': 'https://tel.local.ch/en/q/?what=bakery&where='},
            # {'id': '16', 'url': 'https://tel.local.ch/en/q/?what=Insurance&where='},
            # {'id': '17', 'url': 'https://tel.local.ch/en/q/?what=Pharmacy&where='},
            # {'id': '18', 'url': 'https://tel.local.ch/en/q/?what=Movers&where='},
            # {'id': '19', 'url': 'https://tel.local.ch/en/q/?what=Electricity&where='},
            # {'id': '20', 'url': 'https://tel.local.ch/en/q/?what=Construction+plumbers&where='},
            # {'id': '21', 'url': 'https://tel.local.ch/en/q/?what=Security+services&where='},
            # {'id': '22', 'url': 'https://tel.local.ch/en/q/?what=attorney&where='},
            # {'id': '23', 'url': 'https://tel.local.ch/en/q/?what=bank&where='},
            # {'id': '24', 'url': 'https://tel.local.ch/en/q/?what=mechanic&where='},
            # {'id': '25', 'url': 'https://tel.local.ch/en/q/?what=Dentist&where='},
            # {'id': '26', 'url': 'https://tel.local.ch/en/q/?what=doctors&where='},
            # {'id': '27', 'url': 'https://tel.local.ch/en/q/?what=Accounting&where='},
            # {'id': '28', 'url': 'https://tel.local.ch/en/q/?what=Grocery+store&where='},
            # {'id': '29', 'url': 'https://tel.local.ch/en/q/?what=notary&where='},
            # {'id': '30', 'url': 'https://tel.local.ch/en/q/?what=Jewellery&where='},
            # {'id': '31', 'url': 'https://tel.local.ch/en/q/?what=Tailors&where='},
            # {'id': '32', 'url': 'https://tel.local.ch/en/q/?what=butcher&where='},
            # {'id': '33', 'url': 'https://tel.local.ch/en/q/?what=Library&where='},
            # {'id': '34', 'url': 'https://tel.local.ch/en/q/?what=architect&where='},
            {'id': '36', 'url': 'https://tel.local.ch/en/q?what=cement&where='}, # cement
            {'id': '37', 'url': 'https://tel.local.ch/en/q?what=heating&where='}, # heating
            {'id': '38', 'url': 'https://tel.local.ch/en/q?what=naval&where='}, # naval
            {'id': '39', 'url': 'https://tel.local.ch/en/q?what=cold&where='}, # cold
            {'id': '41', 'url': 'https://tel.local.ch/en/q?what=steel&where='}, # steel
            {'id': '42', 'url': 'https://tel.local.ch/en/q?what=chemicals&where='}, # chemicals
            {'id': '43', 'url': 'https://tel.local.ch/en/q?what=gas&where='}, # gas
            {'id': '44', 'url': 'https://tel.local.ch/en/q?what=goldsmith&where='} # gold
        ]

        capitales = [
            {'id': '8', 'nom': 'Zurich'},
            {'id': '10', 'nom': 'Bern'},
            {'id': '11', 'nom': 'Lucerne'},
            {'id': '12', 'nom': 'Uri'},
            {'id': '13', 'nom': 'Schwytz'},
            {'id': '14', 'nom': 'Obwald'},
            {'id': '15', 'nom': 'Nidwald'},
            {'id': '16', 'nom': 'Glaris'},
            {'id': '17', 'nom': 'Zoug'},
            {'id': '18', 'nom': 'Fribourg'},
            {'id': '19', 'nom': 'Soleure'},
            {'id': '20', 'nom': 'Bâle-Ville'},
            {'id': '21', 'nom': 'Bâle-Campagne'},
            {'id': '22', 'nom': 'Schaffhouse'},
            {'id': '23', 'nom': 'Appenzell+Outer+Rhodes'},
            {'id': '24', 'nom': 'Appenzell+Inner+Rhodes'},
            {'id': '25', 'nom': 'Saint-Gall'},
            {'id': '26', 'nom': 'Grisons'},
            {'id': '27', 'nom': 'Argovie'},
            {'id': '28', 'nom': 'Thurgovie'},
            {'id': '29', 'nom': 'Tessin'},
            {'id': '30', 'nom': 'Vaud'},
            {'id': '31', 'nom': 'Valais'},
            {'id': '32', 'nom': 'Neuchâtel'},
            {'id': '33', 'nom': 'Genève'},
            {'id': '34', 'nom': 'Jura'}
        ]

        try:
            for activite in activites:
                for capitale in capitales:

                    i = 1

                    var = 1

                    while var == 1:
                        url = activite.get('url') + str(capitale.get('nom')) + "+(Canton)&page=" + str(i)

                        print(url)

                        # Request the content of a page from the url of contacts
                        html = requests.get(url)

                        time.sleep(3)

                        # Parse the content of html
                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.find("a", {"title": "E-Mail"}) is None:
                            print(soup.find('h2', {'class': 'lui-margin-vertical-zero'}).text)
                            break

                        else:
                            i_1 = 1

                            for a in soup.find_all("a", {"title": "E-Mail"}):
                                email_business = a.get('href')[7:]

                                suffixes = [
                                    "info@"
                                ]

                                email = ""

                                for suffix in suffixes:
                                    email = str(suffix + str(email_business.split("@")[1]))

                                    with connection.cursor() as cursor:
                                        try:
                                            sql = "INSERT INTO `emails` (`id_activite`, `id_capitale_du_monde`, `email`) " \
                                                  "VALUE (%s, %s, %s)"

                                            cursor.execute(sql, (activite.get('id'), capitale.get('id'), email))

                                            connection.commit()

                                            print(str(i_1) + " The record is stored : " + str(email))
                                        except Exception as e:
                                            print(str(i_1) + " The record already exists : " + str(email) + " - " + str(e))

                                i_1 += 1

                        i += 1
        finally:
            connection.close()
            print("finally ok")


if __name__ == '__main__':
    unittest.main()
