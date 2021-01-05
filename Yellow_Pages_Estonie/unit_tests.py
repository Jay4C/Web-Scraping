from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesEstonie(unittest.TestCase):
    def test_extract_one_email(self):
        url = "https://www.yellowpages.ee/en/companies/116728-UUKREN-MOOBEL-OU.html"

        # Request the content of a page from the url
        html = requests.get(url)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'class': 'email catText'}) is not None:
            email = "info@" + soup.find('a', {'class': 'email catText'}).text.split("@")[1]
            print("email : " + email)
        else:
            print('no email business')

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        activity = "restaurant"
        city = "harjumaa"
        numero_page = "1"

        url_search = "https://www.yellowpages.ee/en/" + city \
                     + "/search.html?PageNum=" + numero_page + "&action=search&keyword=" \
                     + activity + "&regcode=&address=&url=&phone=&email="

        html_search = requests.get(url_search)
        soup_search = BeautifulSoup(html_search.content, 'html.parser')
        number_of_pages = 0

        if soup_search.find('h1', {'class': 'head'}) is not None:
            number_of_pages_with_coma = int(soup_search.find('h1', {'class': 'head'}).text
                                            .replace("Otsingule '", "")
                                            .replace("' leiti tulemusi: ", "")
                                            .replace(activity, "")
                                            .replace("\n", "")
                                            .replace(" ", ""))/20

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))

        i_1 = 0

        for i in range(1, number_of_pages+1):
            url_of_one_page_of_results = "https://www.yellowpages.ee/en/" + city \
                     + "/search.html?PageNum=" + str(i) + "&action=search&keyword=" \
                     + activity + "&regcode=&address=&url=&phone=&email="

            time.sleep(2)
            html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
            soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

            if soup_of_one_page_of_results.find('ul', {'class': 'comlistul'}) is not None:
                for result_item in soup_of_one_page_of_results.find('ul', {'class': 'comlistul'})\
                        .find_all('li'):
                    i_1 += 1

                    if result_item.find('a', {'class': 'url'}) is not None:
                        url_result = "https:" + result_item.find('a', {'class': 'url'}).get('href')

                        time.sleep(2)

                        # Request the content of a page from the url
                        html = requests.get(url_result)

                        # Parse the content of html_doc
                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.find('a', {'class': 'email catText'}) is not None:
                            email = "info@" + soup.find('a', {'class': 'email catText'}).text.split("@")[1]
                            print(str(i_1) + " email : " + email)
                        else:
                            print(str(i_1) + " no email business")
                    else:
                        print(str(i_1) + " no url page")
            else:
                print('sorry there is nothing')

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            {'id': '1', 'url': 'employment'},
            {'id': '2', 'url': 'real+estate'},
            {'id': '3', 'url': 'recruitment'},
            {'id': '4', 'url': 'software'},
            {'id': '5', 'url': 'hotel'},
            {'id': '6', 'url': 'landlord'},
            {'id': '7', 'url': 'cleaning'},
            {'id': '8', 'url': 'association'},
            {'id': '9', 'url': 'financial'},
            {'id': '10', 'url': 'restaurant'},
            {'id': '11', 'url': 'building'},
            {'id': '12', 'url': 'hairdresser'},
            {'id': '13', 'url': 'florist'},
            {'id': '14', 'url': 'locksmith'},
            {'id': '15', 'url': 'bakery'},
            {'id': '16', 'url': 'insurance'},
            {'id': '17', 'url': 'pharmacy'},
            {'id': '18', 'url': 'moving'},
            {'id': '19', 'url': 'electricity'},
            {'id': '20', 'url': 'plumbing'},
            {'id': '21', 'url': 'security'},
            {'id': '22', 'url': 'lawyer'},
            {'id': '23', 'url': 'bank'},
            {'id': '24', 'url': 'garage'},
            {'id': '25', 'url': 'dentist'},
            {'id': '26', 'url': 'doctor'},
            {'id': '27', 'url': 'accounting'},
            {'id': '28', 'url': 'grocery'},
            {'id': '29', 'url': 'notary'},
            {'id': '30', 'url': 'jeweller'},
            {'id': '31', 'url': 'tailor'},
            {'id': '32', 'url': 'meat'},
            {'id': '33', 'url': 'bookstore'},
            {'id': '34', 'url': 'architect'},
            {'id': '36', 'url': 'cement'},
            {'id': '37', 'url': 'heating'},
            {'id': '38', 'url': 'naval'},
            {'id': '39', 'url': 'cold'},
            {'id': '41', 'url': 'steel'},
            {'id': '42', 'url': 'chemicals'},
            {'id': '43', 'url': 'gas'},
            {'id': '44', 'url': 'gold'}
        ]

        capitales_du_monde = [
            {'id': '168', 'nom': 'harjumaa'}, #Tallinn
            {'id': '169', 'nom': 'hiiumaa'}, #Kärdla
            {'id': '170', 'nom': 'ida-virumaa'}, #Jõhvi
            {'id': '171', 'nom': 'jogevamaa'}, #Jõgeva
            {'id': '172', 'nom': 'jarvamaa'}, #Paide
            {'id': '173', 'nom': 'laanemaa'}, #Haapsalu
            {'id': '174', 'nom': 'laane-virumaa'}, #Rakvere
            {'id': '175', 'nom': 'polvamaa'}, #Põlva
            {'id': '176', 'nom': 'parnumaa'}, #Pärnu
            {'id': '177', 'nom': 'raplamaa'}, #Rapla
            {'id': '178', 'nom': 'saaremaa'}, #Kuressaare
            {'id': '179', 'nom': 'tartumaa'}, #Tartu
            {'id': '180', 'nom': 'valgamaa'}, #Valga
            {'id': '181', 'nom': 'viljandimaa'}, #Viljandi
            {'id': '182', 'nom': 'vorumaa'} #Võru
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get("url")
                        city = capitale.get("nom")
                        numero_page = "1"

                        url_search = "https://www.yellowpages.ee/en/" + city \
                                     + "/search.html?PageNum=" + numero_page + "&action=search&keyword=" \
                                     + activity + "&regcode=&address=&url=&phone=&email="

                        headers = {
                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                        }

                        html_search = requests.get(url_search, headers=headers)
                        soup_search = BeautifulSoup(html_search.content, 'html.parser')
                        number_of_pages = 0

                        if soup_search.find('h1', {'class': 'head'}) is not None:
                            number_of_pages_with_coma = int(soup_search.find('h1', {'class': 'head'}).text
                                                            .replace("Otsingule '", "")
                                                            .replace("' leiti tulemusi: ", "")
                                                            .replace(activity, "")
                                                            .replace("\n", "")
                                                            .replace(" ", "")) / 20

                            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                number_of_pages += round(number_of_pages_with_coma) + 1
                                print('number_of_pages : ' + str(number_of_pages))

                            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                number_of_pages += round(number_of_pages_with_coma)
                                print('number_of_pages : ' + str(number_of_pages))

                        i_1 = 0

                        for i in range(1, number_of_pages + 1):
                            url_of_one_page_of_results = "https://www.yellowpages.ee/en/" + city \
                                                         + "/search.html?PageNum=" + str(i) + "&action=search&keyword=" \
                                                         + activity + "&regcode=&address=&url=&phone=&email="

                            time.sleep(2)

                            headers = {
                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                            }

                            html_of_one_page_of_results = requests.get(url_of_one_page_of_results, headers=headers)

                            soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                        'html.parser')

                            if soup_of_one_page_of_results.find('ul', {'class': 'comlistul'}) is not None:
                                for result_item in soup_of_one_page_of_results.find('ul', {'class': 'comlistul'}) \
                                        .find_all('li'):
                                    i_1 += 1

                                    if result_item.find('a', {'class': 'url'}) is not None:
                                        url_result = "https:" + result_item.find('a', {'class': 'url'}).get('href')

                                        time.sleep(2)

                                        headers = {
                                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                                        }

                                        # Request the content of a page from the url
                                        html = requests.get(url_result, headers=headers)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        if soup.find('a', {'class': 'email catText'}) is not None:
                                            email = "info@" + \
                                                    soup.find('a', {'class': 'email catText'}).text.split("@")[1]

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
                                                        print(str(i_1) + " The record already exists : " + str(email) + " - " + str(e))
                                                        connection.close()
                                            except Exception as e:
                                                print(str(i_1) + " An error with the email : " + email + " - " + str(e))
                                        else:
                                            print(str(i_1) + " no email business")
                                    else:
                                        print(str(i_1) + " no url page")
                            else:
                                print('sorry there is nothing')
                    except Exception as e:
                        print("There is an error connection at url : " + str(e))
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
