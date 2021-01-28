import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesAngleterre(unittest.TestCase):
    def test_extract_one_email_from_one_result(self):
        url = "https://www.scoot.co.uk/England/-/London/The-Glenlyn-Hotel-500001032719.html"

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        time.sleep(3)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'data-yext-click': 'website'}) is not None:
            email = "info@" + soup.find('a', {'data-yext-click': 'website'}) \
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

        url = "https://www.scoot.co.uk/find/hotel-in-london"

        time.sleep(2)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'data-yext-click': 'name'}) is not None:
            all_single_product = soup.find_all('a', {'data-yext-click': 'name'})

            for single_product in all_single_product:
                url = 'https://www.scoot.co.uk' + single_product.get('href')

                time.sleep(2)

                # Request the content of a page from the url
                html = requests.get(url, headers=headers)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find('a', {'data-yext-click': 'website'}) is not None:
                    email = "info@" + soup.find('a', {'data-yext-click': 'website'}) \
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

        city = "london"

        number_of_pages = 0

        url_page = "https://www.scoot.co.uk/find/" + activity + "-in-" + city

        time.sleep(2)

        html = requests.get(url_page, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("span", {"class": "result-header-results"}) is not None:
            number_of_pages_with_coma = int(soup.find("span", {"class": "result-header-results"})
                                            .text
                                            .replace(" ", "")
                                            .replace("results", "")
                                            ) / 20

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
                if i <= 10:
                    url = url_page + "&page=" + str(i)

                    print(url)

                    time.sleep(2)

                    # Request the content of a page from the url
                    html = requests.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find('a', {'data-yext-click': 'name'}) is not None:
                        all_single_product = soup.find_all('a', {'data-yext-click': 'name'})

                        for single_product in all_single_product:
                            i_1 += 1

                            url = 'https://www.scoot.co.uk' + single_product.get('href')

                            time.sleep(2)

                            # Request the content of a page from the url
                            html = requests.get(url, headers=headers)

                            # Parse the content of html_doc
                            soup = BeautifulSoup(html.content, 'html.parser')

                            if soup.find('a', {'data-yext-click': 'website'}) is not None:
                                email = "info@" + soup.find('a', {'data-yext-click': 'website'}) \
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
            if soup.find('a', {'data-yext-click': 'name'}) is not None:
                all_single_product = soup.find_all('a', {'data-yext-click': 'name'})

                for single_product in all_single_product:
                    i_1 += 1

                    url = 'https://www.scoot.co.uk' + single_product.get('href')

                    time.sleep(2)

                    # Request the content of a page from the url
                    html = requests.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find('a', {'data-yext-click': 'website'}) is not None:
                        email = "info@" + soup.find('a', {'data-yext-click': 'website'}) \
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
            {'id': '1', 'url': 'employment'},  # Temporary employment agencies
            {'id': '2', 'url': 'real-estate'},  # Real estate
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
            {'id': '32', 'url': 'butcher'},  # butcher
            {'id': '33', 'url': 'library'},  # library
            {'id': '34', 'url': 'architect'},  # architect
            {'id': '36', 'url': 'cement'},  # cement
            {'id': '37', 'url': 'heating'},  # heating
            {'id': '38', 'url': 'boat'},  # boat
            {'id': '39', 'url': 'cold'},  # cold
            {'id': '41', 'url': 'steel'},  # steel
            {'id': '42', 'url': 'chemical'},  # chemical
            {'id': '43', 'url': 'gas'},  # gas
            {'id': '44', 'url': 'gold'}  # gold
        ]

        capitales_du_monde = [
            {'id': '820', 'nom': 'aberdeenshire', 'pays': 'united kingdom'},
            {'id': '821', 'nom': 'aberdeen', 'pays': 'united kingdom'},
            {'id': '822', 'nom': 'argyll', 'pays': 'united kingdom'},
            {'id': '823', 'nom': 'ards', 'pays': 'united kingdom'},
            {'id': '824', 'nom': 'antrim', 'pays': 'united kingdom'},
            {'id': '825', 'nom': 'angus', 'pays': 'united kingdom'},
            {'id': '826', 'nom': 'bath', 'pays': 'united kingdom'},
            {'id': '827', 'nom': 'blackburn-with-darwen', 'pays': 'united kingdom'},
            {'id': '828', 'nom': 'bournemouth', 'pays': 'united kingdom'},
            {'id': '829', 'nom': 'bedford', 'pays': 'united kingdom'},
            {'id': '830', 'nom': 'brighton', 'pays': 'united kingdom'},
            {'id': '831', 'nom': 'blackpool', 'pays': 'united kingdom'},
            {'id': '832', 'nom': 'bracknell-forest', 'pays': 'united kingdom'},
            {'id': '833', 'nom': 'bradford', 'pays': 'united kingdom'},
            {'id': '834', 'nom': 'bristol', 'pays': 'united kingdom'},
            {'id': '835', 'nom': 'bury', 'pays': 'united kingdom'},
            {'id': '836', 'nom': 'cheshire', 'pays': 'united kingdom'},
            {'id': '837', 'nom': 'clackmannanshire', 'pays': 'united kingdom'},
            {'id': '838', 'nom': 'calderdale', 'pays': 'united kingdom'},
            {'id': '839', 'nom': 'cumbria', 'pays': 'united kingdom'},
            {'id': '840', 'nom': 'carmarthenshire', 'pays': 'united kingdom'},
            {'id': '841', 'nom': 'cornwall', 'pays': 'united kingdom'},
            {'id': '842', 'nom': 'coventry', 'pays': 'united kingdom'},
            {'id': '843', 'nom': 'cardiff', 'pays': 'united kingdom'},
            {'id': '844', 'nom': 'croydon', 'pays': 'united kingdom'},
            {'id': '845', 'nom': 'conwy', 'pays': 'united kingdom'},
            {'id': '846', 'nom': 'darlington', 'pays': 'united kingdom'},
            {'id': '847', 'nom': 'derbyshire', 'pays': 'united kingdom'},
            {'id': '848', 'nom': 'denbighshire', 'pays': 'united kingdom'},
            {'id': '849', 'nom': 'derby', 'pays': 'united kingdom'},
            {'id': '850', 'nom': 'devon', 'pays': 'united kingdom'},
            {'id': '851', 'nom': 'dumfries', 'pays': 'united kingdom'},
            {'id': '852', 'nom': 'doncaster', 'pays': 'united kingdom'},
            {'id': '853', 'nom': 'dundee', 'pays': 'united kingdom'},
            {'id': '854', 'nom': 'dorset', 'pays': 'united kingdom'},
            {'id': '855', 'nom': 'ayrshire', 'pays': 'united kingdom'},
            {'id': '856', 'nom': 'edinburgh ', 'pays': 'united kingdom'},
            {'id': '857', 'nom': 'dunbartonshire', 'pays': 'united kingdom'},
            {'id': '858', 'nom': 'lothian', 'pays': 'united kingdom'},
            {'id': '859', 'nom': 'eilean-siar', 'pays': 'united kingdom'},
            {'id': '860', 'nom': 'renfrewshire', 'pays': 'united kingdom'},
            {'id': '861', 'nom': 'falkirk', 'pays': 'united kingdom'},
            {'id': '862', 'nom': 'fife', 'pays': 'united kingdom'},
            {'id': '863', 'nom': 'glasgow', 'pays': 'united kingdom'},
            {'id': '864', 'nom': 'highland', 'pays': 'united kingdom'},
            {'id': '865', 'nom': 'inverclyde', 'pays': 'united kingdom'},
            {'id': '866', 'nom': 'kirklees', 'pays': 'united kingdom'},
            {'id': '867', 'nom': 'knowsley', 'pays': 'united kingdom'},
            {'id': '868', 'nom': 'lancashire', 'pays': 'united kingdom'},
            {'id': '869', 'nom': 'leicester', 'pays': 'united kingdom'},
            {'id': '870', 'nom': 'leeds', 'pays': 'united kingdom'},
            {'id': '871', 'nom': 'liverpool', 'pays': 'united kingdom'},
            {'id': '872', 'nom': 'luton', 'pays': 'united kingdom'},
            {'id': '873', 'nom': 'manchester', 'pays': 'united kingdom'},
            {'id': '874', 'nom': 'middlesbrough', 'pays': 'united kingdom'},
            {'id': '875', 'nom': 'medway', 'pays': 'united kingdom'},
            {'id': '876', 'nom': 'midlothian', 'pays': 'united kingdom'},
            {'id': '877', 'nom': 'moray', 'pays': 'united kingdom'},
            {'id': '878', 'nom': 'newcastle', 'pays': 'united kingdom'},
            {'id': '879', 'nom': 'nottingham', 'pays': 'united kingdom'},
            {'id': '880', 'nom': 'lanarkshire ', 'pays': 'united kingdom'},
            {'id': '881', 'nom': 'lincolnshire', 'pays': 'united kingdom'},
            {'id': '882', 'nom': 'somerset', 'pays': 'united kingdom'},
            {'id': '883', 'nom': 'tyneside', 'pays': 'united kingdom'},
            {'id': '884', 'nom': 'oldham', 'pays': 'united kingdom'},
            {'id': '885', 'nom': 'orkney', 'pays': 'united kingdom'},
            {'id': '886', 'nom': 'oxfordshire', 'pays': 'united kingdom'},
            {'id': '887', 'nom': 'pembrokeshire', 'pays': 'united kingdom'},
            {'id': '888', 'nom': 'perth', 'pays': 'united kingdom'},
            {'id': '889', 'nom': 'plymouth', 'pays': 'united kingdom'},
            {'id': '890', 'nom': 'portsmouth', 'pays': 'united kingdom'},
            {'id': '891', 'nom': 'peterborough', 'pays': 'united kingdom'},
            {'id': '892', 'nom': 'redcar', 'pays': 'united kingdom'},
            {'id': '893', 'nom': 'rochdale', 'pays': 'united kingdom'},
            {'id': '894', 'nom': 'reading', 'pays': 'united kingdom'},
            {'id': '895', 'nom': 'renfrewshire', 'pays': 'united kingdom'},
            {'id': '896', 'nom': 'rotherham', 'pays': 'united kingdom'},
            {'id': '897', 'nom': 'rutland', 'pays': 'united kingdom'},
            {'id': '898', 'nom': 'sandwell', 'pays': 'united kingdom'},
            {'id': '899', 'nom': 'suffolk', 'pays': 'united kingdom'},
            {'id': '900', 'nom': 'sefton', 'pays': 'united kingdom'},
            {'id': '901', 'nom': 'gloucestershire', 'pays': 'united kingdom'},
            {'id': '902', 'nom': 'sheffield', 'pays': 'united kingdom'},
            {'id': '903', 'nom': 'stockport', 'pays': 'united kingdom'},
            {'id': '904', 'nom': 'salford', 'pays': 'united kingdom'},
            {'id': '905', 'nom': 'slough', 'pays': 'united kingdom'},
            {'id': '906', 'nom': 'lanarkshire', 'pays': 'united kingdom'},
            {'id': '907', 'nom': 'sunderland', 'pays': 'united kingdom'},
            {'id': '908', 'nom': 'solihull', 'pays': 'united kingdom'},
            {'id': '909', 'nom': 'stirling', 'pays': 'united kingdom'},
            {'id': '910', 'nom': 'southampton', 'pays': 'united kingdom'},
            {'id': '911', 'nom': 'swindon', 'pays': 'united kingdom'},
            {'id': '912', 'nom': 'tameside', 'pays': 'united kingdom'},
            {'id': '913', 'nom': 'telford', 'pays': 'united kingdom'},
            {'id': '914', 'nom': 'thurrock', 'pays': 'united kingdom'},
            {'id': '915', 'nom': 'torbay', 'pays': 'united kingdom'},
            {'id': '916', 'nom': 'trafford', 'pays': 'united kingdom'},
            {'id': '917', 'nom': 'berkshire', 'pays': 'united kingdom'},
            {'id': '918', 'nom': 'dunbartonshire', 'pays': 'united kingdom'},
            {'id': '919', 'nom': 'wigan', 'pays': 'united kingdom'},
            {'id': '920', 'nom': 'wakefield', 'pays': 'united kingdom'},
            {'id': '921', 'nom': 'walsall', 'pays': 'united kingdom'},
            {'id': '922', 'nom': 'lothian', 'pays': 'united kingdom'},
            {'id': '923', 'nom': 'wolverhampton', 'pays': 'united kingdom'},
            {'id': '924', 'nom': 'windsor', 'pays': 'united kingdom'},
            {'id': '925', 'nom': 'wokingham', 'pays': 'united kingdom'},
            {'id': '926', 'nom': 'wirral', 'pays': 'united kingdom'},
            {'id': '927', 'nom': 'warrington', 'pays': 'united kingdom'},
            {'id': '928', 'nom': 'york', 'pays': 'united kingdom'},
            {'id': '929', 'nom': 'shetland', 'pays': 'united kingdom'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    activity = activite.get('url')

                    city = capitale.get('nom')

                    number_of_pages = 0

                    url_page = "https://www.scoot.co.uk/find/" + activity + "-in-" + city

                    time.sleep(2)

                    html = requests.get(url_page, headers=headers)

                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("span", {"class": "result-header-results"}) is not None:
                        number_of_pages_with_coma = int(soup.find("span", {"class": "result-header-results"})
                                                        .text
                                                        .replace(" ", "")
                                                        .replace("results", "")
                                                        ) / 20

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
                            if i <= 10:
                                url = url_page + "&page=" + str(i)

                                print(url)

                                time.sleep(2)

                                # Request the content of a page from the url
                                html = requests.get(url, headers=headers)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                if soup.find('a', {'data-yext-click': 'name'}) is not None:
                                    all_single_product = soup.find_all('a', {'data-yext-click': 'name'})

                                    for single_product in all_single_product:
                                        i_1 += 1

                                        url = 'https://www.scoot.co.uk' + single_product.get('href')

                                        time.sleep(2)

                                        # Request the content of a page from the url
                                        html = requests.get(url, headers=headers)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        if soup.find('a', {'data-yext-click': 'website'}) is not None:
                                            email = "info@" + soup.find('a', {'data-yext-click': 'website'}) \
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
                        if soup.find('a', {'data-yext-click': 'name'}) is not None:
                            all_single_product = soup.find_all('a', {'data-yext-click': 'name'})

                            for single_product in all_single_product:
                                i_1 += 1

                                url = 'https://www.scoot.co.uk' + single_product.get('href')

                                time.sleep(2)

                                # Request the content of a page from the url
                                html = requests.get(url, headers=headers)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                if soup.find('a', {'data-yext-click': 'website'}) is not None:
                                    email = "info@" + soup.find('a', {'data-yext-click': 'website'}) \
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
