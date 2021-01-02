import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesKosovo(unittest.TestCase):
    def test_extract_one_email(self):
        url = "http://www.yellowpageskosovo.com/item/swiss-diamond-hotel/"

        # Request the content of a page from the url
        html = requests.get(url)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'itemprop': 'email'}) is not None:
            email = "info@" + soup.find('a', {'itemprop': 'email'}).text.split("@")[1]
            print('email : ' + email)
        else:
            print('no email business')

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        activity = "hotel"
        var = 1
        i = 1
        while var == 1:
            url_search = "http://www.yellowpageskosovo.com/?s=" + activity + "&a=true&lang=en&paged=" + str(i)
            print(url_search)
            html_search = requests.get(url_search)
            soup_search = BeautifulSoup(html_search.content, 'html.parser')

            i_1 = 0

            if soup_search.select_one('#content') is not None:
                if soup_search.select_one('#content').find('div', {'class': 'item-container'}) is not None:
                    for result_item in soup_search\
                            .select_one('#content')\
                            .find_all('div', {'class': 'item-container'}):
                        i_1 += 1

                        url_result = result_item\
                            .find('div', {'class': 'content'})\
                            .find('div', {'class': 'item-image'})\
                            .find('a', {'class': 'main-link'})\
                            .get('href')

                        time.sleep(2)

                        # Request the content of a page from the url
                        html = requests.get(url_result)

                        # Parse the content of html_doc
                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.find('a', {'itemprop': 'email'}) is not None:
                            email = "info@" + soup.find('a', {'itemprop': 'email'}).text.split("@")[1]
                            print(str(i_1) + ' email : ' + email)
                        else:
                            print(str(i_1) + ' no email business')

                    i += 1
                else:
                    print("no item container")
            else:
                print("sorry there is nothing")
                break

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            # {'id': '1', 'url': 'labour'}
            # {'id': '2', 'url': 'real+estate'},
            # {'id': '3', 'url': 'recruitment'},
            # {'id': '4', 'url': 'software'},
            # {'id': '5', 'url': 'hotel'},
            # {'id': '6', 'url': 'landlord'},
            # {'id': '7', 'url': 'cleaning'},
            # {'id': '8', 'url': 'association'},
            # {'id': '9', 'url': 'financial'},
            # {'id': '10', 'url': 'restaurant'},
            # {'id': '11', 'url': 'building'},
            # {'id': '12', 'url': 'hairdresser'},
            # {'id': '13', 'url': 'florist'},
            # {'id': '14', 'url': 'locksmith'},
            # {'id': '15', 'url': 'bakery'},
            # {'id': '16', 'url': 'insurance'},
            # {'id': '17', 'url': 'pharmacy'},
            # {'id': '18', 'url': 'moving'},
            # {'id': '19', 'url': 'electricity'},
            # {'id': '20', 'url': 'plumbing'},
            # {'id': '21', 'url': 'security'},
            # {'id': '22', 'url': 'lawyer'},
            # {'id': '23', 'url': 'bank'},
            # {'id': '24', 'url': 'garage'},
            # {'id': '25', 'url': 'dentist'},
            # {'id': '26', 'url': 'doctor'},
            # {'id': '27', 'url': 'accounting'},
            # {'id': '28', 'url': 'store'},
            # {'id': '29', 'url': 'notary'},
            # {'id': '30', 'url': 'jeweller'},
            # {'id': '31', 'url': 'tailor'},
            # {'id': '32', 'url': 'meat'},
            # {'id': '33', 'url': 'library'},
            # {'id': '34', 'url': 'architect'},
            {'id': '36', 'url': 'cement'},
            {'id': '37', 'url': 'heating'},
            {'id': '38', 'url': 'naval'},
            {'id': '39', 'url': 'cold'},
            {'id': '41', 'url': 'steel'},
            {'id': '42', 'url': 'chemicals'},
            {'id': '43', 'url': 'gas'},
            {'id': '44', 'url': 'gold+buyer'}
        ]

        capitales_du_monde = [
            {'id': '237', 'nom': 'around pristina'}
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get('url')

                        var = 1

                        i = 1

                        while var == 1:
                            url_search = "http://www.yellowpageskosovo.com/?s=" + activity + "&a=true&lang=en&paged=" \
                                         + str(i)
                            print(url_search)
                            html_search = requests.get(url_search)
                            soup_search = BeautifulSoup(html_search.content, 'html.parser')

                            i_1 = 0

                            if soup_search.select_one('#content') is not None:
                                if soup_search\
                                        .select_one('#content')\
                                        .find('div', {'class': 'item-container'}) is not None:
                                    for result_item in soup_search \
                                            .select_one('#content') \
                                            .find_all('div', {'class': 'item-container'}):
                                        i_1 += 1

                                        url_result = result_item \
                                            .find('div', {'class': 'content'}) \
                                            .find('div', {'class': 'item-image'}) \
                                            .find('a', {'class': 'main-link'}) \
                                            .get('href')

                                        time.sleep(2)

                                        # Request the content of a page from the url
                                        html = requests.get(url_result)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        if soup.find('a', {'itemprop': 'email'}) is not None:
                                            email = "info@" + soup.find('a', {'itemprop': 'email'}).text.split("@")[1]

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
                                                        print(str(e) + " - " + str(i_1) + " The record already exists : " + email)
                                                        connection.close()
                                            except Exception as e:
                                                print(str(e) + " - " + str(i_1) + " An error with the email : " + email)
                                        else:
                                            print(str(i_1) + ' no email business')

                                    i += 1
                                else:
                                    print("no item container")
                            else:
                                print("sorry there is nothing")
                                break
                    except Exception as e:
                        print(str(e) + " There is an error connection at url")
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
