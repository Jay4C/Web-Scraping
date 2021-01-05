import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesLithuania(unittest.TestCase):
    def test_extract_one_email(self):
        url = "https://www.visalietuva.lt/en/company/astorija-hotel-uab"

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
        city = "vilniuje"
        url_search = "https://www.visalietuva.lt/en/search/" + activity + "/" + city
        html_search = requests.get(url_search)
        soup_search = BeautifulSoup(html_search.content, 'html.parser')
        number_of_pages = 0

        if soup_search.find('div', {'class': 'search_count f_left'}) is not None:
            number_of_pages_with_coma = int(soup_search
                                            .find('div', {'class': 'search_count f_left'})
                                            .find('span').text
                                            )/20

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))

        i_1 = 0

        if soup_search.find('div', {'class': 'company_list'}) is not None:
            print(url_search)
            for result_item in soup_search \
                    .find('div', {'class': 'company_list'}) \
                    .find_all('div', {'class': 'item'}):
                i_1 += 1

                url_result = result_item.find('a', {'class': 'company-item-title'}).get('href')

                time.sleep(2)

                # Request the content of a page from the url
                html_result = requests.get(url_result)

                # Parse the content of html_doc
                soup_result = BeautifulSoup(html_result.content, 'html.parser')

                if soup_result.find('a', {'itemprop': 'email'}) is not None:
                    email = "info@" + soup_result.find('a', {'itemprop': 'email'}).text.split("@")[1]
                    print(str(i_1) + ' email : ' + email)
                else:
                    print(str(i_1) + ' no email business')
        else:
            print('sorry there is nothing')

        if number_of_pages > 1:
            for i in range(2, number_of_pages+1):
                url_of_one_page_of_results = url_search + "/" + str(i)
                print(url_of_one_page_of_results)
                time.sleep(2)
                html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                if soup_of_one_page_of_results.find('div', {'class': 'company_list'}) is not None:
                    for result_item in soup_of_one_page_of_results\
                            .find('div', {'class': 'company_list'})\
                            .find_all('div', {'class': 'item'}):
                        i_1 += 1

                        url_result = result_item.find('a', {'class': 'company-item-title'}).get('href')

                        # Request the content of a page from the url
                        html_result = requests.get(url_result)

                        # Parse the content of html_doc
                        soup_result = BeautifulSoup(html_result.content, 'html.parser')

                        if soup_result.find('a', {'itemprop': 'email'}) is not None:
                            email = "info@" + soup_result.find('a', {'itemprop': 'email'}).text.split("@")[1]
                            print(str(i_1) + ' email : ' + email)
                        else:
                            print(str(i_1) + ' no email business')
                else:
                    print('sorry there is nothing')

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            # {'id': '1', 'url': 'labour'}
            #{'id': '2', 'url': 'real+estate'},
            #{'id': '3', 'url': 'recruitment'},
            #{'id': '4', 'url': 'software'},
            #{'id': '5', 'url': 'hotel'},
            #{'id': '6', 'url': 'landlord'},
            #{'id': '7', 'url': 'cleaning'},
            #{'id': '8', 'url': 'association'},
            #{'id': '9', 'url': 'financial'},
            #{'id': '10', 'url': 'restaurant'},
            #{'id': '11', 'url': 'building'},
            #{'id': '12', 'url': 'hairdresser'},
            #{'id': '13', 'url': 'florist'},
            #{'id': '14', 'url': 'locksmith'},
            #{'id': '15', 'url': 'bakery'},
            #{'id': '16', 'url': 'insurance'},
            #{'id': '17', 'url': 'pharmacy'},
            #{'id': '18', 'url': 'moving'},
            #{'id': '19', 'url': 'electricity'},
            #{'id': '20', 'url': 'plumbing'},
            #{'id': '21', 'url': 'security'},
            #{'id': '22', 'url': 'lawyer'},
            #{'id': '23', 'url': 'bank'},
            #{'id': '24', 'url': 'garage'},
            #{'id': '25', 'url': 'dentist'},
            #{'id': '26', 'url': 'doctor'},
            #{'id': '27', 'url': 'accounting'},
            #{'id': '28', 'url': 'store'},
            #{'id': '29', 'url': 'notary'},
            #{'id': '30', 'url': 'jeweller'},
            #{'id': '31', 'url': 'tailor'},
            #{'id': '32', 'url': 'meat'},
            #{'id': '33', 'url': 'library'},
            #{'id': '34', 'url': 'architect'}
        ]

        capitales_du_monde = [
            {'id': '183', 'nom': 'akmeneje'},#Akmenė
            {'id': '184', 'nom': 'alytuje'},#Alytus
            {'id': '185', 'nom': 'anyksciuose'},#Anykščiai
            {'id': '186', 'nom': 'birstone'},#Birštonas
            {'id': '187', 'nom': 'birzuose'},#Biržai
            {'id': '188', 'nom': 'druskininkuose'},#Druskininkai
            {'id': '189', 'nom': 'elektrenuose'},#Elektrėnai
            {'id': '190', 'nom': 'ignalinoje'},#Ignalina
            {'id': '191', 'nom': 'jonavoje'},#Jonava
            {'id': '192', 'nom': 'joniskyje'},#Joniškis
            {'id': '193', 'nom': 'jurbarke'},#Jurbarkas
            {'id': '194', 'nom': 'kaisiadoryse'},#Kaišiadorys
            {'id': '195', 'nom': 'kalvarijoje'},#Kalvarija
            {'id': '196', 'nom': 'kaune'},#Kaunas
            {'id': '197', 'nom': 'kazlu-rudoje'},#Kazlų Rūda
            {'id': '198', 'nom': 'kedainiuose'},#Kėdainiai
            {'id': '199', 'nom': 'kelmeje'},#Kelmė
            {'id': '200', 'nom': 'klaipedoje'},#Klaipėda
            {'id': '201', 'nom': 'kretingoje'},#Kretinga
            {'id': '202', 'nom': 'kupiskyje'},#Kupiškis
            {'id': '203', 'nom': 'lazdijuose'},#Lazdijai
            {'id': '204', 'nom': 'marijampoleje'},#Marijampolė
            {'id': '205', 'nom': 'mazeikiuose'},#Mažeikiai
            {'id': '206', 'nom': 'moletuose'},#Molėtai
            {'id': '207', 'nom': 'neringoje'},#Neringa
            {'id': '208', 'nom': 'pagegiuose'},#Pagėgiai
            {'id': '209', 'nom': 'pakruojyje'},#Pakruojis
            {'id': '210', 'nom': 'palangoje'},#Palanga
            {'id': '211', 'nom': 'panevezyje'},#Panevėžys
            {'id': '212', 'nom': 'pasvalyje'},#Pasvalys
            {'id': '213', 'nom': 'plungeje'},#Plungė
            {'id': '214', 'nom': 'prienuose'},#Prienai
            {'id': '215', 'nom': 'radviliskyje'},#Radviliškis
            {'id': '216', 'nom': 'raseiniuose'},#Raseiniai
            {'id': '217', 'nom': 'rietave'},#Rietavas
            {'id': '218', 'nom': 'rokiskyje'},#Rokiškis
            {'id': '219', 'nom': 'sakiuose'},#Šakiai
            {'id': '220', 'nom': 'salcininkuose'},#Šalčininkai
            {'id': '221', 'nom': 'siauliuose'},#Šiauliai
            {'id': '222', 'nom': 'silaleje'},#Šilalė
            {'id': '223', 'nom': 'siluteje'},#Šilutė
            {'id': '224', 'nom': 'sirvintose'},#Širvintos
            {'id': '225', 'nom': 'skuode'},#Skuodas
            {'id': '226', 'nom': 'svencionyse'},#Švenčionys
            {'id': '227', 'nom': 'taurageje'},#Tauragė
            {'id': '228', 'nom': 'telsiuose'},#Telšiai
            {'id': '229', 'nom': 'trakuose'},#Trakai
            {'id': '230', 'nom': 'ukmergeje'},#Ukmergė
            {'id': '231', 'nom': 'utenoje'},#Utena
            {'id': '232', 'nom': 'varenoje'},#Varėna
            {'id': '233', 'nom': 'vilkaviskyje'},#Vilkaviškis
            {'id': '234', 'nom': 'vilniuje'},#Vilnius
            {'id': '235', 'nom': 'visagine'},#Visaginas
            {'id': '236', 'nom': 'zarasuose'}#Zarasai
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get("url")
                        city = capitale.get("nom")
                        url_search = "https://www.visalietuva.lt/en/search/" + activity + "/" + city
                        html_search = requests.get(url_search)
                        soup_search = BeautifulSoup(html_search.content, 'html.parser')
                        number_of_pages = 0

                        if soup_search.find('div', {'class': 'search_count f_left'}) is not None:
                            number_of_pages_with_coma = int(soup_search
                                                            .find('div', {'class': 'search_count f_left'})
                                                            .find('span').text
                                                            ) / 20

                            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                number_of_pages += round(number_of_pages_with_coma) + 1
                                print('number_of_pages : ' + str(number_of_pages))

                            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                number_of_pages += round(number_of_pages_with_coma)
                                print('number_of_pages : ' + str(number_of_pages))

                        i_1 = 0

                        if soup_search.find('div', {'class': 'company_list'}) is not None:
                            print(url_search)
                            for result_item in soup_search \
                                    .find('div', {'class': 'company_list'}) \
                                    .find_all('div', {'class': 'item'}):
                                i_1 += 1

                                url_result = result_item.find('a', {'class': 'company-item-title'}).get('href')

                                time.sleep(2)

                                # Request the content of a page from the url
                                html_result = requests.get(url_result)

                                # Parse the content of html_doc
                                soup_result = BeautifulSoup(html_result.content, 'html.parser')

                                if soup_result.find('a', {'itemprop': 'email'}) is not None:
                                    email = "info@" + soup_result.find('a', {'itemprop': 'email'}).text.split("@")[1]

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
                                            except:
                                                print(str(i_1) + " The record already exists : " + email)
                                                connection.close()
                                    except Exception as e:
                                        print(str(i_1) + " An error with the email : " + email + " " + str(e))
                                else:
                                    print(str(i_1) + ' no email business')
                        else:
                            print('sorry there is nothing')

                        if number_of_pages > 1:
                            for i in range(2, number_of_pages + 1):
                                url_of_one_page_of_results = url_search + "/" + str(i)
                                print(url_of_one_page_of_results)
                                time.sleep(2)
                                html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                if soup_of_one_page_of_results.find('div', {'class': 'company_list'}) is not None:
                                    for result_item in soup_of_one_page_of_results \
                                            .find('div', {'class': 'company_list'}) \
                                            .find_all('div', {'class': 'item'}):
                                        i_1 += 1

                                        url_result = result_item.find('a', {'class': 'company-item-title'}).get('href')

                                        # Request the content of a page from the url
                                        html_result = requests.get(url_result)

                                        # Parse the content of html_doc
                                        soup_result = BeautifulSoup(html_result.content, 'html.parser')

                                        if soup_result.find('a', {'itemprop': 'email'}) is not None:
                                            email = "info@" + \
                                                    soup_result.find('a', {'itemprop': 'email'}).text.split("@")[1]

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
                                                    except:
                                                        print(str(i_1) + " The record already exists : " + email)
                                                        connection.close()
                                            except Exception as e:
                                                print(str(i_1) + " An error with the email : " + email + " " + str(e))
                                        else:
                                            print(str(i_1) + ' no email business')
                                else:
                                    print('sorry there is nothing')
                    except Exception as e:
                        print("There is an error connection at url : " + str(e))
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
