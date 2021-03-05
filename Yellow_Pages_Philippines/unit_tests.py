from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesPhilippines(unittest.TestCase):
    def test_extract_email_from_one_result(self):
        print("test_extract_email_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.yellow-pages.ph/business/gv-tower-hotel"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"data-section": "email"}) is not None:
            email = "info@" + soup \
                .find("a", {"data-section": "email"}) \
                .get("href") \
                .replace('mailto:', '') \
                .split("@")[1] \
                .split("/")[0]

            print("email : " + email)
        else:
            print("no email business")

    def test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_one_page_results_one_activity_one_activity = "https://www.yellow-pages.ph/search/hotel/ipil-zamboanga-sibugay/page-1"

        # Request the content of a page from the url
        html_one_page_results_one_activity_one_activity = requests.get(url_one_page_results_one_activity_one_activity, headers=headers)

        # Parse the content of html_doc
        soup_one_page_results_one_activity_one_activity = BeautifulSoup(html_one_page_results_one_activity_one_activity.content, 'html.parser')

        if soup_one_page_results_one_activity_one_activity.find("a", {'class': 'yp-click'}) is not None:
            all_a = soup_one_page_results_one_activity_one_activity.find_all("a", {'class': 'yp-click'})

            for a in all_a:
                soup_one_page_result = "https://www.yellow-pages.ph" + a.get('href')

                time.sleep(3)

                # Request the content of a page from the url
                html_one_page_result = requests.get(soup_one_page_result, headers=headers)

                # Parse the content of html_doc
                soup_one_page_result = BeautifulSoup(html_one_page_result.content, 'html.parser')

                if soup_one_page_result.find("a", {"data-section": "email"}) is not None:
                    email = "info@" + soup_one_page_result \
                        .find("a", {"data-section": "email"}) \
                        .get("href") \
                        .replace('mailto:', '') \
                        .split("@")[1] \
                        .split("/")[0]

                    print("email : " + email)
                else:
                    print("no email business")
        else:
            print("no a class yp-click")

    def test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activity = "hotel"

        city = "ipil-zamboanga-sibugay"

        number_of_pages = 0

        url_page = "https://www.yellow-pages.ph/search/" + activity + "/" + city + "/page-"

        time.sleep(2)

        html_search = requests.get(url_page, headers=headers)

        soup_search = BeautifulSoup(html_search.content, 'html.parser')

        if soup_search.find("li", {"aria-current": "page"}) is not None:
            number_of_pages_with_coma = int(soup_search.find("li", {"aria-current": "page"})
                                            .text
                                            .split("(")[1]
                                            .replace(" ", "")
                                            .replace(")", "")
                                            .replace("\t", "")
                                            .replace("\n", "")
                                            .replace("\r", "")
                                            ) / 15

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
                url_one_page_results_one_activity_one_activity = url_page + str(i)

                print(url_one_page_results_one_activity_one_activity)

                time.sleep(3)

                # Request the content of a page from the url
                html_one_page_results_one_activity_one_activity = requests.get(
                    url_one_page_results_one_activity_one_activity, headers=headers)

                # Parse the content of html_doc
                soup_one_page_results_one_activity_one_activity = BeautifulSoup(
                    html_one_page_results_one_activity_one_activity.content, 'html.parser')

                if soup_one_page_results_one_activity_one_activity.find("a", {'class': 'yp-click'}) is not None:
                    all_a = soup_one_page_results_one_activity_one_activity.find_all("a", {'class': 'yp-click'})

                    for a in all_a:
                        i_1 += 1

                        soup_one_page_result = "https://www.yellow-pages.ph" + a.get('href')

                        time.sleep(3)

                        # Request the content of a page from the url
                        html_one_page_result = requests.get(soup_one_page_result, headers=headers)

                        # Parse the content of html_doc
                        soup_one_page_result = BeautifulSoup(html_one_page_result.content, 'html.parser')

                        if soup_one_page_result.find("a", {"data-section": "email"}) is not None:
                            email = "info@" + soup_one_page_result \
                                .find("a", {"data-section": "email"}) \
                                .get("href") \
                                .replace('mailto:', '') \
                                .split("@")[1] \
                                .split("/")[0]

                            print(str(i_1) + " email : " + email)
                        else:
                            print(str(i_1) + " no email business")
                else:
                    print("no a class yp-click")
        else:
            url_one_page_results_one_activity_one_activity = url_page + "1"

            print(url_one_page_results_one_activity_one_activity)

            time.sleep(3)

            # Request the content of a page from the url
            html_one_page_results_one_activity_one_activity = requests.get(
                url_one_page_results_one_activity_one_activity, headers=headers)

            # Parse the content of html_doc
            soup_one_page_results_one_activity_one_activity = BeautifulSoup(
                html_one_page_results_one_activity_one_activity.content, 'html.parser')

            if soup_one_page_results_one_activity_one_activity.find("a", {'class': 'yp-click'}) is not None:
                all_a = soup_one_page_results_one_activity_one_activity.find_all("a", {'class': 'yp-click'})

                for a in all_a:
                    i_1 += 1

                    soup_one_page_result = "https://www.yellow-pages.ph" + a.get('href')

                    time.sleep(3)

                    # Request the content of a page from the url
                    html_one_page_result = requests.get(soup_one_page_result, headers=headers)

                    # Parse the content of html_doc
                    soup_one_page_result = BeautifulSoup(html_one_page_result.content, 'html.parser')

                    if soup_one_page_result.find("a", {"data-section": "email"}) is not None:
                        email = "info@" + soup_one_page_result \
                            .find("a", {"data-section": "email"}) \
                            .get("href") \
                            .replace('mailto:', '') \
                            .split("@")[1] \
                            .split("/")[0]

                        print(str(i_1) + " email : " + email)
                    else:
                        print(str(i_1) + " no email business")
            else:
                print("no a class yp-click")

    def test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals(self):
        print("test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activites = [
            {'id': '1', 'url': 'temporary-employment-agencies'}, # Temporary employment agencies
            {'id': '2', 'url': 'real-estate'}, # Real estate
            {'id': '3', 'url': 'recruiter'}, # Recruiter
            {'id': '4', 'url': 'software'}, # software
            {'id': '5', 'url': 'hotel'}, # hotel
            {'id': '6', 'url': 'social-landlord'}, # social landlord
            {'id': '7', 'url': 'cleaning'}, # cleaning
            {'id': '8', 'url': 'charities'}, # Charities
            {'id': '9', 'url': 'financial'}, # financial
            {'id': '10', 'url': 'restaurant'}, # restaurant
            {'id': '11', 'url': 'building'}, # building
            {'id': '12', 'url': 'hairdresser'}, # hairdresser
            {'id': '13', 'url': 'florist'}, # florist
            {'id': '14', 'url': 'locksmith'}, # locksmith
            {'id': '15', 'url': 'bakery'}, # bakery
            {'id': '16', 'url': 'insurance'}, # insurance
            {'id': '17', 'url': 'pharmacies'}, # Pharmacies
            {'id': '18', 'url': 'movers'}, # movers
            {'id': '19', 'url': 'electricity'}, # electricity
            {'id': '20', 'url': 'plumbing'}, # plumbing
            {'id': '21', 'url': 'security'}, # security
            {'id': '22', 'url': 'attorney'}, # attorney
            {'id': '23', 'url': 'bank'}, # bank
            {'id': '24', 'url': 'mechanic'}, # mechanic
            {'id': '25', 'url': 'dentist'}, # dentist
            {'id': '26', 'url': 'doctor'}, # doctor
            {'id': '27', 'url': 'accountant'}, # accountant
            {'id': '28', 'url': 'grocery-stores'}, # Grocery Stores
            {'id': '29', 'url': 'notary'}, # notary
            {'id': '30', 'url': 'jewellery'}, # jewellery
            {'id': '31', 'url': 'tailors'}, # tailors
            {'id': '32', 'url': 'butcher'}, # butcher
            {'id': '33', 'url': 'library'}, # library
            {'id': '34', 'url': 'architects'}, # Architects
            {'id': '36', 'url': 'cement'}, # cement
            {'id': '37', 'url': 'heating'}, # heating
            {'id': '38', 'url': 'boat'}, # boat
            {'id': '39', 'url': 'cold'}, # cold
            {'id': '41', 'url': 'steel'}, # steel
            {'id': '42', 'url': 'chemicals'}, # chemicals
            {'id': '43', 'url': 'gas'}, # gas
            {'id': '44', 'url': 'gold'} # gold
        ]

        capitales_du_monde = [
            {'id': '954', 'nom': 'abra', 'pays': 'philippines'},
            {'id': '955', 'nom': 'agusan-del-norte', 'pays': 'philippines'},
            {'id': '956', 'nom': 'aklan', 'pays': 'philippines'},
            {'id': '957', 'nom': 'albay', 'pays': 'philippines'},
            {'id': '958', 'nom': 'apayao', 'pays': 'philippines'},
            {'id': '959', 'nom': 'aurora', 'pays': 'philippines'},
            {'id': '960', 'nom': 'basilan', 'pays': 'philippines'},
            {'id': '961', 'nom': 'bataan', 'pays': 'philippines'},
            {'id': '962', 'nom': 'batanes', 'pays': 'philippines'},
            {'id': '963', 'nom': 'batangas', 'pays': 'philippines'},
            {'id': '964', 'nom': 'benguet', 'pays': 'philippines'},
            {'id': '965', 'nom': 'biliran', 'pays': 'philippines'},
            {'id': '966', 'nom': 'bohol', 'pays': 'philippines'},
            {'id': '967', 'nom': 'bukidnon', 'pays': 'philippines'},
            {'id': '968', 'nom': 'bulacan', 'pays': 'philippines'},
            {'id': '969', 'nom': 'cagayan', 'pays': 'philippines'},
            {'id': '970', 'nom': 'camarines-norte', 'pays': 'philippines'},
            {'id': '971', 'nom': 'camarines-sur', 'pays': 'philippines'},
            {'id': '972', 'nom': 'camiguin', 'pays': 'philippines'},
            {'id': '973', 'nom': 'capiz', 'pays': 'philippines'},
            {'id': '974', 'nom': 'catanduanes', 'pays': 'philippines'},
            {'id': '975', 'nom': 'cavite', 'pays': 'philippines'},
            {'id': '976', 'nom': 'cebu', 'pays': 'philippines'},
            {'id': '977', 'nom': 'compostela-valley', 'pays': 'philippines'},
            {'id': '978', 'nom': 'south-cotabato', 'pays': 'philippines'},
            {'id': '979', 'nom': 'davao-del-norte', 'pays': 'philippines'},
            {'id': '980', 'nom': 'davao-del-sur', 'pays': 'philippines'},
            {'id': '981', 'nom': 'davao-oriental', 'pays': 'philippines'},
            {'id': '982', 'nom': 'dinagat-islands', 'pays': 'philippines'},
            {'id': '983', 'nom': 'eastern-samar', 'pays': 'philippines'},
            {'id': '984', 'nom': 'jordan-guimaras', 'pays': 'philippines'},
            {'id': '985', 'nom': 'ifugao', 'pays': 'philippines'},
            {'id': '986', 'nom': 'ilocos-norte', 'pays': 'philippines'},
            {'id': '987', 'nom': 'ilocos-sur', 'pays': 'philippines'},
            {'id': '988', 'nom': 'iloilo', 'pays': 'philippines'},
            {'id': '989', 'nom': 'isabela', 'pays': 'philippines'},
            {'id': '990', 'nom': 'kalinga', 'pays': 'philippines'},
            {'id': '991', 'nom': 'la-union', 'pays': 'philippines'},
            {'id': '992', 'nom': 'laguna', 'pays': 'philippines'},
            {'id': '993', 'nom': 'lanao-del-norte', 'pays': 'philippines'},
            {'id': '994', 'nom': 'lanao-del-sur', 'pays': 'philippines'},
            {'id': '995', 'nom': 'leyte', 'pays': 'philippines'},
            {'id': '996', 'nom': 'maguindanao', 'pays': 'philippines'},
            {'id': '997', 'nom': 'marinduque', 'pays': 'philippines'},
            {'id': '998', 'nom': 'masbate', 'pays': 'philippines'},
            {'id': '999', 'nom': 'misamis-occidental', 'pays': 'philippines'},
            {'id': '1000', 'nom': 'misamis-oriental', 'pays': 'philippines'},
            {'id': '1001', 'nom': 'mountain-province', 'pays': 'philippines'},
            {'id': '1002', 'nom': 'negros-occidental', 'pays': 'philippines'},
            {'id': '1003', 'nom': 'negros-oriental', 'pays': 'philippines'},
            {'id': '1004', 'nom': 'northern-samar', 'pays': 'philippines'},
            {'id': '1005', 'nom': 'nueva-ecija', 'pays': 'philippines'},
            {'id': '1006', 'nom': 'nueva-vizcaya', 'pays': 'philippines'},
            {'id': '1007', 'nom': 'mindoro-occidental', 'pays': 'philippines'},
            {'id': '1008', 'nom': 'mindoro-oriental', 'pays': 'philippines'},
            {'id': '1009', 'nom': 'palawan', 'pays': 'philippines'},
            {'id': '1010', 'nom': 'pampanga', 'pays': 'philippines'},
            {'id': '1011', 'nom': 'pangasinan', 'pays': 'philippines'},
            {'id': '1012', 'nom': 'quezon-province', 'pays': 'philippines'},
            {'id': '1013', 'nom': 'quirino', 'pays': 'philippines'},
            {'id': '1014', 'nom': 'rizal', 'pays': 'philippines'},
            {'id': '1015', 'nom': 'romblon', 'pays': 'philippines'},
            {'id': '1016', 'nom': 'northern-samar', 'pays': 'philippines'},
            {'id': '1017', 'nom': 'sarangani', 'pays': 'philippines'},
            {'id': '1018', 'nom': 'siquijor', 'pays': 'philippines'},
            {'id': '1019', 'nom': 'sorsogon', 'pays': 'philippines'},
            {'id': '1020', 'nom': 'southern-leyte', 'pays': 'philippines'},
            {'id': '1021', 'nom': 'sultan-kudarat', 'pays': 'philippines'},
            {'id': '1022', 'nom': 'sulu', 'pays': 'philippines'},
            {'id': '1023', 'nom': 'surigao-del-norte', 'pays': 'philippines'},
            {'id': '1024', 'nom': 'surigao-del-sur', 'pays': 'philippines'},
            {'id': '1025', 'nom': 'tarlac', 'pays': 'philippines'},
            {'id': '1026', 'nom': 'tawi-tawi', 'pays': 'philippines'},
            {'id': '1027', 'nom': 'zambales', 'pays': 'philippines'},
            {'id': '1028', 'nom': 'zamboanga-del-norte', 'pays': 'philippines'},
            {'id': '1029', 'nom': 'zamboanga-del-sur', 'pays': 'philippines'},
            {'id': '1030', 'nom': 'ipil-zamboanga-sibugay', 'pays': 'philippines'}
        ]

        for capitale in capitales_du_monde:
            for activite in activites:
                try:
                    activity = activite.get('url')

                    city = capitale.get('nom')

                    number_of_pages = 0

                    url_page = "https://www.yellow-pages.ph/search/" + activity + "/" + city + "/page-"

                    time.sleep(2)

                    html_search = requests.get(url_page, headers=headers)

                    soup_search = BeautifulSoup(html_search.content, 'html.parser')

                    if soup_search.find("li", {"aria-current": "page"}) is not None:
                        number_of_pages_with_coma = int(soup_search.find("li", {"aria-current": "page"})
                                                        .text
                                                        .split("(")[1]
                                                        .replace(" ", "")
                                                        .replace(")", "")
                                                        .replace("\t", "")
                                                        .replace("\n", "")
                                                        .replace("\r", "")
                                                        ) / 15

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
                            url_one_page_results_one_activity_one_activity = url_page + str(i)

                            print(url_one_page_results_one_activity_one_activity)

                            time.sleep(3)

                            # Request the content of a page from the url
                            html_one_page_results_one_activity_one_activity = requests.get(
                                url_one_page_results_one_activity_one_activity, headers=headers)

                            # Parse the content of html_doc
                            soup_one_page_results_one_activity_one_activity = BeautifulSoup(
                                html_one_page_results_one_activity_one_activity.content, 'html.parser')

                            if soup_one_page_results_one_activity_one_activity.find("a",
                                                                                    {'class': 'yp-click'}) is not None:
                                all_a = soup_one_page_results_one_activity_one_activity.find_all("a",
                                                                                                 {'class': 'yp-click'})

                                for a in all_a:
                                    try:
                                        i_1 += 1

                                        soup_one_page_result = "https://www.yellow-pages.ph" + a.get('href')

                                        time.sleep(3)

                                        # Request the content of a page from the url
                                        html_one_page_result = requests.get(soup_one_page_result, headers=headers)

                                        # Parse the content of html_doc
                                        soup_one_page_result = BeautifulSoup(html_one_page_result.content,
                                                                             'html.parser')

                                        if soup_one_page_result.find("a", {"data-section": "email"}) is not None:
                                            email = "info@" + soup_one_page_result \
                                                .find("a", {"data-section": "email"}) \
                                                .get("href") \
                                                .replace('mailto:', '') \
                                                .split("@")[1] \
                                                .split("/")[0]

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
                                    except Exception as e:
                                        print(str(i_1) + " error page : " + str(e))
                            else:
                                print("no a class yp-click")
                    else:
                        url_one_page_results_one_activity_one_activity = url_page + "1"

                        print(url_one_page_results_one_activity_one_activity)

                        time.sleep(3)

                        # Request the content of a page from the url
                        html_one_page_results_one_activity_one_activity = requests.get(
                            url_one_page_results_one_activity_one_activity, headers=headers)

                        # Parse the content of html_doc
                        soup_one_page_results_one_activity_one_activity = BeautifulSoup(
                            html_one_page_results_one_activity_one_activity.content, 'html.parser')

                        if soup_one_page_results_one_activity_one_activity.find("a", {'class': 'yp-click'}) is not None:
                            all_a = soup_one_page_results_one_activity_one_activity.find_all("a", {'class': 'yp-click'})

                            for a in all_a:
                                try:
                                    i_1 += 1

                                    soup_one_page_result = "https://www.yellow-pages.ph" + a.get('href')

                                    time.sleep(3)

                                    # Request the content of a page from the url
                                    html_one_page_result = requests.get(soup_one_page_result, headers=headers)

                                    # Parse the content of html_doc
                                    soup_one_page_result = BeautifulSoup(html_one_page_result.content, 'html.parser')

                                    if soup_one_page_result.find("a", {"data-section": "email"}) is not None:
                                        email = "info@" + soup_one_page_result \
                                            .find("a", {"data-section": "email"}) \
                                            .get("href") \
                                            .replace('mailto:', '') \
                                            .split("@")[1] \
                                            .split("/")[0]

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
                                except Exception as e:
                                    print(str(i_1) + ' error page : ' + str(e))
                        else:
                            print("no a class yp-click")
                except Exception as e:
                    print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
