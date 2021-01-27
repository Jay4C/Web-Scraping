from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesBulgaria(unittest.TestCase):
    def test_extract_email_from_one_result(self):
        print("test_extract_email_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "http://www.goldenpages.bg/en/o/hotelmontecito-7031537"

        time.sleep(3)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("span", {'hashtype': 'content'}) is not None:
            email = "info@" + soup.find("span", {'hashtype': 'content'}) \
                .text \
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

        url = "http://www.goldenpages.bg/en/search/results?search[product]=hotel&search[location]=sofia/page/1"

        time.sleep(2)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('div', {'class': 'single-product'}) is not None:
            all_single_product = soup.find_all('div', {'class': 'single-product'})

            for single_product in all_single_product:
                url_single_product = 'http://www.goldenpages.bg' + single_product\
                    .find('div', {'class': 'h4'})\
                    .find('a')\
                    .get('href')

                time.sleep(2)

                # Request the content of a page from the url
                html = requests.get(url_single_product, headers=headers)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("span", {'hashtype': 'content'}) is not None:
                    email = "info@" + soup.find("span", {'hashtype': 'content'}) \
                        .text \
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

        city = "sofia"

        number_of_pages = 0

        url_page = "http://www.goldenpages.bg/en/search/results?search[product]=" + activity + "&search[location]=" + city

        time.sleep(2)

        html_search = requests.get(url_page, headers=headers)

        soup_search = BeautifulSoup(html_search.content, 'html.parser')

        if soup_search.find("div", {"class": "type-h1"}) is not None:
            number_of_pages_with_coma = int(soup_search.find("div", {"class": "type-h1"})
                                            .text
                                            .split("-")[1]
                                            .replace(" ", "")
                                            .replace("found", "")
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
                url = url_page + "/page/" + str(i)

                print(url)

                time.sleep(2)

                # Request the content of a page from the url
                html = requests.get(url, headers=headers)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find('div', {'class': 'single-product'}) is not None:
                    all_single_product = soup.find_all('div', {'class': 'single-product'})

                    for single_product in all_single_product:
                        i_1 += 1

                        url_single_product = 'http://www.goldenpages.bg' + single_product \
                            .find('div', {'class': 'h4'}) \
                            .find('a') \
                            .get('href')

                        time.sleep(2)

                        # Request the content of a page from the url
                        html = requests.get(url_single_product, headers=headers)

                        # Parse the content of html_doc
                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.find("span", {'hashtype': 'content'}) is not None:
                            email = "info@" + soup.find("span", {'hashtype': 'content'}) \
                                .text \
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
            if soup_search.find('div', {'class': 'single-product'}) is not None:
                all_single_product = soup_search.find_all('div', {'class': 'single-product'})

                for single_product in all_single_product:
                    i_1 += 1

                    url_single_product = 'http://www.goldenpages.bg' + single_product \
                        .find('div', {'class': 'h4'}) \
                        .find('a') \
                        .get('href')

                    time.sleep(2)

                    # Request the content of a page from the url
                    html = requests.get(url_single_product, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("span", {'hashtype': 'content'}) is not None:
                        email = "info@" + soup.find("span", {'hashtype': 'content'}) \
                            .text \
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
            {'id': '1', 'url': 'employment'},  # Temporary employment agencies
            {'id': '2', 'url': 'real+estate'},  # Real estate
            {'id': '3', 'url': 'recruitment'},  # Recruiter
            {'id': '4', 'url': 'software'},  # software
            {'id': '5', 'url': 'hotel'},  # hotel
            {'id': '6', 'url': 'social'},  # social landlord
            {'id': '7', 'url': 'cleaning'},  # cleaning
            {'id': '8', 'url': 'charity'},  # charity
            {'id': '9', 'url': 'financial'},  # financial
            {'id': '10', 'url': 'restaurant'},  # restaurant
            {'id': '11', 'url': 'building'},  # building
            {'id': '12', 'url': 'hairdresser'},  # hairdresser
            {'id': '13', 'url': 'florist'},  # florist
            {'id': '14', 'url': 'locksmith'},  # locksmith
            {'id': '15', 'url': 'bakery'},  # bakery
            {'id': '16', 'url': 'insurance'},  # insurance
            {'id': '17', 'url': 'pharmacy'},  # pharmacy
            {'id': '18', 'url': 'mover'},  # mover
            {'id': '19', 'url': 'electricity'},  # electricity
            {'id': '20', 'url': 'plumbing'},  # plumbing
            {'id': '21', 'url': 'security'},  # security
            {'id': '22', 'url': 'attorney'},  # attorney
            {'id': '23', 'url': 'bank'},  # bank
            {'id': '24', 'url': 'garage'},  # garage
            {'id': '25', 'url': 'dentist'},  # dentist
            {'id': '26', 'url': 'doctor'},  # doctor
            {'id': '27', 'url': 'accountant'},  # accountant
            {'id': '28', 'url': 'grocery'},  # grocery stores
            {'id': '29', 'url': 'notary'},  # notary
            {'id': '30', 'url': 'jewellery'},  # jewellery
            {'id': '31', 'url': 'tailor'},  # tailor
            {'id': '32', 'url': 'meat'},  # butcher
            {'id': '33', 'url': 'library'},  # library
            {'id': '34', 'url': 'architect'},  # architect
            {'id': '36', 'url': 'cement'},  # cement
            {'id': '37', 'url': 'heating'},  # heating
            {'id': '38', 'url': 'maritime'},  # boat
            {'id': '39', 'url': 'cold'},  # cold
            {'id': '41', 'url': 'steel'},  # steel
            {'id': '42', 'url': 'chemical'},  # chemical
            {'id': '43', 'url': 'gas'},  # gas
            {'id': '44', 'url': 'gold'}  # gold
        ]

        capitales_du_monde = [
            {'id': '751', 'nom': 'blagoevgrad', 'pays': 'Bulgaria'},
            {'id': '752', 'nom': 'burgas', 'pays': 'Bulgaria'},
            {'id': '753', 'nom': 'dobrich', 'pays': 'Bulgaria'},
            {'id': '754', 'nom': 'gabrovo', 'pays': 'Bulgaria'},
            {'id': '755', 'nom': 'haskovo', 'pays': 'Bulgaria'},
            {'id': '756', 'nom': 'kardzhali', 'pays': 'Bulgaria'},
            {'id': '757', 'nom': 'kyustendil', 'pays': 'Bulgaria'},
            {'id': '758', 'nom': 'lovech', 'pays': 'Bulgaria'},
            {'id': '759', 'nom': 'montana', 'pays': 'Bulgaria'},
            {'id': '760', 'nom': 'pazardzhik', 'pays': 'Bulgaria'},
            {'id': '761', 'nom': 'pernik', 'pays': 'Bulgaria'},
            {'id': '762', 'nom': 'pleven', 'pays': 'Bulgaria'},
            {'id': '763', 'nom': 'plovdiv', 'pays': 'Bulgaria'},
            {'id': '764', 'nom': 'razgrad', 'pays': 'Bulgaria'},
            {'id': '765', 'nom': 'ruse', 'pays': 'Bulgaria'},
            {'id': '766', 'nom': 'shumen', 'pays': 'Bulgaria'},
            {'id': '767', 'nom': 'silistra', 'pays': 'Bulgaria'},
            {'id': '768', 'nom': 'sliven', 'pays': 'Bulgaria'},
            {'id': '769', 'nom': 'smolyan', 'pays': 'Bulgaria'},
            {'id': '770', 'nom': 'sofia', 'pays': 'Bulgaria'},
            {'id': '771', 'nom': 'stara zagora', 'pays': 'Bulgaria'},
            {'id': '772', 'nom': 'targovishte', 'pays': 'Bulgaria'},
            {'id': '773', 'nom': 'varna', 'pays': 'Bulgaria'},
            {'id': '774', 'nom': 'veliko tarnovo', 'pays': 'Bulgaria'},
            {'id': '775', 'nom': 'vidin', 'pays': 'Bulgaria'},
            {'id': '776', 'nom': 'vratsa', 'pays': 'Bulgaria'},
            {'id': '777', 'nom': 'yambol', 'pays': 'Bulgaria'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    activity = activite.get('url')

                    city = capitale.get('nom')

                    number_of_pages = 0

                    url_page = "http://www.goldenpages.bg/en/search/results?search[product]=" + activity + "&search[location]=" + city

                    time.sleep(2)

                    html_search = requests.get(url_page, headers=headers)

                    soup_search = BeautifulSoup(html_search.content, 'html.parser')

                    if soup_search.find("div", {"class": "type-h1"}) is not None:
                        number_of_pages_with_coma = int(soup_search.find("div", {"class": "type-h1"})
                                                        .text
                                                        .split("-")[1]
                                                        .replace(" ", "")
                                                        .replace("found", "")
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
                            url = url_page + "/page/" + str(i)

                            print(url)

                            time.sleep(2)

                            # Request the content of a page from the url
                            html = requests.get(url, headers=headers)

                            # Parse the content of html_doc
                            soup = BeautifulSoup(html.content, 'html.parser')

                            if soup.find('div', {'class': 'single-product'}) is not None:
                                all_single_product = soup.find_all('div', {'class': 'single-product'})

                                for single_product in all_single_product:
                                    i_1 += 1

                                    url_single_product = 'http://www.goldenpages.bg' + single_product \
                                        .find('div', {'class': 'h4'}) \
                                        .find('a') \
                                        .get('href')

                                    time.sleep(2)

                                    # Request the content of a page from the url
                                    html = requests.get(url_single_product, headers=headers)

                                    # Parse the content of html_doc
                                    soup = BeautifulSoup(html.content, 'html.parser')

                                    if soup.find("span", {'hashtype': 'content'}) is not None:
                                        email = "info@" + soup.find("span", {'hashtype': 'content'}) \
                                            .text \
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
                        if soup_search.find('div', {'class': 'single-product'}) is not None:
                            all_single_product = soup_search.find_all('div', {'class': 'single-product'})

                            for single_product in all_single_product:
                                i_1 += 1

                                url_single_product = 'http://www.goldenpages.bg' + single_product \
                                    .find('div', {'class': 'h4'}) \
                                    .find('a') \
                                    .get('href')

                                time.sleep(2)

                                # Request the content of a page from the url
                                html = requests.get(url_single_product, headers=headers)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                if soup.find("span", {'hashtype': 'content'}) is not None:
                                    email = "info@" + soup.find("span", {'hashtype': 'content'}) \
                                        .text \
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
